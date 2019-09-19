arr = [1,5,3,2,0,8]

def bubbleSort(arr):
  for j in range(0,len(arr)-1):

    for i in range (0,len(arr)-1-j):
      if arr[i]>arr[i+1]:
        arr[i], arr[i+1]=arr[i+1], arr[i]
  return arr

print (bubbleSort(arr))