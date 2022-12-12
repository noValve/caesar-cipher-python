import string
import os
import keyboard

#creates an alphabet containing every lowercase ascii character
ALPHABET = string.ascii_lowercase
FRENCH_ALPHABET = "abcdefghijklmnopqrstuvwxyzéèàùêâîôûçëïüÿäö"

def display():
    """
    Displays the name of the script and the credits :p.
    """
    
    logo = """ _____                          _____           _ 
/  __ \                        |_   _|         | |
| /  \/ __ _  ___  ___  __ _ _ __| | ___   ___ | |
| |    / _` |/ _ \/ __|/ _` | '__| |/ _ \ / _ \| |
| \__/\ (_| |  __/\__ \ (_| | |  | | (_) | (_) | |
\_____/\__,_|\___||___/\__,_|_|  \_/\___/ \___/|_|

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
        result+= ALPHABET[(ALPHABET.find(letter)+shift)%len(ALPHABET)] if letter in ALPHABET else letter
        #result+=ALPHABET[(ALPHABET.find(letter.lower())+shift)%len(ALPHABET)]
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
    
    Returns:
        string: The deciphered message with every possible shift.
    """
    result = ""
    for i in range(len(ALPHABET)):
        result+="Shift " + str(i) + " : \t" + decipher(message, i) + "\n" 
    return result
        
def parameters(choice):
    message = ""
    shift = 0
    match choice:
        case "1":
            clear_terminal()
            display()
            print("\n(for the ciphering to work better, don't use any special character)")
            print("\nEnter the desired message: ", end=" ")
            message = input()
            print("\nEnter the desired shift: ", end=" ")
            shift = input()
            while(not shift.isdigit()):
                print("\nPlease, enter a number: ", end=" ")
                shift = input()
        case "2":
            clear_terminal()
            display()
            print("\nEnter the ciphered message: ", end=" ")
            message = input()
            print("\nEnter the shift: ", end=" ")
            shift = input()
            while(not shift.isdigit()):
                print("\nPlease, enter a number: ", end=" ")
                shift = input()
        case "3":
            clear_terminal()
            display()
            print("\nEnter the ciphered message: ", end=" ")
            message = input()
    return message, int(shift)
    
    
def display_result(result):
    clear_terminal()
    display()
    print("\nCiphered message: " + result)
    
def wait_for_input():
    """
    Waits for the user to press enter.
    """
    print("\nPress [Enter] to continue.") 
    input()
            
def menu():
    """
    Displays the menu and asks the user to choose an option.
    
    Returns:
        string: the user's answer.
    """
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
                wait_for_input()
            case "2":
                message, shift = parameters("2")
                result = decipher(message, shift)
                display_result(result)
                wait_for_input()
            case "3":
                message, shift = parameters("3")
                result = decipher_bruteforce(message)
                display_result(result)
                wait_for_input()
            case "4":
                exit()
                
        
    

main()