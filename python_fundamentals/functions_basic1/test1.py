# this length, that value - function accepts 2 parameters (size,value), take 2 num return list of length size containing only num in value
# i.e. function(4,7) should return [7,7,7,7]

def lengthAndValue(size,value):
  myarr=[]
  for i in range (0,size):
    myarr.append(value)

  return myarr

x = lengthAndValue(4,7)
print(x)
    