import random

Name_Of_Player = input("Enter your name: ")

user_action = input("Enter a choice (rock, paper, scissors): ")


actions = ["rock", "paper", "scissors"]
computer = random.choice(possible_actions)

print(f"\n{Name_Of_Player} chose {user_action} and  computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. No Winner!")

elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors!", Name_Of_Player, "Won!")
    else:
        print("Paper covers rock!", Name_Of_Player, "lost.")

elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock!", Name_Of_Player, "Won!")
    else:
        print("Scissors cuts paper!", Name_Of_Player, "lost.")

elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper!", Name_Of_Player, "Won!")
    else:
        print("Rock smashes scissors!", Name_Of_Player, "lose.")
