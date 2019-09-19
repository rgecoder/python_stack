first_name = 'Corey'
last_name = 'Schafer'

sentence = 'My name is {} {}'.format(first_name,last_name)
print(sentence)

sentence2 = f'My name is {first_name} {last_name}'
print(sentence2)

sentence2=f"My name is {first_name.upper()} {last_name.upper()}"
print(sentence2)

person = {'name':'Jenn', 'age':23}

sentence = 'My name is {} and I am {} years old'.format(person['name'], person['age'])
print(sentence)

sentence = f'My name is {person["name"]} and I am {person["age"]} years old'
print(sentence)

calculation = f'4 times 11 is euqal to {4*11}'
print (calculation)

for n in range (1,11):
  sentence = f'the value is {n:03}' #zero padding 3 digits
  print(sentence)

pi = 3.14159265

sentence = f'pi is equal to {pi:.4f}' # 4 digits f floating point value
print(sentence)

from datetime import datetime
birthday = datetime(1990,1,1)

sentence =f'Jenn has a birthday on {birthday:%B %d, %Y}'
print(sentence)
#Jenn has a birthday on January 01, 1990

# **********************
print ("*"*80)
def beCheerful(name="", repeat=1):
  print(f"good morning {name}\n"*repeat)
beCheerful()

beCheerful(name="John")
beCheerful(name="michael", repeat=5)
beCheerful(repeat=5, name="kb")
beCheerful(name="aa")

import random
print(random.random()) #returns random floating num between 0.000 to 1.000
print(random.random()*50) #floating point between 0.000 to 50.000
int(3.654)   # returns 3
round(3.654) # returns 4

#return 0 - 100
def randInt ():
  import random
  x = random.random()*100
  return int(x)

print(randInt())

#return random int between 0 to 50
def randInt(max=50):
  import random
  x = random.random()*50
  return int(x)

print(randInt())

# return random int 50-100

def randInt(min=50):
  import random
  x = 100 - random.random()*50
  return int(x)

print(randInt())

# return random int 50-500

def randInt(min=50):
  import random
  x = random.random()*450 + 50
  return int(x)

print(randInt())






