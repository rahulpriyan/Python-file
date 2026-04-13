try:
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    print("result:",a/b)
except ZeroDivisionError:
    print("Error: cannot divide by zero")