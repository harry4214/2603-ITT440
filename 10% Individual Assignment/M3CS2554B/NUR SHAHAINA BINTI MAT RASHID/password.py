import random
import string

# generate password with random level
def generate_password():
    level = random.choice(["Weak", "Medium", "Strong"])

    if level == "Weak":
        characters = string.ascii_lowercase
        length = random.randint(4, 6)

    elif level == "Medium":
        characters = string.ascii_letters
        length = random.randint(7, 9)

    else:
        characters = string.ascii_letters + string.digits
        length = random.randint(10, 12)

    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password


# check strength
def check_strength(password):
    score = 0

    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if len(password) >= 10:
        score += 1

    if score <= 1:
        return "Weak"
    elif score <= 3:
        return "Medium"
    else:
        return "Strong"


def task(i):
    password = generate_password()
    strength = check_strength(password)
    return (i + 1, password, strength)