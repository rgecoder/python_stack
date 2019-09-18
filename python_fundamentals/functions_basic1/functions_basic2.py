#1 countdown - function accept num input, return new list that counts down by 1, from the num (0th) to 0 (last element)
def countdown(num):
  mylist = []
  for i in range(0,num+1):
    mylist.append(i)
  #1 
  #list.reverse()
  # 
  # 
  # 2
  # reverse_list = list[::-1]
  # print(reverse_list)

  #3 iterators
  reversed(mylist)
  print(reversed(mylist))
  reversed_list=list(reversed(mylist))
  print(reversed_list)
countdown(5)

#2 print and return - receive list 2 numbers, print first value, return 2nd

def print_return(lst):
  # print(lst[0])
  return (lst[1])

mylist = [1,2]
print(print_return(mylist))

#3 first plus length - given list, return sum of first value in list, plus the list length

def first_plus_length(arr):
  sum = arr[0] + len(arr)
  return sum

myarr = [1,3,0,5]

print first_plus_length(myarr)

#4 values greater than second - function accept list, return new list with values greater than 2nd value, print how many values this is
# if list only 1 element print false

def values_greater_second(arr):
  count = 0
  arr2=[]
  for i in range(0,len(arr)):
    if len(arr) == 1:
      return False
    
    elif arr[i]>arr[1]:
      arr2.append(arr[i])
      count += 1

  return arr2, count

myarr = [1,6,7,8,11,2,21]

print(values_greater_second(myarr))

#5 this length, that value - function accepts 2 parameters (size,value), take 2 num return list of length size containing only num in value
# i.e. function(4,7) should return [7,7,7,7]

def lengthAndValue(size,value):
  myarr=[]
  for i in range (0,size):
    myarr.append(value)

  return myarr

x = lengthAndValue(4,7)
print(x)
    


