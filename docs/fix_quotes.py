import re

with open('countability-onepager.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all ``...'' with \textit{...}
content = re.sub(r"``([^']+)''", r'\\textit{\1}', content)

# Also handle Japanese quotes 「...」
content = re.sub(r'「([^」]+)」', r'\\textit{\1}', content)

with open('countability-onepager.tex', 'w', encoding='utf-8') as f:
    f.write(content)

print('Replacements complete')
