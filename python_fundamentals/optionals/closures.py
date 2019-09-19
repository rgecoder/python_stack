#Closures

def outer_func():
  message = "Hi"

  def inner_func():
    print(message) #"free variable" inside inner function
  
  return inner_func

my_func = outer_func()
print(my_func.__name__)

my_func() #this is the inner function
my_func() # this is a closure: inner function that remembers and has access to variables in the local scope in which it was created, even after outer function finished exec

#*************

def outer_func2(msg):
  message = msg

  def inner_func():
    print(msg)
  return inner_func

hi_func = outer_func2('Hi')
hello_func = outer_func2('Hello')

hi_func() # remembers the value of their own message variable
hello_func() # a closure closes over the free variables in their environment (in this -> message)


