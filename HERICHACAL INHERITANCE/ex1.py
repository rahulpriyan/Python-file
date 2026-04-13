class person:
    def greet(self):
        print("hello from person")
class student(person):
    def study(self):
        print("student is studying")
class employee(person):
    def work(self):
        print("employee is working")
s=student()
c=employee()
s.greet()
s.study()
c.greet()
c.work()