import threading
def task():
    print("thread 1 running")
t1=threading.Thread(target=task)
t1.start()
print("this is the main program")