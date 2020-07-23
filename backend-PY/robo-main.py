class Employee:
    bonous = 10000
    no_of_employees = 0
    raise_amount = 1.04
    
    def __init__(self,first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name + '.' + last_name + '@gmail.com'
        
        Employee.no_of_employees +=1
    
    def fullname(self):
        return '{} {}'.format(self.first_name,self.last_name)
    
    def apply_bonous(self):
        self.bonous = int(self.bonous + self.salary)
    
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)
    
    # @classmethod
    # def from_string(cls, emp_str):
    #     first_name, last_name, salary = emp_str.split(' ')
    #     return cls(first_name, last_name, salary)

class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first_name, last_name, salary, prog_lang):
        super().__init__(first_name, last_name, salary)
        self.prog_lang = prog_lang

emp1 = Developer('vinay', 'kumar', 50000, 'Python')
emp2 = Developer('vvv', 'kkkk', 60000, 'HTML')

print(emp1.email)
print(emp2.email)