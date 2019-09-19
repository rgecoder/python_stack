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