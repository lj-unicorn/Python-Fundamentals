# rock - 1 
# paper -2 
# scissors -3

import random

hand = ["rock", "paper", "scissors"]

# computer play
computerHand = random.choice(hand)

# my play
my_play = int(input(
    "Choose:\n"
    "0 for Rock\n"
    "1 for Paper\n"
    "2 for Scissors\n"
))

my_hand= hand[my_play]

if computerHand == my_hand: 
  print(f"Computer choose {computerHand} and you also choose {my_hand}. So, it is draw!")

if computerHand == "rock" and my_hand == "paper":
  print("Computer choose rock. So, you won.")
elif computerHand == "paper" and my_hand == "rock":
  print("Computer choose paper. So, you lost.")

if computerHand == "rock" and my_hand == "scissors":
  print("Computer choose rock. So, you lost.")
elif computerHand == "scissors" and my_hand == "rock":
  print("Computer choose scissors. So,you won.")

if computerHand == "paper" and my_hand == "scissors":
  print("Computer choose paper. So, you won.")
elif computerHand == "scissors" and my_hand == "paper":
  print("Computer choose scissors. So, you lost.")