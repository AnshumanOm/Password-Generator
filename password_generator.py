import random
import string

def get_user_input():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 1:
                raise ValueError("Length must be at least 1")
            break
        except ValueError as e:
            print(e)

    includes = {
        'letters': input("Include letters? (y/n): ").lower() == 'y',
        'numbers': input("Include numbers? (y/n): ").lower() == 'y',
        'symbols': input("Include symbols? (y/n): ").lower() == 'y'
    }

    if not any(includes.values()):
        raise ValueError("At least one character type must be selected")

    return length, includes

def generate_password(length, includes):
    char_set = ''
    if includes['letters']:
        char_set += string.ascii_letters
    if includes['numbers']:
        char_set += string.digits
    if includes['symbols']:
        char_set += string.punctuation

    if not char_set:
        raise ValueError("No valid characters selected for password generation")

    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

def main():
    try:
        length, includes = get_user_input()
        password = generate_password(length, includes)
        print("Generated Password:", password)
    except ValueError as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
