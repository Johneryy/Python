print("Enter your Score")

Grade1 = "A"
Grade2 = "B"
Grade3 = "C"
Grade4 = "D"
Grade5 = "E"
Grade6 = "F"

score = int(input())

if 70 <= score <= 100:
    print("Your Grade is :", Grade1, "\nExcellent!")
if 60 <= score <= 69:
    print("Your Grade is :", Grade2, "\nVery Good")
if 50 <= score <= 59:
    print("Your Grade is :", Grade3, "\nGood")
if 45 <= score <= 49:
    print("Your Grade is :", Grade4, "\nPassed")
if 40 <= score <= 44:
    print("Your Grade is :", Grade5, "\nPoor")
if score < 40:
    print("Your Grade is :", Grade6, "\nFailed")


