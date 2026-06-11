import random

hand = ["rock", "paper", "scissors"]

wins = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

computerHand = random.choice(hand)

my_play = int(input(
    "Choose:\n"
    "0 for Rock\n"
    "1 for Paper\n"
    "2 for Scissors\n"
    "> "
))

# safety check (prevents crash if user enters wrong number)
if my_play < 0 or my_play > 2:
    print("Invalid choice! Please select 0, 1, or 2.")
    exit()

my_hand = hand[my_play]

print(f"\nComputer chose: {computerHand}")
print(f"You chose: {my_hand}\n")

if computerHand == my_hand:
    print("It's a draw! 🤝")

elif wins[my_hand] == computerHand:
    print("You win! 🎉")

else:
    print("You lose! 😢")