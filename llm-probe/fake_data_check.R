#!/usr/bin/env Rscript
# fake_data_check.R — Gelman-style: fit the model to simulated data
# before collecting real data. Confirms the analysis pipeline works,
# the model recovers known effects, and the design can detect
# the predicted interaction.
#
# Usage: Rscript fake_data_check.R

library(brms)
library(dplyr)
library(tidyr)
library(ggplot2)

set.seed(42)

# --- Design parameters ---
n_vps     <- 16
n_models  <- 3
n_reps    <- 50   # Likert reps per item per model
nouns     <- c("people", "folks")
dets      <- c("three", "several")
constructions <- c("existential", "agentive")

# --- Generate the design matrix (one row per item-level mean) ---
design <- expand.grid(
  vp_set       = 1:n_vps,
  noun         = nouns,
  det          = dets,
  construction = constructions,
  model        = paste0("model", 1:n_models),
  stringsAsFactors = FALSE
)

cat("Design:", nrow(design), "rows (item-level means)\n")
cat("  =", n_vps, "VPs ×", length(nouns), "nouns ×",
    length(dets), "dets ×", length(constructions), "constructions ×",
    n_models, "models\n\n")

# --- Simulate under the PREDICTED effect ---
# Grand mean: ~5.0 (most sentences are acceptable)
# Noun effect: folks slightly lower than people (-0.3)
# Det effect: three slightly lower than several (-0.2)
# Construction effect: existential slightly lower than agentive (-0.1)
# KEY: three-way interaction: three × folks × existential = -0.8
#   (existentials degrade three folks more than three people)
#   (no such interaction for several)

grand_mean <- 5.0

# Treatment coding: people=0, folks=1; three=0, several=1; exist=0, agent=1
design <- design %>%
  mutate(
    noun_c  = ifelse(noun == "folks", 1, 0),
    det_c   = ifelse(det == "several", 1, 0),
    const_c = ifelse(construction == "agentive", 1, 0)
  )

# Fixed effects (the "true" parameters)
b_noun  <- -0.3   # folks slightly lower
b_det   <- -0.2   # three slightly lower
b_const <- -0.1   # existential slightly lower
b_noun_det   <- 0.0   # no noun × det interaction
b_noun_const <- 0.0   # no noun × construction interaction
b_det_const  <- 0.0   # no det × construction interaction
b_three_way  <- -0.8  # THE KEY: three × folks × existential

# Random effects
sd_vp    <- 0.3   # VP-level variability
sd_model <- 0.2   # model-level variability
residual_sd <- 0.5  # residual noise on item means

# Generate random intercepts
vp_effects <- rnorm(n_vps, 0, sd_vp)
model_effects <- rnorm(n_models, 0, sd_model)

design <- design %>%
  mutate(
    vp_re    = vp_effects[vp_set],
    model_re = model_effects[as.numeric(factor(model))],
    # Linear predictor
    mu = grand_mean +
      b_noun * noun_c +
      b_det * det_c +
      b_const * const_c +
      b_noun_det * noun_c * det_c +
      b_noun_const * noun_c * const_c +
      b_det_const * det_c * const_c +
      b_three_way * noun_c * det_c * const_c +  # note: three_way fires when
                                                  # noun=folks, det=three, const=exist
                                                  # i.e., noun_c=1, det_c=0, const_c=0
                                                  # so the interaction term is 0 here!
      vp_re + model_re
  )

# Wait — the three-way interaction as coded fires when all three dummies = 1.
# But our coding has three=0, several=1 and exist=0, agent=1.
# The prediction is: three × folks × existential is LOW.
# That means we need the interaction to fire when noun=folks, det=three, const=exist.
# With our coding: noun_c=1, det_c=0, const_c=0 → product = 0. Wrong.
#
# Recode: three=1, several=0; exist=1, agent=0.
# Then the interaction fires when noun=folks(1) × det=three(1) × const=exist(1) = 1.

design <- design %>%
  mutate(
    det_c   = ifelse(det == "three", 1, 0),
    const_c = ifelse(construction == "existential", 1, 0),
    # Recompute
    mu = grand_mean +
      b_noun * noun_c +
      b_det * det_c +
      b_const * const_c +
      b_noun_det * noun_c * det_c +
      b_noun_const * noun_c * const_c +
      b_det_const * det_c * const_c +
      b_three_way * noun_c * det_c * const_c +
      vp_re + model_re,
    # Simulate observed mean rating (clipped to 1-7)
    mean_rating = pmin(7, pmax(1, rnorm(n(), mu, residual_sd)))
  )

# --- Check the cell means ---
cat("Simulated cell means (true interaction = -0.8):\n")
cell_means <- design %>%
  group_by(noun, det, construction) %>%
  summarise(mean = mean(mean_rating), sd = sd(mean_rating), .groups = "drop") %>%
  arrange(noun, det, construction)
print(as.data.frame(cell_means), row.names = FALSE)

# The interaction: (exist - agent) for three folks MINUS (exist - agent) for three people
interaction_check <- cell_means %>%
  pivot_wider(names_from = construction, values_from = c(mean, sd)) %>%
  mutate(exist_agent_diff = mean_existential - mean_agentive)
cat("\nExistential - agentive difference:\n")
print(as.data.frame(interaction_check[, c("noun", "det", "exist_agent_diff")]),
      row.names = FALSE)

# --- Fit the model ---
cat("\nFitting brms model...\n")
cat("(model as fixed effect — only 3 levels, too few for random)\n")
fit <- brm(
  mean_rating ~ noun * det * construction + model + (1 | vp_set),
  data = design,
  family = gaussian(),
  chains = 4,
  iter = 4000,
  warmup = 2000,
  seed = 42,
  control = list(adapt_delta = 0.95),
  silent = 2,
  refresh = 0
)

cat("\nModel summary:\n")
print(summary(fit))

# --- Check: does the model recover the interaction? ---
cat("\nPosterior for the three-way interaction:\n")
cat("(brms codes nounpeople as the contrast; the interaction for folks\n")
cat(" is recovered from the two-way detthree:constructionexistential)\n\n")
post <- as_draws_df(fit)

# The two-way det:construction gives the exist-agent difference for THREE
# when noun=folks (reference level). This is the focal penalty.
twoway_col <- "b_detthree:constructionexistential"
threeway_col <- "b_nounpeople:detthree:constructionexistential"

if (all(c(twoway_col, threeway_col) %in% names(post))) {
  twoway <- post[[twoway_col]]
  threeway <- post[[threeway_col]]

  cat("  detthree:constructionexistential (= effect for FOLKS):\n")
  cat(sprintf("    Posterior mean: %.3f (true: %.1f)\n", mean(twoway), b_three_way))
  cat(sprintf("    95%% CI: [%.3f, %.3f]\n",
              quantile(twoway, 0.025), quantile(twoway, 0.975)))
  cat(sprintf("    P(< 0): %.3f\n\n", mean(twoway < 0)))

  cat("  nounpeople:detthree:constructionexistential (= people UNDOES the penalty):\n")
  cat(sprintf("    Posterior mean: %.3f (true: %.1f)\n", mean(threeway), -b_three_way))
  cat(sprintf("    95%% CI: [%.3f, %.3f]\n",
              quantile(threeway, 0.025), quantile(threeway, 0.975)))
  cat(sprintf("    P(> 0): %.3f\n", mean(threeway > 0)))
} else {
  cat("  Could not find interaction terms. Available:\n")
  cat("  ", grep("^b_", names(post), value = TRUE), "\n")
}

# --- Plot cell means ---
cell_plot <- design %>%
  group_by(noun, det, construction) %>%
  summarise(
    m = mean(mean_rating),
    lo = m - 1.96 * sd(mean_rating) / sqrt(n()),
    hi = m + 1.96 * sd(mean_rating) / sqrt(n()),
    .groups = "drop"
  )

p <- ggplot(cell_plot, aes(x = construction, y = m, colour = noun, group = noun)) +
  geom_point(position = position_dodge(0.3), size = 3) +
  geom_errorbar(aes(ymin = lo, ymax = hi), width = 0.15,
                position = position_dodge(0.3)) +
  geom_line(position = position_dodge(0.3), linetype = "dashed") +
  facet_wrap(~ det) +
  labs(
    title = "Fake data: simulated cell means with 95% CIs",
    subtitle = sprintf("True three-way interaction = %.1f", b_three_way),
    y = "Mean rating (1-7)",
    x = "Construction",
    colour = "Noun"
  ) +
  theme_minimal(base_size = 14) +
  scale_colour_manual(values = c("people" = "#2E5077", "folks" = "#E85D4C"))

ggsave("results/fake_data_cell_means.pdf", p, width = 8, height = 4)
cat("\nPlot saved to results/fake_data_cell_means.pdf\n")

cat("\n=== FAKE DATA CHECK COMPLETE ===\n")
cat("If the model recovered the interaction (posterior mean near -0.8,\n")
cat("95% CI excluding 0), the analysis pipeline works and the design\n")
cat("can detect the predicted effect. Proceed to real data collection.\n")
