import random

correct_guess = random.randint(0, 100)

count = 0
while count < 5:
    guess = int(input("Guess a number between 0 and 100: "))

    if guess < 0 or guess > 100:
        print("Out of range.......You lost!!!")
        break

    if guess < correct_guess:
        print("Too Low, Try again")

    elif guess > correct_guess:
        print("Too high, try again")

    else:
        print("Awesome, You are correct")
        break

    count += 1

else:
    print("You tried but you can never make it")







