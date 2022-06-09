# for num in range(1, 101):
#     if not num % 15:
#         print("FIZZBUZZ")
#     elif not num % 3:
#         print("BUZZ")
#     elif not num % 5:
#         print("BUZZ")
#     else:
#         print(num)
#


for num in range(1, 101):
    if num % 15 == 0:
        print("FIZZBUZZ")
    elif num % 3 == 0:
        print("BUZZ")
    elif num % 5 == 0:
        print("BUZZ")
    else:
        print(num)