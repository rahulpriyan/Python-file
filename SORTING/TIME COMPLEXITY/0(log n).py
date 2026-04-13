def logarithmic_time(n):
    print("\nO(log n)-logarithmic time example")
    while n>1:
        print(n)
        n=n//2
n=int(input("enter value of n:"))
logarithmic_time(n)