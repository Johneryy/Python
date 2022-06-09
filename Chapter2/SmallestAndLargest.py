num1 = int(input("Enter First Number -> "))
num2 = int(input("Enter Second Number -> "))
num3 = int(input("Enter Third Number -> "))

Total = num1 + num2 + num3
Product = num1 * num2 * num3
Average = Total/2


if Total:
    print("Sum -> ", Total)

if Product:
    print("Product ->", Product)

if Average:
    print("Average -> ", Average)
