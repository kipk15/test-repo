class Employee():
    # class variables
    num_of_employees = 0
    raise_amount = 1.05

    def __init__(self, fname, lname, department, pay):
        # instance variables
        self.fname = fname
        self.lname = lname
        self.department = department
        self.pay = pay
        
        Employee.num_of_employees += 1
    
    def pay_raise(self):
        self.pay = int (self.pay * self.raise_amount)

emp_1 = Employee('Joe', 'May', 'logistics', 5000)
emp_2 = Employee('Burn', 'Leu', 'security', 6000)
emp_1.pay_raise()
emp_2.raise_amount = 1.04
emp_2.pay_raise()
print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employee.num_of_employees)




