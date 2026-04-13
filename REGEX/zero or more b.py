import re
t="ac abc abbc"
r=re.findall("ab*c",t)
print(r)