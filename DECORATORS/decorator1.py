def decorator(func):
    def wrapper():
        print("before execution")
        func()
    def wrapper():
        print("after execution")
    return wrapper
def greet():
    print("Hello!")
# Manual decoration
greet = decorator(greet)
greet()