import random
import string

def generate_password(length):
    if length < 1:
        return "Password length must be greater than 0"

    # Define possible characters
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = lower + upper + digits + symbols

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("Password Generator")
    
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()

