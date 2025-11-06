# Numbers and Operations
# Author: Ubial
# 5 November 2025

# Create an algorithm to gather
# data to find the most popular
# bubble tea place around us

# Version 1
def vote_listed_choices():
    """Display all voting choices
    5 users vote for their choice
    Results will be printed"""
    CHOICES = [
        "A. CoCo",
        "B. Chatime",
        "C. BUBBLE WAFFEL",
        "D. gong cha"
    ]

    # Show all the bbt choices
    print("Vote for your favourite from the list.")
    print("Give the letter of your choice.")
    for choice in CHOICES:
        print(choice)
    # Ask the user for their choice
    # Add their vote to a running
    # tally
    # Give some raw scores
    # Give score as a percentage

# Version 2
# Ask the user what their fave
# bbt place is
# Add their vote to a running
# tally
# Give the raw score
# Give score as percentage

def main():
    vote_listed_choices()

if __name__ == "__main__":
    main()
