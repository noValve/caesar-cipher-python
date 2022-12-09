import string
import os

#creates an alphabet containing every lowercase ascii character
ALPHABET = string.ascii_lowercase

def display():
    """
    Displays the name of the script and the credits :p.
    """
    
    logo = """ _____                            
/  __ \                           
| /  \/ __ _  ___  ___  __ _ _ __ 
| |    / _` |/ _ \/ __|/ _` | '__|
| \__/\ (_| |  __/\__ \ (_| | |   
\____/ \__,_|\___||___/\__,_|_|   

"""
    credits = "made by @noValve\n\n"
    print(logo, credits)
   
def clear_terminal():
    """
    Clears the terminal depending on what OS the user is running.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
   
def cipher(message, shift):
    """
    Ciphers a message using the caesar method.

    Args:
        message (string): The message to cipher.
        shift (int): The shift between the letters.

    Returns:
        string: The ciphered message.
    """
    
    result = ""
    for letter in message:
        result+=ALPHABET[(ALPHABET.find(letter.lower())+shift)%len(ALPHABET)]
    return result

def decipher(message, shift):
    """
    Decifers a message using the caesar method.

    Args:
        message (string): The ciphered message.
        shift (int): The shift used to cipher the original message.
    
    Returns:
        string: The deciphered message.
    """
    return cipher(message, -shift)

def decipher_bruteforce(message):
    """
    Deciphers the message using bruteforce.

    Args:
        message (string): The ciphered message.
    """
    for i in range(len(ALPHABET)):
        print("Shift " + str(i) + " : \t" + decipher(message, i), end="\n") 
        
def parameters(choice):
    if choice == "1":
        clear_terminal()
        display()
        print("\nEnter the desired message: ", end=" ")
        message = input()
        print("\nEnter the desired shift: ", end=" ")
        shift = input()
    return message, int(shift)
    
    
def display_result(result):
    clear_terminal()
    display()
    print("\nCiphered message: " + result)
    
def menu():
    clear_terminal()
    display()
    print("What do you wish to do?\n")
    print("\tCipher a message (1)")
    print("\tDecipher using a shift (2)")
    print("\tDecipher without using a shift (bruteforce) (3)")
    print("\tExit (4)")
    answer = input("\nAnswer: ")
    while answer not in ["1","2","3","4"]:
        answer = input("\nPlease, choose a correct number (1,2,3 or 4): ")
    return answer
    
        
def main():
    while(True):
        match menu():
            case "1":
                message, shift = parameters("1")
                result = cipher(message, shift)
                display_result(result)
                print("\nPress [ENTER] to continue.")
                input()
                
        
    

main()