# 1 biggie size - given array, write function change all positive numbers to "big"


def biggie(arr):
    for i in range(0, len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    return arr


x = biggie([-1, 3, 5, -5])

print(x)

# 2 count positives - give array of num, create function to replace last value of number of positive values
# i.e. [-1,1,1,1] -> [-1,1,1,3]


def count_positives(arr):
    positive_count = 0
    for i in range(0, len(arr)):
        if arr[i] > 0:
            positive_count += 1
    arr[len(arr) - 1] = positive_count

    return arr


x = [-1, 1, 1, 1]


y = count_positives(x)

print(y)


#3 Sum Total - function takes in array, returns sum of all values in array

def sum_total(arr):
  sum = 0
  for i in range(0,len(arr)):
    sum += arr[i]
  return sum

x = [1,2,3,4]

print(sum_total(x))


#4. average - array as argument, returns averages of all values

def average(arr):
  count=0
  sum=0.0
  for i in range (0,len(arr)):
    sum += arr[i]
    count += 1
  average = sum/count
  return average

x = [1,2,3,4]
print (average(x))


#5. length - create function takes array as argument, returns length of array

def length(arr):
  len_arr = len(arr)
  return len_arr

x = [1,3,1,9]

print (length(x))

#6. minimum - takes arr as argument and returns minimum value of arr, if arr empty return false 

def minimum_arr(arr):
  if len(arr) == 0:
    return False
  
  min_arr = arr[0]
  for i in range (0,len(arr)):
    if arr[i] < min_arr:
      min_arr = arr[i]
  
  return min_arr

x = [1,2,3,4]
y = [-1,-2,-3]
z = []

print (minimum_arr(z))

#7. max - takes arr as argument and returns max value of arr, if arr empty return false 

def maximum_arr(arr):
  if len(arr) == 0:
    return False
  
  max_arr = arr[0]
  for i in range (0,len(arr)):
    if arr[i] > max_arr:
      max_arr = arr[i]
  
  return max_arr

x = [1,2,3,4]
y = [-1,-2,-3]
z = []

print (maximum_arr(x))

#8. Ultimate Analyze - takes array as argument and returns dictionary that has sumTotal, average, minimum, maximum, and length of array

def ultimate_analyze(arr):
  my_dict={}
  sum=0.0
  count=0
  min=arr[0]
  max=arr[0]
  for i in range (0,len(arr)):
    sum +=arr[i]
    count += 1
    if min>arr[i]:
      min = arr[i]
    if max<arr[i]:
      max = arr[i]
  avg = sum/count
  my_dict={'sumTotal':sum,'average':avg,'minimum':min,'maximum':max, 'length of array':len(arr)}
  return my_dict

x = [1,2,3,4]

print(ultimate_analyze(x))


#8. reverse list - function takes in array, return array in reversed order. Do without creating empty temporary array *****

def reverse_list(arr):
  return list(reversed(arr))

x = [1,2,3,4]

print(reverse_list(x))

