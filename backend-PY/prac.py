# class C: 

#     counter = 0
    
#     def __init__(self): 
#         self.counter += 1

#     def __del__(self):
#         self.counter -= 1

# if __name__ == "__main__":
#     x = C()
#     print("Number of instances: : " + str(C.counter))
#     y = C()
#     print("Number of instances: : " + str(C.counter))
#     del x
#     print("Number of instances: : " + str(C.counter))
#     del y
#     print("Number of instances: : " + str(C.counter))





















class Employee:
    
    gvk = '{} {}'.format('GANDHAM', 'VINAY')
    aki = 'AKI','CHANDU',70000


    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name + '.' + last_name + '@iBHubs.com'
    
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)
#gvk =Employee('GANDHAM','VINAY',70000)

n = input('Enter no of Employees do you what to know: ')
for _ in range(int(n)):
    employee_name = input('Enter employee name: ').split()
    print(Employee.gvk)

# print(emp1)
# print(emp2)
# print(emp1.email)
# print(emp2.email)
# print()



# #print(emp1.fullname())
# #print()
# #print(emp2.fullname())
# #print('{} {}'.format(emp1.first_name, emp1.last_name))

