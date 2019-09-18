def add(a,b):
  x = a+b
  return x
result = add(3,5)
print(result)

def say_hi(name):
  print ("Hi, " + name)

say_hi("roy")

#define parameters
# PASS IN arguments

# ** A functional call is equal to whatever the function returns
def say_hi2(name):
  return "Hi, " + name
greeting = say_hi("Michael")
print(greeting)

def add2(a,b):
  x = a+b
  return x
sum1 = add2(4,6)
sum2 = add2(1,4)
sum3 = sum1+sum2

print (sum1,sum2,sum3)