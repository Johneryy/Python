def count_sheep(cs):
    sheep = ""
    for i in range(1, cs + 1):
        sheep += str(i) + " sheep..."
    return sheep

Sheep = int(input("Enter a number-> "))
print(count_sheep(Sheep))