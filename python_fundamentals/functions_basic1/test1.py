# return random int 50-500

def randInt(min=50):
  import random
  x = random.random()*450 + 50
  return int(x)

print(randInt())
