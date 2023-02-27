import re

pattern = r'ab*'
text = 'abbbabbbabbbdsdsdsdsdsaaabbbadbababa'

result = re.findall(pattern, text)
print(result)
