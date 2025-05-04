# collect user preferences
# - length
# - should contain uppercase
# - should contain special
# - should contain digits

# get all available characters
# randomly pick characters up to the length
# ensure we have at least one of each character type
# ensure length is valid

import random
import string

def generate_password():
    length = int(input("Enter password length: ").strip())
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower()
    include_special = input("Include uppercase special characters? (yes/no): ").strip().lower()
    include_digits = input("Include uppercase digits? (yes/no): ").strip().lower()


    if length < 4:
        print("Password length must be at least 4 characters.")
        return 
    
    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else "" 
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""

    all_characters = lower + uppercase + special + digits

    
    required_characters = []
    if include_uppercase == "Yes":
        required_characters.append(random.choice(uppercase))

    if special == "Yes":
        required_characters.append(random.choice(special))

    if digits == "Yes":
        required_characters.append(random.choice(digits))

    remaining_length = length - len(required_characters)
    password = required_characters

    for _ in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)


    random.shuffle(password)

    str_password = "".join(password)
    return str_password 


password = generate_password()
print(password)


