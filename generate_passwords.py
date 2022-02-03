import string
import random

# storing all the possible characters for password generation
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.digits + string.ascii_letters + "!@#$%^&*()")

# function to generate random password of given length
def generate_password():
    length = int(input("Enter password length: "))

    password = []

    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    print("".join(password))



# function to generate custom random password of given length
def generate_custom_password():
    length = int(input("Enter password length: "))

    alphabets_count = int(input("Enter the count of alphabets: "))
    digits_count = int(input("Enter the count of digits: "))
    special_characters_count = int(
        input("Enter the count of special characters: "))

    characters_count = alphabets_count+digits_count+special_characters_count

    if characters_count > length:
        print("Characters total count is greater than password's length !")
        return

    password = []

    for i in range(alphabets_count):
        password.append(random.choice(alphabets))

    for i in range(digits_count):
        password.append(random.choice(digits))

    for i in range(special_characters_count):
        password.append(random.choice(special_characters))

    if characters_count < length:
        random.shuffle(password)
        for i in range(length - characters_count):
            password.append(random.choice(characters))

    random.shuffle(password)

    print("".join(password))


print("Generate Passwords using 2 methods: ")
print("1. Generate Random Password")
print("2. Genrate Custom Random Password")

choice=int(input("Enter choice: "))

if choice==1:
    generate_password()
elif choice==2:
    generate_custom_password()
else:
    print("Invalid option !!, generating random password.")
    generate_password()

