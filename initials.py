# File: initials.py
# Description: Prints stylized large initials for MZM with specific spacing and period rules using only basic print functions and strings.
# Assignment Number: 1
#
# Name: Mubarik Zakari
# STUDENT ID:  2425401451
# Email: 2425401451@live.gctu.edu.gh
# Grader: Mr. Augustus Buckman 
#
# On my honor, Mubarik Zakari, this programming assignment is my own work
# and I have not provided this code to any other student.


def main():
    """Prints stylized large letters for the initials MZM according to strict formatting rules."""

    # 1. Blank line before the small initials
    print()

    # 2. Small initials: 1 line, 6 characters total
    print("...MZM")

    # 3. Blank line between small and large initials
    print()

    # 4. Large Initials (10 lines high, 12 chars per letter, 60 chars wide total)
    print("...MMM......MMM.........ZZZZZZZZZZZZ........MMM......MMM.....")
    print("...MMMM....MMMM.........ZZZZZZZZZZZZ........MMMM....MMMM.....")
    print("...MM.MM..MM.MM..................ZZ.........MM.MM..MM.MM.....")
    print("...MM..MMMM..MM................ZZ...........MM..MMMM..MM.....")
    print("...MM...MM...MM..............ZZ.............MM...MM...MM.....")
    print("...MM........MM............ZZ...............MM........MM.....")
    print("...MM........MM..........ZZ.................MM........MM.....")
    print("...MM........MM........ZZ...................MM........MM.....")
    print("...MM........MM...**...ZZZZZZZZZZZZ...**....MM........MM...**")
    print("...MM........MM...**...ZZZZZZZZZZZZ...**....MM........MM...**")

    # 5. Blank line after the large initials
    print()


if __name__ == "__main__":
    main()
