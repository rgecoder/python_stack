class Car:
  def __init__(self, price, speed, fuel, mileage):
    self.price = price
    if self.price >= 10000:
      self.tax = 0.15
    else:
      self.tax = 0.12
    self.speed = speed
    self.fuel = fuel
    self.mileage = mileage
    self.display_all() ##call this method once attributes are defined

  
  def display_all(self):
    print (self.price, self.speed, self.fuel, self.mileage, self.tax)
    return self

car1 = Car(10000,25,"full", "15mpg")
  
  
