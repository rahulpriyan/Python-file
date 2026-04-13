import threading
a=int(input("enter ur number"))
def task():
    print(a**2)
t1=threading.Thread(target=task)
t1.start()
print("program finished")