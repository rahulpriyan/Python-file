import re
text="rahul priyan is a student"
result=re.findall("student$",text)
print(result)

import re
text="rahul priyan is a student"
result=re.findall("^rahul",text)
print(result)