print("this is a sample string")

name = "roy"
print("My name is", name)

print("My name is " + name)
# cannot concat string with int 

#string interpolation
# f strings
# older method uses .format()
first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))

# % formating
hw = "Hello %s" % "world"
py = "I love python %d" % 3
print (hw,py)

name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name,age))
# %d placeholder for a number

# build-in string methods
x = "hello world"
print(x.title())


