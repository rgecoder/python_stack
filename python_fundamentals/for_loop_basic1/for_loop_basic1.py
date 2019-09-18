#1 basic - print int 0 - 150
for count in range(0,151):
  print(count)

#2 multiples of 5, print all multiples of 5 from 5 to 1000000
# for count in range (5,1000001):
#   if (count % 5 == 0):
#     print(count)

#3 counting the dojo way - print 1 to 100, if divisible by 5 print coding, if by 10 also print dojo
for count in range (1,101):
  if (count % 5 == 0 and count % 10 == 0):
    print("Coding Dojo")
  
  elif (count % 5 ==0):
    print("Coding")

#4 add odd int from 0 to 500000, print final sum
x=500000
sum=0
while x>0:
  if(x%2 == 1):
    sum = sum + x
  x = x-1
print(sum)

#5 print positive numbers starting @ 2018, count down by 4s, exlude 0
y = 2018
while y>0:
  print (y)
  y = y-4

#6 flexible countdown
def flexible_countdown(lowNum,highNum,mult):
  for count in range (lowNum,highNum+1):
    if count % mult == 0:
      print(count)
    count = count - 1

flexible_countdown(1,100,5)

list = [3,5,1,2]
for i in list:
    print(i)

# list = [3,5,1,2]
# for i in range(list):
#   print(i)
# does not work

list = [3,5,1,2]
for i in range(len(list)):
    print(i)
