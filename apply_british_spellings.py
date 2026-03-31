#!/usr/bin/env python3
"""Apply British spellings (Oxford -ize style) to main.tex"""

import re

# British spelling conversions (excluding -ize/-ise which we keep as -ize)
CONVERSIONS = [
    # -or to -our
    (r'\b(behavio)(r)\b', r'\1ur'),
    (r'\b(colo)(r)\b', r'\1ur'),
    (r'\b(favo)(r)\b', r'\1ur'),
    (r'\b(hono)(r)\b', r'\1ur'),
    (r'\b(labo)(r)\b', r'\1ur'),
    (r'\b(neighbo)(r)\b', r'\1ur'),
    (r'\b(flavo)(r)\b', r'\1ur'),
    (r'\b(rumo)(r)\b', r'\1ur'),
    (r'\b(vigo)(r)\b', r'\1ur'),
    
    # -er to -re
    (r'\b(cent)(er)\b', r'\1re'),
    (r'\b(theat)(er)\b', r'\1re'),
    (r'\b(met)(er)\b', r'\1re'),
    (r'\b(lit)(er)\b', r'\1re'),
    
    # -og to -ogue  
    (r'\b(analo)(g)\b', r'\1gue'),
    (r'\b(catalo)(g)\b', r'\1gue'),
    (r'\b(dialo)(g)\b', r'\1gue'),
    
    # -ense to -ence (nouns)
    (r'\b(defen)(se)\b', r'\1ce'),
    (r'\b(offen)(se)\b', r'\1ce'),
    (r'\b(preten)(se)\b', r'\1ce'),
    
    # Special case: license (verb) vs licence (noun) - convert all to licence
    (r'\blicen(se)\b', r'licen\1'),
]

with open('main.tex', 'r', encoding='utf-8') as f:
    content = f.read()

original_content = content

# Apply conversions
for pattern, replacement in CONVERSIONS:
    content = re.sub(pattern, replacement, content)

# Count changes
changes_made = (content != original_content)

if changes_made:
    with open('main.tex', 'w', encoding='utf-8') as f:
        f.write(content)
    print("British spellings applied successfully")
    print(f"File size: {len(content)} bytes")
else:
    print("No American spellings found to convert")
