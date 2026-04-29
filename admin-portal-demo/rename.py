import os
import re

html_files = [
    'adjustment-create.html', 'adjustments.html', 'index.html',
    'products.html', 'report-fluctuation.html', 'report-overall.html',
    'returns.html', 'units.html'
]

# Rename units.html to index.html if units.html exists
if os.path.exists('units.html'):
    if os.path.exists('index.html'):
        os.remove('index.html')
    os.rename('units.html', 'index.html')

# Update references in all HTML files
for fname in html_files:
    # After renaming, units.html is now index.html, so skip units.html
    if fname == 'units.html':
        continue
        
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content.replace('href="units.html"', 'href="index.html"')
        
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Renamed and updated links successfully.")
