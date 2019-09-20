#python object-oriented programming

class Employee:
  def __init__(self, first, last, pay): # self, receive instance of self automatically
    self.first = first
    #could be self.fname does not need to match
    self.last = last
    self.pay = pay
    self.email = first + "." + last + "@company.com"
  
  def fullname(self): #each method in the class auto takes in instances as its first argument
    #method
    return '{} {}'.format(self.first, self.last)




emp_1 = Employee('Roy', 'Ge', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1)
print(emp_2)

# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'Corey.Schafer@company.com'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@Company.com'
# emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

# print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_1.fullname())

print(emp_2.fullname())

#These 2 do the same thing!
Employee.fullname(emp_1)
emp_2.fullname()

