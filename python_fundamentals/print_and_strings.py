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
print(x.title()) #built in method to capitalize

# The following is a list of commonly used string methods:
# string.upper(): returns a copy of the string with all the characters in uppercase.
# string.lower(): returns a copy of the string with all the characters in lowercase.
# string.count(substring): returns number of occurrences of substring in string.
# string.split(char): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
# string.find(substring): returns the index of the start of the first occurrence of substring within string.
# string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
# string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
# string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.


