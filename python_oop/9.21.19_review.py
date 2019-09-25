class User:
  def __init__(self,name,email):
    self.name = name
    self.email = email
    self.logged = True
  def login(self):
    self.logged = True
    print(self.name + ' is logged in.')
    return self
  def logout(self):
    self.logged = False
    print(self.name + ' is not logged in')
    return self

  def show(self):
    print(f"name is {self.name}, email at {self.email} ")
    return self

  
user1 = User('Roy', 'roy@gmail.com')
user1.show()