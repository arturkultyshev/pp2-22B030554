import re

pattern = r'[A-Z][^A-Z]*'
text = 'ArturSashaArtem'

result = re.findall(pattern, text)
print(result)
