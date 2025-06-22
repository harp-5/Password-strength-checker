import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters."
    if not re.search(r'[A-Z]', password):
        return "Weak: Needs at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Weak: Needs at least one lowercase letter."
    if not re.search(r'[0-9]', password):
        return "Weak: Needs at least one number."
    return "Strong password!"

if __name__ == "__main__":
    password = input("Enter password to check: ")
    print(check_password_strength(password))



