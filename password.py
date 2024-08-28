import random
import string

def generate_password(length):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    try:
        # Prompt the user for the desired password length
        length = int(input("Enter the desired length for the password: "))
        
        if length <= 0:
            print("Please enter a positive integer for the length.")
            return
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print("Generated Password:", password)
    
    except ValueError:
        print("Invalid input. Please enter a valid integer for the length.")

# Run the main function
if __name__ == "__main__":
    main()
