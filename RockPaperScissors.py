import random

Name_Of_Player = input("Enter your name: ")
user_actions = input("Enter a choice (rock, paper, scissors): ")


actions = ["rock", "paper", "scissors"]
computer = random.choice(actions)

print(f"\n{Name_Of_Player} chose {user_actions} and  computer chose {computer}.\n")

if user_actions == computer:
    print(f"Both players selected {user_actions}. No Winner!")

elif user_actions == "rock":
    if computer == "scissors":
        print("Rock smashes scissors!", Name_Of_Player, "Won!")
    else:
        print("Paper covers rock!", Name_Of_Player, "lost.")

elif user_actions == "paper":
    if computer == "rock":
        print("Paper covers rock!", Name_Of_Player, "Won!")
    else:
        print("Scissors cuts paper!", Name_Of_Player, "lost.")

elif user_actions == "scissors":
    if computer == "paper":
        print("Scissors cuts paper!", Name_Of_Player, "Won!")
    else:
        print("Rock smashes scissors!", Name_Of_Player, "lose.")
