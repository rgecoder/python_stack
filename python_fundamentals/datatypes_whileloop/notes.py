#notes
#data types while loops

name = "Joe Blue"
age = 35
weight = 160.57
dead = False 
ninjas = ['Rozen','KB','Oliver']
new_person = {'name':'John', "age":35}
print(new_person)

my_list= ['4',['list','in','a','list'],987]

empty_list = []

print(ninjas[0])

ninjas.append('Michael')
print(ninjas)

ninjas.pop()
print(ninjas)

ninjas.pop(1)
print(ninjas)

if age >= 18:
  print('your age is above 18.')

elif age == 17:
  print('You are seventeen')

else:
  print('You are so young')

for count in range(0,5):
  print("looping - ", count)


for element in ninjas:
  print(element)

for element in new_person:
  print(new_person)

def sum(a,b):
  print("a:",a,"b:",b)
  return a+b

print (sum(2,3))

print (sum(3,2)+sum(5,6))



def say_hello(name=""):
  if name:
    print('hello, ' + name + ', from inside the function')
  else:
    print('no name')

print('Outside the function')

say_hello('Roy')

#while loops
for count in range(0,5):
  print("looping- ", count)

count = 0
while count<5:
  print("looping - ", count)
  count +=1

#loop control
for val in "string":
  if val == "i":
    break
  print(val)

#else
x=3
y=x
while y>0:
  print(y)
  y=y-1
else:
  print("final else statement")

x=3
y=x
while y>0:
  print(y)
  y=y-1
  if y==0:
    break
else:
  print("final else statement")

