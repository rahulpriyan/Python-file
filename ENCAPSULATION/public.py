class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
stu=student("rahul",20)
print(stu.name)
print(stu.marks)
stu.name="rahul"
print(stu.name)