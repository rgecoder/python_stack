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

cat = Animal('Cat', 30)
cat.walk().run().display_health()

class Dog(Animal):
  def __init__(self,name):
    super(Dog, self).__init__(name,150)
    

dog = Dog("dog")
dog.display_health()
