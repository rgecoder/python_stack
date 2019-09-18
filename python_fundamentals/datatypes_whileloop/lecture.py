for count in range(0,5):
  print("looping -", count)

count = 0
while count <5:
  print("looking -", count)
  count+=1



for val in "string":
  if val == "i":
    continue
  print(val)

x=3
y=x
while y>0:
  print(y)
  y=y-1
else :
  print("Final Else Statement")

name = "Joe Blue"
age = 35
weight = 160.57
dead = False
ninjas = ['Rozen','KB','Oliver']
new_person = {"name":"John","age":35, "dead":False} # store dictionaries
my_list = ['4',['list','in'],987]
empty_list = []
print(ninjas[0])
print(len(ninjas))
ninjas.append("Michael")
ninjas.pop() #pops the last value in the list
ninjas.pop(1) # pops index 1 off the list

if age>=18:
  print('Your age is above 18.')
elif age ==17:
  print('You are seventeen')
else:
  print('you are so young!')
for count in range(0,5):
  print('looping-', count)
for element in ninjas:
  print(element) #looping through an array

#define a function that returns the sum of two numbers
def sum(a,b):
  print("a:",a,"b:",b)
  return a+b
print(sum(3,5))

print(sum(2,4)+sum(1,5))

def say_hello(name=""):
  if name:
    print('Hello, ' + name +', from inside the function')
  else:
    print('no name')
#now we are unindented and have ended the previous block
print('Outside of the function')