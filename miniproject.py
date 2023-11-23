import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbol=True):
    characters = string.ascii_letters if use_uppercase else string.ascii_lowercase
    characters += string.digits if use_digits else ''
    characters += string.punctuation if use_symbol else ''

    if not characters:
        return "error no character selected"
    
    password= ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_preferences():
    print("Password Generated Prefernences")
    length = int(input("Enter the desired password length"))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower()=='y'
    use_digits = input("Include digits? (y/n): ").lower()=='y'
    use_symbol = input("Include symbols? (y/n): ").lower()=='y'
    return length, use_uppercase, use_digits, use_symbol

def save_password_to_file(password, filename='passwaors.txt'):
    with open(filename, 'a') as file:
        file.write(password + '\n')

def main():
    length, use_uppercase, use_digits, use_sumbols = get_user_preferences()
    save_to_file = input("Save passwords to a file? (y/n):").lower() == 'y'

    for _ in range(num_password):
        password = generate_password(length, use_uppercase, use_digits, use_digits)
        print("Generated Password:", password)

        if save_to_file:
            save_password_to_file(password)

if __name__== "__main__":
    main()