class Parent:
  def method_a(self):
    print("invoking PARENT method_a!")
class Child(Parent):
  def method_a(self):
    print("invoking CHILD method_a!")
  
dad = Parent()
son = Child()
dad.method_a()
son.method_a()

#Child overrides this method from the parent by defining its own version

#POLYMORPHISM

#we'll use the Person class to demonstrate polymorphism
#in which multiple classes inherit from the same class but behave in different ways
class Person:
  def pay_bill(self):
    raise NotImplementedError

# Millionaire inherits from Person
class Millionaire(Person):
  def pay_bill(self):
    print("Here you go! Keep the change!")
# Grad student also inherits from the Person class
class GradStudent(Person):
  def pay_bill(self):
    print("Can I owe you ten dollars or do dishes?")


guy1 = Millionaire()
guy2 = GradStudent()
guy1.pay_bill()
guy2.pay_bill()



