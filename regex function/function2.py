import re
text ="i have 20 apple and 45 oranges"
result=re.findall(r"[have]",text)
print(result)