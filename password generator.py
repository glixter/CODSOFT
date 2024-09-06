import random
import string


def generate_password(length,
                      use_uppercase=True,
                      use_digits=True,
                      use_special=True):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special else ''

    all_characters = lowercase + uppercase + digits + special

    if not all_characters:
        return "Error! No character sets selected."

    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password


def main():
    print("Welcome to the Python Password Generator!")

    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for the length.")
        return

    if length <= 0:
        print("Password length must be greater than 0.")
        return

    use_uppercase = input(
        "Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special = input(
        "Include special characters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, use_uppercase, use_digits,
                                 use_special)

    print(f"Generated Password: {password}")


if __name__ == "__main__":
    main()
