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

    # Buckets to hold all the votes
    coco = 0
    chatime = 0
    bubble_waffel = 0
    gong_cha = 0

    # Show all the bbt choices
    print("Vote for your favourite from the list.")
    print("Give the letter of your choice.")
    for choice in CHOICES:
        print(choice)
    # Ask the user for their choice
    vote = input("Your vote: ").lower().strip(",.?! ")
    # Add their vote to a running
    # tally
    if vote == "a":
        coco = coco + 1  # incrementation
    elif vote == "b":
        chatime += 1
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
