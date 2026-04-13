class bank:
    def __init__(self,acc_no,phone_no):
        self.acc_no=acc_no
        self.phone_no=phone_no

    def show_info(self):
        print(f"acc_no:{self.acc_no},phone_no:{self.phone}")
        
class bank(employee):
    def __init__(self,acc_no,phone_no):
        super().__init__(acc_no,phone_no)
        self.interest=interest
    def show_employee_info(self):
        print(f"name:{self.name},age:{self.age},salary:{self.salary}")
emp=employee("rahul",28,50000)
emp.show_info()
emp.show_employee_info()