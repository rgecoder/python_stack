class Bike:
  def __init__(self,price,max_speed):
    self.price = price
    self.max_speed=max_speed
    self.miles = 0
  
  def displayinfo(self):
    print(f"Bike price: {self.price} Max Speed: {self.max_speed} Total Miles: {self.miles}")
    #OR -> print self.price, self.max_speed, self.miles
    return self

  def ride(self):
    print("Riding")
    self.miles += 10
    return self

  def reverse(self):
    print("Reversing")
    
    self.miles -= 10
    if self.miles < 0:
      self.miles = 0
    return self
  
bike1 = Bike(10,100)
print (bike1.price, bike1.max_speed)

bike1.ride().ride().ride().displayinfo()

bike2 = Bike(10,100)
bike2.reverse().reverse().displayinfo()