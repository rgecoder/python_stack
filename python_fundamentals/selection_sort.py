#part 1 this will not work for duplicate numbers 

list1 = [1,5,3,2,2,0,8]

def selection_sort_1(arr):
  for i in range(len(list1)):
    min_val = min(list1[i:])
    min_ind = list1.index(min_val)
    list1[i],list1[min_ind]=list1[min_ind],list1[i]

    print(list1)

print(selection_sort_1(list1))

#part 2 works for duplicate numbers

list2 = [56,0,2,2,6,0]



