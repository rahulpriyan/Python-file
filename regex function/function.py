import re
text ="i have 20 apple and 45 oranges"
print(re.search(r"\d",text))
print(re.search(r"\w",text))
print(re.findall(r"\d",text))
print(re.findall(r"\w",text))
