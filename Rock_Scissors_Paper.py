import random

user_selection = input("Enter Rock, Scissors or Paper: ")
user_variant = ["Rock", "Scissors", "Paper"]
comp_variant = random.choice(user_variant)

if user_selection not in user_variant:
    print("Enter right value")
    exit()
    
if user_selection == comp_variant:
    print("Draw")
elif (user_variant == "Rock" and "Scissors" == comp_variant) or \
        (user_variant == "Scissors" and comp_variant == "Paper") or \
        (user_variant == "Paper" and comp_variant == "Rock"):
    print("Player wins")
else:
    print("Computer wins")
