class Animal:
  def __init__(self, name, health):
    self.name = name
    self.health = health

  def walk(self):
    self.health -= 1
    return self
  
  def run(self):
    self.health -= 5
    return self

  def display_health(self):
    print(f'Name: {self.name} Health: {self.health}')
    return self



class Dog(Animal):
  def __init__(self,name):
    # super(Dog, self).__init__(name,150)
    super().__init__(name,150)
    
class Dragon(Animal):
  def __init__(self,name):
    super().__init__(name,170)

  def fly(self):
    self.health -= 10

  def display_health(self):
    super().display_health()
    print ("This is a dragon!")


class Zoo:
  def __init__(self,zoo_name):
    self.animals = []
    self.name = zoo_name
  def addDog(self,name):
    self.animals.append( Dog(name))
  
  def addDragon(self,name):
    self.animals.append( Dragon(name))
  
  def printAllHealth(self):
    print("-"*30, self.name, "-"*30)
    for animal in self.animals:
      animal.display_health()


zoo1= Zoo("John's Zoo")
zoo1.addDog("Tracy")
zoo1.addDog("Doggy")

zoo1.addDragon("Draggy")
zoo1.addDragon("Dragoon")
zoo1.printAllHealth()

