x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]['last_name'] =  "Bryant"
print(students)

sports_directory['soccer'][0] = "Andres"
print (sports_directory)

z[0]['y'] = 30
print (z)

#2. function that given a dict, loops through each dict and prints key value pair
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def loop_one(arr):
  for i in range(0,len(arr)):
    for keys in arr[i].items():
      sentence = f'first_name - {arr[i]["first_name"]}, last_name - {arr[i]["last_name"]}'
    print(sentence) #extra indent makes this print twice?
  
loop_one(students)

#3

#4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printDojoinfo (obj):
  location_count=0
  instructor_count=0
  for k,v in obj.items():
    if k == 'locations':
      for i in range(0,len(v)):
        location_count += 1
      print(f'{location_count} Locations')
      print(v)
      
    elif k== 'instructors':
      for i in range(0,len(v)):
        instructor_count += 1
      print(f'{instructor_count} Instructors')
      print(v)
    
  
printDojoinfo(dojo)



 

