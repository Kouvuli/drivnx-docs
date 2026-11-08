# Renders a docs Markdown file to print-ready HTML for Chromium, e.g.
#   python3 build_pdf.py DrivnX_Phase1_Development_Direction.md p.html
#   chromium --headless --no-pdf-header-footer --print-to-pdf=DrivnX_Phase1_Development_Direction.pdf "file://$PWD/p.html" && rm p.html
import re, markdown, pathlib, sys
src=pathlib.Path(sys.argv[1]); out=pathlib.Path(sys.argv[2])
md=src.read_text(encoding='utf-8').replace('<details>','<details open markdown="1">')
def gh_slug(value, separator):   # GitHub-style anchors, so the Markdown's #links keep working
    return re.sub(r'[^\w\- ]','',value.strip().lower()).replace(' ','-')
body=markdown.markdown(md,extensions=['tables','fenced_code','md_in_html','toc'],
                       extension_configs={'toc':{'slugify':gh_slug}})
css='''
@page{size:A4;margin:16mm 15mm}
body{font-family:Lato,"DejaVu Sans",sans-serif;font-size:10pt;line-height:1.45;color:#1b2333}
h1{font-size:20pt;margin:0 0 4pt} h2{font-size:14pt;margin-top:18pt;border-bottom:1px solid #ccd;padding-bottom:3pt}
h3{font-size:11.5pt;margin-top:14pt} h2,h3{break-after:avoid} table{break-before:avoid}
table{border-collapse:collapse;width:100%;margin:6pt 0 10pt;font-size:9pt}
th,td{border:1px solid #c9cfdb;padding:3pt 5pt;vertical-align:top;text-align:left} th{background:#eef1f7}
tr,img,pre,blockquote{break-inside:avoid}
blockquote{margin:8pt 0;padding:4pt 10pt;border-left:3pt solid #4a6cf7;background:#f3f5fb}
code{font-family:"DejaVu Sans Mono",monospace;font-size:8.5pt;background:#f1f3f7;padding:0 2pt}
pre{background:#f1f3f7;padding:6pt;white-space:pre-wrap}
img{max-width:100%} details summary{font-weight:bold;margin:4pt 0} a{color:#2846c9;text-decoration:none}
hr{display:none}
'''
title=re.search(r'^# (.+)$',md,re.M).group(1)
out.write_text(f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title><style>{css}</style></head><body>{body}</body></html>',encoding='utf-8')
