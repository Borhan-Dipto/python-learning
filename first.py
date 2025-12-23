print("hello, bangladesh!")

# What is python?
#Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.


"""

Python Keywords
Python has a set of keywords that are reserved words that cannot be used as variable names, function names, or any other identifiers:

Keyword	Description
and	A logical operator
as	To create an alias
assert	For debugging
async	Define an asynchronous function
await	Wait for and get a result from an awaitable
break	To break out of a loop
case	Pattern in a match statement
class	To define a class
continue	To continue to the next iteration of a loop
def	To define a function
del	To delete an object
elif	Used in conditional statements, same as else if
else	Used in conditional statements
except	Used with exceptions, what to do when an exception occurs
False	Boolean value, result of comparison operations
finally	Used with exceptions, a block of code that will be executed no matter if there is an exception or not
for	To create a for loop
from	To import specific parts of a module
global	To declare a global variable
if	To make a conditional statement
import	To import a module
in	To check if a value is present in a list, tuple, etc.
is	To test if two variables are equal
lambda	To create an anonymous function
match	Start a match statement (compare a value against cases)
None	Represents a null value
nonlocal	To declare a non-local variable
not	A logical operator
or	A logical operator
pass	A null statement, a statement that will do nothing
raise	To raise an exception
return	To exit a function and return a value
True	Boolean value, result of comparison operations
try	To make a try...except statement
while	To create a while loop
with	Used to simplify exception handling
yield	To return a list of values from a generator









It is used for:

web development (server-side),
software development,
mathematics,
system scripting.

What can Python do?
Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.

Why Python?
Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
Python has a simple syntax similar to the English language.
Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
Python can be treated in a procedural way, an object-oriented way or a functional way.
"""

import sys

print(sys.version)

"""
Python Indentation
Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.

Example
if 5 > 2:
  print("Five is greater than two!")

"""


if 1000 > 200:
    print("1000 is bigger")







"""


if 5 > 2:
print("Five is greater than two!") #error

if 5 > 2:
        print("Five is greater than two!") #correct

"""
"""

Python Variables
In Python, variables are created when you assign a value to it:

Example
Variables in Python:

x = 5
y = "Hello, World!"


"""


x = 5
y = "Hello, World!"

print(x,y)

"""
Statements
A computer program is a list of "instructions" to be "executed" by a computer.

In a programming language, these programming instructions are called statements.

The following statement prints the text "Python is fun!" to the screen:

Example
print("Python is fun!")
In Python, a statement usually ends when the line ends. 
You do not need to use a semicolon (;) like in many other 
programming languages (for example, Java or C).


Many Statements
Most Python programs contain many statements.

The statements are executed one by one, in the same order as they are written:

Example
print("Hello World!")
print("Have a good day.")
print("Learning Python is fun!")



Semicolons (Optional, Rarely Used)
Semicolons are optional in Python. You can write multiple statements on one line by separating them with ; but this is rarely used because it makes it hard to read:

Example
print("Hello"); print("How are you?"); print("Bye bye!")
However, if you put two statements on the same line without a separator (newline or ;), Python will give an error:

Example
print("Python is fun!") print("Really!")
Result:

SyntaxError: invalid syntax



Double Quotes
Text in Python must be inside quotes. You can use either " double quotes or ' single quotes:

Example
print("This will work!")
print('This will also work!')


If you forget to put the text inside quotes, Python will give an error:

Example
print(This will cause an error)
Result:

SyntaxError: invalid syntax.




Print Without a New Line
By default, the print() function ends with a new line.

If you want to print multiple words on the same line, you can use the end parameter:

Example
print("Hello World!", end=" ")
print("I will print on the same line.")

print("hello", end=" ")
print('max')


Print Numbers
You can also use the print() function to display numbers:

However, unlike text, we don't put numbers inside double quotes:

Example
print(3)
print(358)
print(50000)

You can also do math inside the print() function:

Example
print(3 + 3)
print(2 * 5)



Mix Text and Numbers
You can combine text and numbers in one output by separating them with a comma:

Example
print("I am", 35, "years old.")

print("jalal is", 35, "years old")



Variables
Variables are containers for storing data values.

Creating Variables
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

Example
x = 5
y = "John"
print(x)
print(y)


x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = 4       # x is of type int
y = "Sally" # y is now of type str
print(x,y)




Casting
If you want to specify the data type of a variable, this can be done with casting.

Example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0




Get the Type
You can get the data type of a variable with the type() function.

Example
x = 5
y = "John"
print(type(x))
print(type(y))

x=1
z="Max"
print(type(z))


Case-Sensitive
Variable names are case-sensitive.

Example
This will create two variables:

a = 4
A = "Sally"
#A will not overwrite a



Python - Variable Names
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
Example
Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


Python Variables - Assign Multiple Values

"""





