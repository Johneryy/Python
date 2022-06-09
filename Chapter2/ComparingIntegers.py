num = int(input("Enter number-> "))

Sqr = num * num

if Sqr:
    print("Square is ->", Sqr)

if num + Sqr > 100:
    print("Your value is higher than 100")

if num + Sqr == 100:
    print("Your value is equivalent to 100")

if num + Sqr != 100:
    print("Your value is not equivalent to 100")

if num + Sqr < 100:
    print("Your value is less than 100")