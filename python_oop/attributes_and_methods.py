#declare a class and give it name User
class User:
  #the __init__ method is called every time a new object is created
  def __init__(self,name,email):
    #set some instane variables, just like any variable we can call these anything
    self.name = name
    self.email = email
    self.logged = false

  #method we create to help user login
  def login(self):
    self.logged = True
    print(self.name + " is logged in. ")
    return self

#now create an instance of a class
new_user = User("Anna","anna@anna.com")
print(new_user.email)