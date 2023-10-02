#Hello World

print ('Hello World')

# Syntax
if 5 > 2:
  print("Five is greater than two!")

# Syntax Error:
#
# if 5 > 2:
# print("Five is greater than two!")


# Variables
x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Casting
# If you want to specify the data type of a variable, this can be done with casting.
#
# Example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x,y,z)

#Get the type of varaible

print(type(z))

# Case Sensitive
average =10

total_students=20

def printMyName(name):
    print("Hello" +" "+ name)


printMyName('Ahmed')

#By Default Every command is on one line
x=1
z=3
y=5

#You can combine them by adding ; between them
x=9; z=10; y=9

#Naming Rules

# Identifiers should begin with Letters (A-Z)/ (a-z) or _
# Keywords are prohibited to use. (def, If, print,def,class, break,else .....)
# Case Sensitive (Average <> average)

#Example

avarage=10
Average=4

print("average equals "); print(average)
print("average equals "+ str(average))
print( "Average equales "); print(Average)

#########################################################

# True or False for Indentifer names:

# Ahmed =10
# ahmed = 9
# 1Ahmed
# _Ahmed
# @ahmed = 6
# 2myvar = "John"
# my-var = "John"
# my var = "John"

#####################################################################
# There are several techniques you can use to make them more readable:
#
# Camel Case
# Each word, except the first, starts with a capital letter:
#
# myVariableName = "John"
# Pascal Case
# Each word starts with a capital letter:
#
# MyVariableName = "John"
# Snake Case
# Each word is separated by an underscore character:
#
# my_variable_name = "John"

# Data Types:
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType