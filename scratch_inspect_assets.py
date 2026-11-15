import re

with open(r'c:\Users\TEJASWINI\Codes web\cat-assets.js', 'r', encoding='utf-8') as f:
    text = f.read()

print('Length of cat-assets.js:', len(text))
matches = re.findall(r'"([a-zA-Z0-9_\-]+)":\s*"data:([^;]+);base64,([^"]+)"', text)
for m in matches:
    print(m[0], m[1], len(m[2]))
