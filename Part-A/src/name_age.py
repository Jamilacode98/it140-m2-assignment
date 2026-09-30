The main purpose of this program is to the user to get the feel of coding.

Input:
     prompt the user to enter their name using the prompt "What is your name?" Functional requirements 1.1.
     Prompt the user to enter their age using the prompt "How old are you?" Functional requirements 1.2.
    

Process:
    Treat the entered age as an integer that can be used in an arithmetic calculation Functional requirements 1.3
    Calculate the user's approximate birth year by subtracting the entered age from the current calendar year Functional Requirements 1.4.

Output:
    Display a personalized result using the user's name and calculated birth year in this format Functional requirements 1.5.

Typical usage example:
    "What is your name?".
    "How old are you? ".
    Hello {name}! You were born in {year}.

.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    # Print("What is your name?").
    # input_text = input(Enter a number:)

    # Calculate user's approximate birth year.
      current_year = 2026
      birth_year = current_year -age

    # Output personalized message with user's name and birth year.
    # print(f"Hello, {name} ! You were born around {birth year}.").


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===

