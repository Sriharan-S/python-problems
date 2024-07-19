import random
import string

def generate_password(length, use_special_chars=True):
    if length < 1:
        raise ValueError("Password length must be at least 1.")
    
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ''
    
    all_chars = lower_chars + upper_chars + digits + special_chars
    
    if not all_chars:
        raise ValueError("At least one character set must be selected.")
    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

length = int(input("Enter the length of the password: "))
use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

password = generate_password(length, use_special_chars)
print(f"Generated Password: {password}")
