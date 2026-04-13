class person:
    def name_person(self):
        print("name:rahul")

class employee(person):
    def salary_employee(self):
        print("salary:80000")
class manager(employee):
    def department_manager(self):
        print("department:biomedical")
c=manager()
c.name_person()
c.salary_employee()
c.department_manager()