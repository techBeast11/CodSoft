import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def check_password_strength(password):
    criteria = [
        any(char.islower() for char in password),
        any(char.isupper() for char in password),
        any(char.isdigit() for char in password),
        any(char in string.punctuation for char in password)
    ]
    return all(criteria)

# Get user input for password length
try:
    password_length = int(input("Enter the desired password length: "))
except ValueError:
    print("Invalid input. Using default length of 12.")
    password_length = 12

# Generate a password based on user input
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)

# Check and print password strength
strength = check_password_strength(generated_password)
print("Password Strength:", "Strong" if strength else "Weak")
