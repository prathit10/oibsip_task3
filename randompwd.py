import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_pool = ''
    
    if use_letters:
        character_pool += string.ascii_letters  
    
    if use_numbers:
        character_pool += string.digits 
    
    if use_symbols:
        character_pool += string.punctuation 
    
    if not character_pool:
        raise ValueError("At least one character set must be selected")
    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # User input
    length = int(input("Enter the length of the password: "))
    
    print("Choose the character sets to include in the password (you can choose multiple options):")
    print("1. Letters (a-z, A-Z)")
    print("2. Numbers (0-9)")
    print("3. Symbols (!, @, #, etc.)")
    print("Enter your choices as a comma-separated list (e.g., 1,2 for letters and numbers): ")
    
    choices = input().split(',')
    
    use_letters = '1' in choices
    use_numbers = '2' in choices
    use_symbols = '3' in choices
    
    if not (use_letters or use_numbers or use_symbols):
        print("Invalid choice. At least one character set must be selected.")
        return
    
     # Generate pwd based on user input
    password = generate_password(length, use_letters, use_numbers, use_symbols)
    print(f"Generated password: {password}")
   
if __name__ == "__main__":
    main()
