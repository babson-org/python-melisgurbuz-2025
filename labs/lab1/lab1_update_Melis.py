'''
Melis, would like to have a better understanding of your computational thinking
for each problem.  The loop for text input in the diamond problem doesn't make any
sense.

No points off but it appears you and another student may have shared to much code.

Grade A-

'''

# ==============================
# Main Program
# ==============================
def main():
    while True:
        print("Lab 1 - Python Basics")
        print("1. Draw Diamond")
        print("2. Text Analysis")
        print("3. Caesar Cipher")
        choice = input("Select part to run (1-3): ")
        
        if choice == "1":
            draw_diamond()
        elif choice == "2":
            text_analysis()
        elif choice == "3":
            caesar_cipher()
        else:
            exit()



"""
Lab 1 - Python Basics
Author: <Your Name>
Instructions: Complete each part below. Save your work and commit + sync in Codespaces.
"""

# ==============================
# Part 1: Draw a Diamond
# ==============================
def draw_diamond():
    """
    Ask the user for an odd number for the diamond height
    and print a symmetric diamond of that height.
    """
    
    print("you have some work todo!, draw_diamond")

"""
STEPS I TOOK:
Prompted user for input → used a while True loop with try/except to make sure the input is an integer 
→ checked if the integer was odd (height % 2 == 1), otherwise told the user to re-enter.
→ if the user typed something that is not a number, printed a correction message.
→ looped through odd numbers 1, 3, 5… height and printed spaces and stars centered.
→ looped backward from height - 2 down to 1, printing spaces + stars to mirror the top.
"""
    # TODO: Prompt user for an odd number

while True:
    try:
        height = int(input("Please enter an odd integer for the diamond height: "))
        if height % 2 == 1:   
            break
        else:
            print("Follow directions, enter an odd number!")
    except ValueError:
        print("Follow directions, enter an number which is odd!")

    # TODO: Draw the top half of the diamond
for i in range(1, height + 1, 2):
        spaces = (height - i) // 2
        if i == 1:
            print(" " * spaces + "*")
        else:
            print(" " * spaces + "*" + " " * (i - 2) + "*")

    # TODO: Draw the bottom half of the diamond
for i in range(height - 2, 0, -2):
        spaces = (height - i) // 2
        if i == 1:
            print(" " * spaces + "*")
        else:
            print(" " * spaces + "*" + " " * (i - 2) + "*")
# Uncomment to test Part 1
draw_diamond()


# ==============================
# Part 2: Count Letters, Words, and Sentences
# ==============================
def text_analysis():
    """
    Ask the user for a block of text.
    Count and display:
        - Number of letters (only count a-zA-Z)
        - Number of words   (use split())
        - Number of sentences (., ?, !) 

    STEPS I TOOK:
    - used a while True loop to make sure the user entered valid text.
    - checked each character with .isalpha() to ensure at least one letter was included.
    - looped through text and increased `letters` when character was alphabetic.
    - counted words with len(text.split()).
    - counted sentences whenever ., ?, or ! was found.
    - displayed results with print().
    """
    

    # TODO: Get user input

'''
#############let's examine this block#######################################
while True:
        text = input("Enter some text: ")
        # check if there is at least one alphabetic character
        has_letter = False
        for letter in text:
            if letter.isalpha():
                has_letter = True
                break
        if has_letter:
            break
        else:
            print("Follow directions, only enter letters not numbers")
#########################################################################

why has_letter? you don't need a loop for text entry

text = input("Enter some text: ")    

also, this looks exactly like what another student did

'''

# this can be done in one loop

text = input("Enter some text: ")
    # TODO: Count letters
letters = 0
for letter in text:
        if letter.isalpha():
            letters += 1
    # TODO: Count words
words = len(text.split())

    # TODO: Count sentences
sentences = 0
for letter in text:
        if letter in ".!?":
            sentences += 1
    # TODO: Print the results
print(f"Letters: {letters}")
print(f"Words: {words}")        # replace 0
print(f"Sentences: {sentences}")    # replace 0

# Uncomment to test Part 2
text_analysis()

# ==============================
# Part 3: Caesar Cipher – Encrypt and Decrypt
# ==============================
def caesar_cipher():
    """
    Ask the user for text and a shift value.
    Provide options to encrypt or decrypt the text using a Caesar cipher.
    """

"""    
STEPS I TOOK:
Defined the function caesar_cipher() → with a docstring describing encryption and decryption using Caesar cipher.
→ used a while True loop to ensure the input had at least one alphabetic character (.isalpha() check).
→ used another while True with try/except to make sure the shift entered was an integer.
→ prompted the user to choose encryption ('e') or decryption ('d'), looping until a valid response was given.
Handled decryption → if user chose 'd', reversed the shift by making it negative.
Implemented Caesar cipher logic:
→If it's a letter → shifted it forward/backward within the alphabet.
Used ord() and chr() with a base ('A' for uppercase, 'a' for lowercase) to wrap correctly with % 26.
If it wasn't a letter → added it unchanged to the result.
→ printed both the original text and the encrypted/decrypted version.
"""
print("you have some work todo!, caesar_cypher")

    # TODO: Get user input text
while True:
        text = input("Enter some text: ")
        has_letter = False
        for letter in text:
            if letter.isalpha():
                has_letter = True
                break
        if has_letter:
            break
        else:
            print("Follow directions, enter text:")

    # TODO: Get shift value
while True:
        try:
            shift = int(input("Please enter an integer shift, an integer shift is you shift each letter forward by the number specified by the shift integer: "))
            break
        except ValueError:
            print("Follow directions and enter a number!")
    # TODO: Ask user whether to encrypt or decrypt
while True:
        choice = input("Type 'e' to encrypt or 'd' to decrypt, to encrypt a message, you shift each letter forward by the number specified by the shift integer, and decrypt is the backward shift : ").lower()
        if choice in ("e", "d"):
            break
        else:
            print("Follow directions please, enter 'e' or 'd'!")
if choice == "d": 
        shift = -shift   # flip shift direction if decrypting
    # TODO: Implement encryption and decryption logic
result = ""
for letter in text:
        if letter.isalpha():
            if letter.isupper():
                base = ord("A")
                result += chr((ord(letter) - base + shift) % 26 + base)
            else:
                base = ord("a")
                result += chr((ord(letter) - base + shift) % 26 + base)
        else:
            result += letter

    # TODO: Print the final result
print("Original:", text)
print("Result:  ", result)

# Uncomment to test Part 3
caesar_cipher()




if __name__ == "__main__":
    main()