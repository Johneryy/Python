import random

r = "Rock"
p = "Paper"
s = "Scissors"

userName = input("Enter your name -> ")

rounds = int(input("How many rounds will you like to play?-> "))

userScore = 0
computerScore = 0
counter = 0

while counter < rounds:
    player = int(input("""
    CHOOSE YOUR OPTION:
    1.Rock
    2.Paper
    3.Scissors
    """))

    if player == 1:
        print("You chose", r)
    elif player == 2:
        print("You chose", p)
    elif player == 3:
        print("You chose", s)
    else:
        print("Invalid Option,Enter only 1 to 3")

    option = int(input("""
    1.Done
    0.Exit
    """))

    computer = random.randint(1, 3)
    if option == 1:
        if computer == 1:
            print("Computer chose", r)
        elif computer == 2:
            print("Computer chose", p)
        elif computer == 3:
            print("Computer chose", s)
    else:
        print(userName, "Lost")
        break

    if player == computer:
        print("No winner")
    elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        print("You lost", userName)
        computerScore += 1
        counter += 1
    else:
        print("You won", userName)
        userScore += 1
        counter += 1

        print("\nGameScore:\nComputer ->", computerScore, ":", userScore, "<-", userName)
        if (userScore == (rounds // 2 + 1)) or (computerScore == (rounds // 2 + 1)):
            counter = rounds

else:
    if computerScore > userScore:
        print("You lost the game", userName)
    elif computerScore < userScore:
        print("You won the game", userName)
    else:
        print("\nNo winner...You are as good as the computer.")
