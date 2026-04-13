import re
t="hello world welcome to python "
result=re.findall(r"[hello]",t)
print(result)