#Python OOP - classmethods and staticmethods
class Employee:

  num_of_emps = 0
  raise_amt = 1.04

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.email = first + '.' + last + '@email.com'
    self.pay = pay

    Employee.num_of_emps += 1

  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay + self.raise_amt)

  @classmethod #DECORATORS
  #working with our class instead of instance
  def set_raise_amt(cls,amount): #automatically pass cls
    cls.raise_amt = amount
  # can run class method from instances as well, still works, not used much

  @classmethod #ALTERNATIVE CONSTRUCTORS
  def from_string(cls,emp_str):
    first, last, pay = emp_str.split('-')
    cls(first,last,pay) # create a new employee
    return cls(first, last, pay) #so can receive new Employee object when returned

  @staticmethod #Don't access instance or the class
  def is_workday(day): #dont take in instance or the class as first arg
    if day.weekday() == 5 or day.weekday() == 6:
      return False
    return True
  

emp_str_1 = 'John-Doe-70000'

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first,last,pay)  

new_emp_1 = Employee.from_string(emp_str_1)

import datetime
my_date = datetime.date(2019, 9, 20)

print(Employee.is_workday(my_date))




emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','Employee', 60000)


emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'



Employee.set_raise_amt(1.05) #class method! NEW
# same as Employee.raise_amt = 1.05



print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

print(new_emp_1.email)
print(new_emp_1.pay)
