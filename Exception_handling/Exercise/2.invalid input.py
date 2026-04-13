try:
    num=int(input("enter your number"))
    print("you entered correct num",num)
except ValueError:
    print("invalid input error")