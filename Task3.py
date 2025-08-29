import random
import string

print("Password Generator")

while True:
    try:
        length = int(input("\nEnter password length (or 0 to exit): "))
        if length == 0:
            print("Goodbye!")
            break
        if length < 4:
            print("Password length should be at least 4.")
            continue

        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))
        print("Generated Password:", password)

    except ValueError:
        print("Please enter a valid number.")
