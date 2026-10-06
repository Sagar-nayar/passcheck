"""passcheck v1 - password strength analyzer.

Fill in each function below. Run the program with:
    python -m passcheck.main
Check your work with:
    pytest
"""


def score_password(password: str) -> int:
    """Return a score from 0 to 6 for the given password.

    One point for each of these:
      - length is at least 8
      - length is at least 12 (bonus point, on top of the one above)
      - contains a lowercase letter
      - contains an uppercase letter
      - contains a digit
      - contains a symbol (anything that is not a letter or digit)
    """
    score = 6 - len(get_feedback(password))
    return score



def get_rating(score: int) -> str:
    """Turn a score into a rating: 0-2 "Weak", 3-4 "Medium", 5-6 "Strong"."""
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def get_feedback(password: str) -> list[str]:
    """Return a list of tips for each rule the password fails.

    Example: ["Use at least 12 characters", "Add a symbol"]
    A password that passes every rule returns an empty list.
    """
    list_tips = ["Use at least 8 characters", "Use at least 12 characters", 
                 "Add a lowercase letter", "Add an uppercase letter", 
                 "Add a digit", "Add a symbol"]

    feedback = []
    if len(password) < 8:
        feedback.append(list_tips[0])
    if len(password) < 12:
        feedback.append(list_tips[1])
    if not any(char.islower() for char in password):
        feedback.append(list_tips[2])
    if not any(char.isupper() for char in password):
        feedback.append(list_tips[3])
    if not any(char.isdigit() for char in password):
        feedback.append(list_tips[4])
    if not any(not char.isalnum() for char in password):
        feedback.append(list_tips[5])

    return feedback

def load_common_passwords(path: str) -> set[str]:
    """Read a wordlist file and return its passwords as a set.

    One password per line. Remove the newline from each one.
    """
    common_passwords=set()
    with open(path, encoding="utf-8") as f:
        for line in f:
            common_passwords.add(line.strip())

    return common_passwords


def is_common(password: str, common: set[str]) -> bool:
    """Return True if the password is in the common-passwords set.

    The check ignores upper/lower case: "PASSWORD" counts as "password".
    """
  
    return password.lower() in common













def main() -> None:
    """Ask the user for a password, then print its score, rating, and tips."""
    password = input("Enter a password to check: ")

    score = score_password(password)
    rating = get_rating(score)
    feedback = get_feedback(password)
    common = load_common_passwords("data/common.txt")
    if is_common(password, common):
        print("⚠ This password has been found in data leaks")
        rating = "Weak"

    print(f"Score: {score}/6")
    print(f"Rating: {rating}")
    if feedback:
        print("Feedback:")
        for tip in feedback:
            print(f"- {tip}")
    else:
        print("Your password is strong!")

if __name__ == "__main__":
    main()
