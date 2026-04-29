import os
import re

html_files = [
    'adjustment-create.html', 'adjustments.html', 'index.html',
    'products.html', 'report-fluctuation.html', 'report-overall.html',
    'returns.html', 'units.html'
]

# 1. Update adjustments.html to inject cards
adj_file = 'adjustments.html'
with open(adj_file, 'r', encoding='utf-8') as f:
    content = f.read()

cards_html = '''                    </div>
                    <div class="dashboard-cards" style="margin-bottom: 2rem;">
                        <div class="stat-card">
                            <div class="stat-icon bg-blue-light"><i class="fa-solid fa-file-signature text-blue"></i>
                            </div>
                            <div class="stat-details">
                                <h3>Phiếu chờ duyệt</h3>
                                <p class="stat-number">12</p>
                            </div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-icon bg-red-light"><i class="fa-solid fa-triangle-exclamation text-red"></i></div>
                            <div class="stat-details">
                                <h3>Sản phẩm hết hàng</h3>
                                <p class="stat-number">34</p>
                            </div>
                        </div>
                    </div>
                    <div class="card">'''

content = content.replace('                    </div>\n                    <div class="card">', cards_html)

with open(adj_file, 'w', encoding='utf-8') as f:
    f.write(content)

# 2. Remove nav-group
nav_pattern = re.compile(r'\s*<div class="nav-group">\s*<h3 class="nav-title">TỔNG QUAN</h3>\s*<a href="dashboard\.html" class="nav-item.*?\s*<i class="fa-solid fa-chart-pie"></i>\s*<span>Dashboard</span>\s*</a>\s*</div>', re.DOTALL)

for fname in html_files:
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8') as f:
            c = f.read()
        
        c = re.sub(nav_pattern, '', c)
        
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(c)

# 3. Delete dashboard.html
if os.path.exists('dashboard.html'):
    os.remove('dashboard.html')

print('DONE')
