import random
import string

def generate_password(length=12):
    # Define the characters to use in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password of the given length
    password = ''.join(random.choice(all_characters) for i in range(length))

    return password

# Example usage:
password = generate_password(16)  # You can change the length as needed
print("Generated Password:", password)
