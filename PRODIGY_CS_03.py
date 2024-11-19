import re

def assess_password_strength(password):
    # Initialize score
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should contain lowercase letters.")
    
    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Password should contain uppercase letters.")
    
    # Check for digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")
    
    # Strength evaluation based on score
    if score == 5:
        return "Strong password!", feedback
    elif score >= 3:
        return "Moderate password.", feedback
    else:
        return "Weak password.", feedback

# Example usage
password = input("Enter a password to assess: ")
strength, feedback = assess_password_strength(password)
print(f"Password Strength: {strength}")
if feedback:
    print("Feedback:")
    for comment in feedback:
        print(f"- {comment}")
