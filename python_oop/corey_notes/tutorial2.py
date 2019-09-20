class Employee:
  raise_amount = 1.04 # class variable

  num_of_emps = 0

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + "." + last + "@company.com"

    Employee.num_of_emps += 1 #don't want total employees different for each instance
                              #so no self here
  
  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  
  def apply_raise(self):
    self.pay = int(self.pay * Employee.raise_amount) # or use self.raise_amount


print(Employee.num_of_emps) # 0

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps) # 2

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# emp_1.raise_amount
# Employee.raise_amount
#or if we want to update the 4%?

emp_1.raise_amount = 1.05 # this will now only change raise amount for emp_1
#created raise_amount attribute in emp_1

print(emp_1.raise_amount) #1.05
print(Employee.raise_amount) # 1.04
print(emp_2.raise_amount) # 1.04
#*** WHAT IS HAPPENING - first check if instance contain that attribute, THEN check if class it inherits from contains that attribute
# in this case accessing parent class attribute

print (emp_1.__dict__)
# {'first': 'Corey', 'last': 'Schafer', 'pay': 52000, 'email': 'Corey.Schafer@company.com'}

print(Employee.__dict__)
# {'__module__': '__main__', 'raise_amount': 1.04, '__init__': <function Employee.__init__ at 0x1073c8840>, 'fullname': <function Employee.fullname at 0x1073c87b8>, 'apply_raise': <function Employee.apply_raise at 0x1073c8730>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}

