class Employee:
    bonous = 10000
    no_of_employees = 0
    
    def __init__(self,first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name + '.' + last_name + '@email.com'
        
        Employee.no_of_employees +=1
    
    def fullname(self):
        return '{} {}'.format(self.first_name,self.last_name)
    
    def apply_bonous(self):
        self.bonous = int(self.bonous + self.salary)
        
    @classmethod
    def raise_amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first_name, last_name, salary = emp_str.split(' ')
        return cls(first_name, last_name, salary)
        
employee_list = []
for _ in range(int(input())):
    employee_details = input()
    emp_str = Employee.from_string(employee_details)
    employee_list.append(f'{(emp_str.no_of_employees)}. {(Employee.fullname(emp_str)).ljust(50)} \t {str(emp_str.email).center(20)} \t {(emp_str.salary).ljust(20)}')
  
for i in employee_list:
    print(i)

"""   
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
import datetime
my_date = datetime.datetime.now()

print(Employee.is_workday(my_date))
"""      
