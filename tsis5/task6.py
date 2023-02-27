import re

pattern = r'[,. ]'
repl = r':'
text = 'a,sds.d b'

result = re.sub(pattern, repl, text)
print(result)
