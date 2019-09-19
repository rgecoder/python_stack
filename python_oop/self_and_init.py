# class User:
#   name = "anna"
# anna = User()
# print("anna's name:", anna.name)

# User.name = "Bob"
# print("anna's name after change: ", anna.name)

# bob = User()
# print("bob's name: ",bob.name)

class User:
  def __init__(self,name,email):
    self.name = name
    self.email = email
    self.logged = False

user1 = User("anna propas","anna@anna.com")
print(user1.name)
print(user1.logged)
print(user1.email)