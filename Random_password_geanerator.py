import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user-defined length
try:
    length = int(input("Enter the length of the password: "))
    if length <= 0:
        raise ValueError("Length must be a positive integer.")
except ValueError as e:
    print(e)
    exit()

# Generate and print the random password
password = generate_password(length)
print(f"Generated Password: {password}")
