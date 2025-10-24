"""
Lab 1 – Python Basics
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
    # TODO: Prompt user for an odd number
    height = int(input("Enter an odd number for the diamond height: "))

    # TODO: Draw the top half of the diamond

    # TODO: Draw the bottom half of the diamond

# Uncomment to test Part 1
# draw_diamond()


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
    """
    # TODO: Get user input
    text = input("Enter some text: ")

    # TODO: Count letters
    letters = 0

    # TODO: Count words

    # TODO: Count sentences

    # TODO: Print the results
    print(f"Letters: {letters}")
    print(f"Words: {0}")        # replace 0
    print(f"Sentences: {0}")    # replace 0

# Uncomment to test Part 2
# text_analysis()


# ==============================
# Part 3: Caesar Cipher – Encrypt and Decrypt
# ==============================
def caesar_cipher():
    """
    Ask the user for text and a shift value.
    Provide options to encrypt or decrypt the text using a Caesar cipher.
    """
    # TODO: Get user input text
    text = input("Enter text: ")

    # TODO: Get shift value
    shift = int(input("Enter shift value (integer): "))

    # TODO: Ask user whether to encrypt or decrypt
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    # TODO: Implement encryption and decryption logic
    result = ""

    # TODO: Print the final result
    print("Result:", result)

# Uncomment to test Part 3
# caesar_cipher()


# ==============================
# Main Program
# ==============================
def main():
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
        print("Invalid choice.")

if __name__ == "__main__":
    main()

def draw_diamond():
    """
    Ask the user for an odd number for the diamond height
    and print a symmetric filled diamond of that height using '-'.
    """
    
while True:
        try:
            height = int(input("Please enter an odd number for the diamond height: "))
            if height % 2 == 1:   # check odd
                break
            else:
                print("Enter an odd number!")
        except ValueError:
            print("Enter a number that is odd!")

    # Top half
for i in range(1, height + 1, 2): 
        spaces = (height - i) // 2     
        print(" " * spaces + "-" * i)   # CHANGED LINE (was hollow)

    # Bottom half
for i in range(height - 2, 0, -2):
        spaces = (height - i) // 2
        print(" " * spaces + "-" * i)   # CHANGED LINE (was hollow)
""""""
------------------------------------------
""""""

def draw_diamond():
    """
    Ask the user for an odd number for the diamond height
    and print a symmetric diamond of that height.
    """
    
    print("you have some work todo!, draw_diamond")
# keep prompting until user enters a valid odd integer
    # TODO: Prompt user for an odd number
while True:
    try:
        height = int(input("Enter an odd number for the diamond height: "))
        if height > 0 and height % 2 == 1:   
            break
        else:
            print("Enter an odd number")
    except ValueError:
        print("Make sure to enter an odd number")

# print top half of diamond (including middle row)
    # TODO: Draw the top half of the diamond
for i in range(1, height + 1, 2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i)

# print bottom half of diamond
    # TODO: Draw the bottom half of the diamond
for i in range(height - 2, 0, -2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i)

''''''
-----------------------------------------------------
''''''
def caesar_decode_check(message):
    """
    Brute-force Caesar cipher to see if any decoding
    contains the word 'python'.
    """

    message = message.lower()   # ignore case
    target = "python"

    for shift in range(26):  # try all shifts
        decoded = ""
        for ch in message:
            if ch.isalpha():
                base = ord('a')
                decoded += chr((ord(ch) - base - shift) % 26 + base)
            else:
                decoded += ch
        if target in decoded:   # check for keyword
            print(f"Found with shift {shift}: {decoded}")
            return decoded

    print("No decoded message contains the word 'python'.")
    return None


# Example usage:
encrypted = "wduklq sbwkrq lv ixq"   # Caesar shift 3 of "training python is fun"
caesar_decode_check(encrypted)

