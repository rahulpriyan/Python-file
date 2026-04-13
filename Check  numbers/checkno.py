def natural_numbers(n):
    print("natural numbers series:")
    for i in range(1, n+1):
        print(i, end=" ")
    print()
def even_numbers(n):
    print("even numbers series:")
    for i in range(2, n+1,2 ):
        print(i, end=" ")
    print()
def odd_numbers(n):
    print("odd numbers series:")
    for i in range(1,n+1,2):
        print(i,end=" ")
    print()
def fibonaci_series(n):
    print("fibonnaci_series:")
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
print()
natural_numbers(10)
even_numbers(2)
odd_numbers(7)
fibonaci_series(10)