stack=[10,20,30,40,50,60,70,80,90]
if len(stack)==0:
    print("stack underflow")
else:
    removal=stack.pop()
    print("popped element:",removal)
print("stack after pop:",stack)