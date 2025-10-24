from classes.week00.second_class.utils import clear_screen
'''
# 1

Write down the steps a program would need to make a cup of tea. Then implement a Python 
function make_tea() that prints each step.
'''
steps=['step1','step2','step3']
def make_tea(myList):
    myList[2] = "step5"
    for item in myList:
        print(item)
    

make_tea(steps)
print(steps)

# enter your code here

'''Boil water
Place the tea bag in a cup
Pour hot water 
Remove the tea bag
Add sugar 
Stir'''

def make_tea():
    steps = [
        "Boil water",
        "Place the tea bag in a cup",
        "Pour hot water",
        "Remove the tea bag",
        "Add sugar",
        "Stir"
    ]
    for step in steps:
        print(step)

make_tea()
pause = input("pause")
clear_screen()

pause=input('pause')
clear_screen()
'''
#2

Given a list [2, 4, 6, 8, 10], write a program that prints the next three numbers in the list.  
(the ones after 10)
'''
# enter your code here
nums = [2, 4, 6, 8, 10]

def new_func(nums):
    return [nums[-1] + (i+1)*2 for i in range(3)]

print(new_func(nums))
 

pause=input('pause')
clear_screen()
'''
#3

Write a program that asks the user for their first and last name, then prints a greeting:
"Hello, <first name> <last name>!"
'''
# enter your code here
fname = input('please enter yur first name: ')
lname = input('please enter your last name: ')
fname = fname.capitalize()
lname = lname.capitalize()
print(f'Hello, {fname} {lname}')

# Ask for first and last name
first = input("Enter your first name: ")
last = input("Enter your last name: ")

# Print greeting
print(f"Hello dear {first} {last}!")

pause=input('pause')
clear_screen()
'''
#4

Write a program that prints your Python version and platform using the sys and platform modules.
'''
# enter your code here
import sys
import platform

print("Python version:", sys.version)
print("Platform:", platform.system(), platform.release())

pause=input('pause')
clear_screen()
'''
#5

Ask the user to input two numbers. Calculate and print their sum, difference, product, 
and division (both / and //).
'''
# enter your code here
txt = 'please enter an integer: '
while True:
    try:
        x = int(input(txt))
        break
    except ValueError:
        txt = 'follow directions, enter a number: '

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Perform calculations
print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
print(f"Division (/): {a / b}")
print(f"Floor Division (//): {a // b}")

''' Output:
Enter the first number: 3
Enter the second number: 5
Sum: 8
Difference: -2
Product: 15
Division (/): 0.6
Floor Division (//): 0
'''
pause=input('pause')
clear_screen()
'''
#6

Ask the user to input a sentence. Print it in uppercase, lowercase, with the first letter 
capitalized, and split it into words.
'''
txt = input('please entr some text:')
print(txt.upper())
print(txt.lower())
print(txt.capitalize())
print(txt.split())

# enter your code here

sentence = input("Enter a sentence: ")

print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Capitalized:", sentence.capitalize())
print("Split into words:", sentence.split())
pause=input('pause')
clear_screen()

'''Output:
Enter a sentence: i love mars
Uppercase: I LOVE MARS
Lowercase: i love mars
Capitalized: I love mars
Split into words: ['i', 'love', 'mars']
'''
#7Calculate the result of the following without parentheses and then with parentheses:
10 + 2 * 5 / 2 - 3 ** 2

# enter your code here
print(10 + 2 * 5 / 2 - 3 ** 2)

# Without parentheses
print(10 + 2 * 5 / 2 - 3 ** 2)   # 6.0

# With parentheses
print(((10 + 2) * 5) / 2 - (3 ** 2))   # 21.0

print(x)

x = 2**3**2
print(x)
pause=input('pause')
clear_screen()
'''
#8

Create a list of your three favorite foods. Replace the second item with a new one, 
then print the list.
'''
# enter your code here
# Create a list of three favorite foods
foods = ["sushi", "iskender", "yaprak sarma"]

# Replace the second item (index 1) with a new one
foods[1] = "karniyarik"

# Print the updated list
print(foods)


pause=input('pause')
clear_screen()
'''
#9

Create a tuple with four numbers. Try to change the first number (observe the error) 
and then print the tuple.
'''
# enter your code here

# Create a tuple with four numbers
nums = (10, 20, 30, 40)

# Try to change the first number
try:
    nums[0] = 99
except TypeError as e:
    print("Error:", e)

# Print the tuple
print("Tuple is still:", nums)


pause=input('pause')
clear_screen()
'''
#10

Create a dictionary representing a student (name, age). Update the age. Create a list of 
favorite numbers and add a new number.
'''
# enter your code here
# Create a dictionary for a student
student = {
    "name": "Melis",
    "age": 21
}

# Update the age
student["age"] = 22

# Create a list of favorite numbers
favorite_numbers = [3, 7, 11]

# Add a new number
favorite_numbers.append(42)

# Print results
print("Student:", student)
print("Favorite numbers:", favorite_numbers)

pause=input('pause')
clear_screen()
'''
#11

Ask the user to input their favorite quote. Save it to a file quotes.txt 
and read it back to print it.
'''
# enter your code here
# Ask the user for their favorite quote
quote = input("Enter your favorite quote: silly goose on the loose")

# Save it to quotes.txt
with open("quotes.txt", "w") as f:
    f.write(quote)

# Read it back
with open("quotes.txt", "r") as f:
    saved_quote = f.read()

# Print the result
print("You entered:", saved_quote)

pause=input('pause')
clear_screen()
'''
#12
Ask the user to input 5 numbers (one at a time), store them in a list, and print the sum and average.
'''
# enter your code here
# Ask the user for 5 numbers
numbers = []

for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate sum and average
total = sum(numbers)
average = total / len(numbers)

# Print results
print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)


pause=input('pause')
clear_screen()
'''Output:
Enter number 1: 7
Enter number 2: 1907 
Enter number 3: 21
Enter number 4: 8
Enter number 5: 2
Numbers: [7.0, 1907.0, 21.0, 8.0, 2.0]
Sum: 1945.0
Average: 389.0
pause
'''
