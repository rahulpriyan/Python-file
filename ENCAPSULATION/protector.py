class employee:
    def __init__(self,name,salary):
        self._name=name
        self._salary=salary
emp=employee("rahulpriyan",10000)
print(emp._salary)
class manager(employee):
    def show_salary(self):
        print(f"salary:{self._salary}")
mgr=manager("rahulpriyan",10000)
mgr.show_salary()