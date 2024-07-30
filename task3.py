import random
import string

def generate_password(length):
    if length < 1:
        return "Error! Password length should be at least 1."
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    print("Password Generator")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Password length should be at least 1. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()