import threading
def greet(name):
    print("hello",name)
t1=threading.Thread(target=greet,args=("lilly",))
t1.start()
t1.join()
print("program finished")