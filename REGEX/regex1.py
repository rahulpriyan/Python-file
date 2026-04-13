import re
text="i live in thiruvallur"
pattern="thiruvallur"
result=re.search(pattern,text)
if result:
    print("match found")
else:
    ("match not found")