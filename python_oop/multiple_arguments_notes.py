#what if we do a function to accept variable amount of arguments?
#what does the splat operator do?

# * is called SPLAT operator

def varargs(arg1, *args):
  print("Got " + arg1 + " and " + ", ".join(args))

varargs("one")
#Got one and 

varargs("one", "two")
#Got one and two

varargs("one", "two", "three")
#Got one and two, three

varargs("one", "two", "three", "four")
#Got one and two, three, four



#**************#
def varargs2(arg1,*args):
  print("args is of " + str(type(args)))
varargs2("one", "two", "three") 
# output:args is of <class 'tuple'>

#.join() method in first code snip is called on a string that glues the values of tuple together
# i.e. the tuple of arg ('two','three') was joined as 'two,three' when we called ", ".join(args)



def list(*food):
  print (food)

list('apples')
# ('apples',) prints out as tuples

list('apples', 'peaches', 'beef')
# ('apples', 'peaches', 'beef')

def profile(name, *ages):
  print (name)
  print (ages)

profile('Roy', 21,34,'hello', 'age', [1,2,3])
# Roy
# (21, 34, 'hello', 'age', [1, 2, 3])




