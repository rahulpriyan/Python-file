import re
text="aBC123"
print(re.findall(r"[a-z]",text))


import re
text="Abc123"
print(re.findall(r"[A-Z]",text))