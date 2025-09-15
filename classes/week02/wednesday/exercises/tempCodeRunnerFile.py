Prompt the user for a number and display whether it’s positive, negative, or zero.
'''
value == int(input("Type a number: "))
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