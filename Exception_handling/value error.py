try:
    name=int(input("enter a number:"))
    print("you entered:", name)
except ValueError:
    print("error:index out of range")
