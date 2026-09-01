def password_strength_checker():
    password = input("Enter your password: ")
    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
    strength = 0

    if len(password) > 8:
        strength += 1

    if any(c.isupper() for c in password):
        strength += 1

    if any(c.islower() for c in password):
        strength += 1

    if any(c.isdigit() for c in password):
        strength += 1

    if any(c in special_characters for c in password):
        strength += 1

    if strength <= 2:
        label = "Weak"
    elif strength <= 4:
        label = "Medium"
    else:
        label = "Strong"

    print(f"Password strength: {strength} from 5 ({label})")

password_strength_checker()