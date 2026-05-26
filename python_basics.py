# Python basics :
# reference video: https://www.youtube.com/watch?v=8KCuHHeC_M0&t=141s

# variables and data types: 4 data types: int, float, str, bool
age = 5 # int
gpa = 3.14 # float
name = "Mimi" # str
is_student = True # bool
print(f"Hello {name}")

print(f"You are {age} years old")
print(f"Your gpa is {gpa}")
print(f"Are you a student?: {is_student}")

# arithmetic operators: +, -, *, /( division, return a float), //( integer division, reutrn an integer), % (modulo, remainder), ** (exponentiation)
print(5 + 3) # going to add 5 and 3
print(5 - 3) # going to subtract 3 from 5
print(5 * 3) # going to multiply 5 and 3
print(5 / 3) # going to divide 5 by 3, return a
print(5 // 3) # going to divide 5 by 3, return an integer
print(5 % 3) # going to return the remainder of 5 divided by
print(5 ** 3) # going to raise 5 to the power of 3


# typecasting: int(), float(), str(), bool(): used to convert a value from one data type to another.


print(type(age)) # going to return the data type of age, return <class 'int'>
print(type(gpa)) # going to return the data type of gpa, return <class 'float'>
print(type(name)) # going to return the data type of name, return <class 'str'>
print(type(is_student)) # going to return the data type of is_student, return <class 'bool'>
gpa = int(gpa) # going to convert gpa to an integer, return 3
print(gpa)
age = float(age) # going to convert age to a float, return 5.0
print(type(age)) # going to return the data type of age, return <class 'float'>
age = str(age) # going to convert age to a string, return '5.0'
print(type(age)) # going to return the data type of age, return <class 'str'>
name = bool(name) # going to convert name to a boolean, return True
print(name) # going to print the value of name, return True


# user input: input(): used to get input from the user, return a string.

name = input( "Enter your name: ") # going to prompt the user to enter their name, return a string and assign it to the variable name
print(f"Hello {name}")

# if statements: used to make decisions in the code, if condition is true, the code block will be executed, if condition is false, the code block will be skipped.
# order of if statements: if, elif, else matters, if the first condition is true, the code block will be executed and the rest of the conditions will be skipped, if the first condition is false, the next condition will be checked, and so on until a condition is true or all conditions are false.


if age >= 18:
    print("You are an adult")
elif age < 0: # can add a lot elif statements to check for different conditions
    print("You are not born yet")
elif age == 0:
    print("You are a newborn")
else:
    print("You are a minor")

has_ticket = True
if has_ticket:
    print("You can enter the concert")
else:
    print("You cannot enter the concert")

# while loops: used to repeat a block of code while a condition is true, the code block will be executed as long as
#  the condition is true, if the condition is false, the code block will be skipped and the loop will end. 

name = input("Enter your name: ")
while name == "":
    print("Name cannot be empty")
    name = input("Enter your name: ")
print(f"Hello {name}")

age = int(input("Enter your age: "))
while age < 0:
    print("Age cannot be negative")
    age = int(input("Enter your age: "))
print(f"You are {age} years old")

# for loops: used to repeat a block of code a certain number of times, the code block will be executed for
# each item in a sequence (list, tuple, string, etc.) or for a range of numbers.

for i in range(10): # going to repeat the code block 10 times, i will take the values from 0 to 9
    print(i) # going to print the value of i, return 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

for i in range(2, 11): # going to repeat the code block 10 times, i will take the values from 2 to 10
    print(i) # going to print the value of i, return 2, 3, 4, 5, 6, 7, 8, 9, 10 

name = " Madina Alizada"
for letter in name: # going to repeat the code block for each letter in the string name, letter will take the values of each letter in the string name
    print(letter) # going to print the value of letter, return ' ', 'M', 'a', 'd', 'i', 'n', 'a', ' ', 'A', 'l', 'i', 'z', 'a', 'd', 'a'

for letter in name:
    print(letter, end = "-") # going to print the value of letter, return ' ', 'M', 'a', 'd', 'i', 'n', 'a', ' ', 'A', 'l', 'i', 'z', 'a', 'd', 'a' with a hyphen between each letter

# Lists []: used to store multiple values in a single variable, lists are ordered, changeable, and allow duplicate values, lists are defined using square brackets [] and the values are separated by commas.

# tuple () is similar to a list, but it is immutable, meaning that the values cannot be changed after they are created, tuples are defined using parentheses () and the values are separated by commas.

# set {} is similar to a list and tuple, but it is unordered and does not allow duplicate values, sets are defined using curly braces {} and the values are separated by commas.


fruits = ["apple", "banana", "orange"] # going to create a list of fruits and assign it to the variable fruits

print(fruits[0]) # going to print the first element of the list fruits, return 'apple'

fruits[1] = "grape" # going to change the second element of the list fruits to 'grape'
print(fruits) # going to print the list fruits, return ['apple', 'grape', 'orange']

fruits.append("kiwi") # going to add 'kiwi' to the end of the list fruits
print(fruits) # going to print the list fruits, return ['apple', 'grape', 'orange', 'kiwi']
fruits.remove("grape") # going to remove 'grape' from the list fruits
print(fruits) # going to print the list fruits, return ['apple', 'orange', 'kiwi']
fruits.pop(0) # going to remove the first element of the list fruits, return 'apple'








