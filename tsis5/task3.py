import re

pattern = r'[a-z]+_[a-z]+'
text = 'my_name_is_Artur'

result = re.findall(pattern, text)
print(result)