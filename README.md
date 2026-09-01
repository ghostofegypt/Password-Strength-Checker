# Password-Strength-Checker
A Python script that scores password strength based on length and character variety.

## How It Works

The program asks the user to enter a password, then checks it against five criteria. Each criterion met adds one point to the strength score, out of a maximum of 5.

### Scoring Criteria
- Length greater than 8 characters
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit
- Contains at least one special character (`!@#$%^&*()-_=+[]{}|;:',.<>?/\`~`)

## How to Run

1. Make sure you have Python installed.
2. Run the script:
3. Enter a password when prompted.

## Note

This tool only scores a password's *composition* — it doesn't check it against known breached password lists or common patterns (like "password123"). A high score here doesn't guarantee a password is actually safe to use.

## Possible Improvements

- Add a strength label (e.g. "Weak", "Medium", "Strong") instead of just a number
- Check against a list of commonly used/breached passwords
- Penalize repeated characters or simple sequences (e.g. "1234", "aaaa")
