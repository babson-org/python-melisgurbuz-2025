
from classes.week00.second_class.utils import clear_screen

'''
#13 - Conditional Logic
Prompt the user for a number and display whether it’s positive, negative, or zero.
'''
value = int(input("Type a number: "))
if value > 0:
    print("The number is positive")
elif value < 0:
    print("The number is negative")
else:
    print("The number is zero")

pause = input('pause')
clear_screen()
'''
Type a number: 2
The number is positive
'''


'''
#14 - Even/Odd Check
Ask the user for a number and show if it is even or odd.
'''
number = int(input("Enter any integer: "))
if number % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")

pause = input('pause')
clear_screen()


'''
#15 - Boolean Operators
Request two numbers. Report if both are positive, if at least one is positive, or if neither is.
'''
x = int(input("First number: "))
y = int(input("Second number: "))

if x > 0 and y > 0:
    print("Both numbers are positive")
elif x > 0 or y > 0:
    print("One of them is positive")
else:
    print("Neither number is positive")

pause = input('pause')
clear_screen()


'''
#16 - For Loop
Print numbers from 1 through 20, but leave out multiples of 3.
'''
for n in range(1, 21):
    if n % 3 == 0:
        continue
    print(n)

pause = input('pause')
clear_screen()
'''
1
2
4
5
7
8
10
11
13
14
16
17
19
20
'''


'''
#17 - While Loop
Keep asking the user to guess a fixed secret number until they succeed.
'''
hidden = 7
guess = -1
while guess != hidden:
    guess = int(input("Guess the secret number: "))
print("You got it!")

pause = input('pause')
clear_screen()
'''
Guess the secret number: 10
Guess the secret number: 8
Guess the secret number: 7
You got it!
'''


'''
#18 - Break / Continue
Show numbers from 1 to 10, but skip the number 3 and stop once 7 is reached.
'''
for n in range(1, 11):
    if n == 3:
        continue
    if n == 7:
        break
    print(n)

pause = input('pause')
clear_screen()
'''
1
2
4
5
6
'''


'''
#19 - Function Definition
Make a function square(num) that returns a squared value and try it out.
'''
def square(num):
    return num ** 2

print("The square of 5 equals:", square(5))

pause = input('pause')
clear_screen()
'''
The square of 5 equals: 25
'''


'''
#20 - Function with Mutable Argument
Write a function add_item(lst, val) that appends to the list and check how it affects the original list.
'''
def add_item(lst, val):
    lst.append(val)

items = [1, 2, 3]
add_item(items, 4)
print("List after adding:", items)

pause = input('pause')
clear_screen()
'''
List after adding: [1, 2, 3, 4]
'''


'''
#21 - Comments / Documentation
Define a function greet(person) with single-line and multi-line comments describing each part.
'''
def greet(person):
    # Display a hello message
    """
    This function accepts a name
    and prints a personalized greeting.
    """
    print(f"Hi, {person}!")

greet("Melis")

pause = input('pause')
clear_screen()
'''
Hi, Melis!
'''


'''
#22 - Combining Tools
Ask the user to provide 5 names. Capitalize each one, sort them, and print the list.
'''
people = []
for i in range(5):
    entry = input(f"Name {i+1}: ")
    people.append(entry.capitalize())

people.sort()
print("Alphabetical list:", people)

pause = input('pause')
clear_screen()
'''
Name 1: Melis
Name 2: Serra
Name 3: Deniz
Name 4: Ali
Name 5: Zeynep
Alphabetical list: ['Ali', 'Deniz', 'Melis', 'Serra', 'Zeynep']
'''