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
    # TODO
    pass


def get_rating(score: int) -> str:
    """Turn a score into a rating: 0-2 "Weak", 3-4 "Medium", 5-6 "Strong"."""
    # TODO
    pass


def get_feedback(password: str) -> list[str]:
    """Return a list of tips for each rule the password fails.

    Example: ["Use at least 12 characters", "Add a symbol"]
    A password that passes every rule returns an empty list.
    """
    # TODO
    pass


def main() -> None:
    """Ask the user for a password, then print its score, rating, and tips."""
    # TODO
    pass


if __name__ == "__main__":
    main()
