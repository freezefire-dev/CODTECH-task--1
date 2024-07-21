import re
import string

def check_length(password):
    """Check if the password meets the minimum length requirement."""
    min_length = 8
    if len(password) < min_length:
        return False, f"Password should be at least {min_length} characters long."
    return True, ""

def check_complexity(password):
    """Check if the password contains uppercase, lowercase, digits, and special characters."""
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    if not all([has_upper, has_lower, has_digit, has_special]):
        return False, "Password must include uppercase letters, lowercase letters, digits, and special characters."
    return True, ""

def check_uniqueness(password):
    """Check for common patterns and repeated characters."""
    common_patterns = [r'123456', r'password', r'123456789', r'12345678']
    for pattern in common_patterns:
        if re.search(pattern, password, re.IGNORECASE):
            return False, "Password is too common or contains common patterns."

    if len(set(password)) < len(password) / 2:
        return False, "Password contains too many repeated characters."

    return True, ""

def assess_password(password):
    """Assess the strength of the given password."""
    results = []
    
    # Length Check
    valid, message = check_length(password)
    results.append(message)
    
    # Complexity Check
    valid, message = check_complexity(password)
    results.append(message)
    
    # Uniqueness Check
    valid, message = check_uniqueness(password)
    results.append(message)
    
    # Overall Strength Assessment
    if all("not" not in result for result in results):
        return "Password is strong!"
    return "\n".join(result for result in results if result)

def main():
    password = input("Enter the password to assess: ")
    feedback = assess_password(password)
    print(feedback)

if __name__ == "__main__":
    main()
