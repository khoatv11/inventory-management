import os
import glob

# Get all HTML files in the current directory
html_files = glob.glob('*.html')

for filepath in html_files:
    # Read the content of the file
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Filter out lines that contain class="page-subtitle"
    new_lines = [line for line in lines if 'class="page-subtitle"' not in line]
    
    # Write the modified content back to the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

print("Removed page-subtitle from all HTML files.")
