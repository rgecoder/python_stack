class Vehicle:
  def __init__ (self, wheels, capacity, make, model):
    self.wheels = wheels
    self.capacity = capacity
    self.make = make
    self.model = model
    self.mileage = 0
  
  def drive(self, miles):
    self.mileage += miles
    return self
  
  def reverse(self,miles):
    self.mileage -= miles
    return self
  
# READ AS: make a class Bike/Car/Airplane that inherits Vehicle
# IMPLICIT INHERITANCE

# class Parent:
#   # parent methods and attributes here
# class Child(Parent): #inherits from Parent class so we define Parent as the first parameter
#   # parent methods and attributes are implicitly inherited
#   # child methods and attributes


class Bike(Vehicle):
  def vehicle_type(self):
    return "Bike"

class Car(Vehicle):
  def set_wheels(self):
    self.wheels = 4
    return self

class Airplane(Vehicle):
  def fly(self,miles):
    self.mileage += miles
    return self

v = Vehicle(4,8,"dodge", "minivan")
print(v.make)
v.drive(10).reverse(10)

# print(v.vehicle_type()) -- won't work with no attribute 'vehicle_type'

b = Bike(2,1,"Schwinn", "paramount")
print(b.vehicle_type())


c = Car(8,5,"Toyota", "Matrix")
c.set_wheels()
print(c.wheels)

a = Airplane(22,853,"airbus","A300")
a.fly(500)
print(a.mileage)

