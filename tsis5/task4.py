import re

pattern = r'[A-Z][a-z]+'
text = 'my_name_is_Artur'

result = re.findall(pattern, text)
print(result)
