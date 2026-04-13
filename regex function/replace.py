import re
text="my number is 6382651626"
result=re.sub(r"\d","[6382651629]",text)
print(result)