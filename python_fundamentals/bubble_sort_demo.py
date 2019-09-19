arr = [1,5,3,2,0,8]

def bubbleSort(arr):
  count = 0
  for j in range(0,len(arr)-1):
    print("\n\n", "-"*50, "iteration",j)
    for i in range(0,len(arr)-1-j):
      print("\n","*"*80,"\nindex ", i, "value",arr[i])
    

      print("comparing", arr[i], arr[i+1])

      count += 1
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        print("swapped", arr[i], arr[i+1])
        print("array is now", arr)
      else:
        print("no need to swap", arr[i],arr[i+1])
  print("# of evaluations", count)

  return arr

bubbleSort(arr)