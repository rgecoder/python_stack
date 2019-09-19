def square(num):
  x = num ** 2
  return x

print(square(2))

#rewrite function that takes in one parameter (num) squares it and then returns it

lambda num: num ** 2
#means: here is an anonymous (Nameless) function that takes one argument, called num, and returns num ** 2

lambda num1, num2: num1 + num2
#takes in 2 arguments and returns sum of the two arguments

#create a new list, with a lambda as an element
my_list = ['test_string', 99, lambda x: x ** 2]
#access the value in the list
print(my_list[2]) #will print a lambda object stored in memory
#invoke the lambda function, passing in 5 as the arguemtn
my_list[2](5)



#***********
#define a function that takes one input that is a function
def invoker(callback):
  #invoke the input pass the argument 2
  print(callback(2))
invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)

#************
#stored in a variable
add10 = lambda x: x+ 10
add10(2) # returns 12
add10(98) # returns 108

#*************
#returned by another function
def incrementor(num):
  start = num
  return lambda x: num + x

print(incrementor(5))

#**************
#lambdas and other functions
#create a list
my_arr=[1,2,3,4,5]
#define a function that squares values
def square(num):
  return num ** 2
#invoke map function
print(list(map(square,my_arr)))

#!!!! lambdas are useful when we only need a function once
# don't need to define a function and unnecessarily consume meory and complicate code

my_arr2 = [1,2,3,4,5]
print(list(map(lambda x: x ** 2, my_arr2)))


# map function
def map(list,function):
  for i in range (len(list)):
    list[i] = function(list[i])
  return list

print( map([1,2,3,4], (lambda num: num * num)))
print( map([1,2,3,4], (lambda num: num * 3)))
print( map([1,2,3,4], (lambda num: num % 2)))

