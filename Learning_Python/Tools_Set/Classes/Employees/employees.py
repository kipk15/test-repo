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
    def fullname(self):
        return(f"{self.fname.title()} {self.lname.title()}")

    def pay_raise(self):
        self.pay = int (self.pay * self.raise_amount)

    def __repr__(self):
        return(f"Employee({self.fname}, {self.lname}, {self.pay})")
    
    def __str__(self):
        return(f"Employee({self.fullname()}, {self.department})")

    # eg adding two employees gives their total salaries
    def __add__(self, other):
        return self.pay + other.pay

    # dunder method that displays # of characters in a fullname
    def __len__(self):
        return len(self.fullname())

    @classmethod # takes a class as an instance
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    
    # instance/class that will not be accessed 
    # anywhere in the function above
    @staticmethod 
    def is_workday(day):# assuming only weekdays are
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amount = 1.15

    def __init__(self, fname, lname, department, pay, prog_language):
        super().__init__(fname, lname, department, pay)
        self.prog_language = prog_language
        
class Manager(Employee):
    raise_amount = 1.20

    def __init__(self, fname, lname, department, pay, employees=None):
        super().__init__(fname, lname, department, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employees(self, emp):
        if emp not in self.employees:
            employees.append(emp)

    def remove_employees(self, emp):
        if emp in self.employees:
            employees.remove(emp)
    
    def show_employees(self):
        print(f"Employees under {self.fullname()} are:")
        for emp in self.employees:
            print(f"\t-{emp.fullname()}")
    

print(Employee.num_of_employees)
emp_1 = Employee('Joe', 'May', 'logistics', 5000)
emp_2 = Employee('Burn', 'Leu', 'security', 6000)
emp_1.pay_raise()
emp_2.raise_amount = 1.04 # gets assigned to the specific instance as an attribute
emp_2.pay_raise()

print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employee.num_of_employees)

import datetime # python's module
my_date = datetime.date(2010, 10, 20)

print(Employee.is_workday(my_date))

dev_1 = Developer('Devel', 'Oper1', 'Development', 7000, 'Python')
man_1 = Manager('Manner', 'Ger1', 'Management', 7500, [dev_1])
print(dev_1.__dict__)
print(man_1.__dict__)
dev_1.pay_raise()
man_1.pay_raise()
print(dev_1.__dict__)
print(man_1.__dict__)
man_1.show_employees()

print(repr(emp_1)) # or print(emp_1.__repr_())
print(str(emp_2))
print(emp_1 + emp_2)
print(len(emp_1))
print(emp_2.__len__())





