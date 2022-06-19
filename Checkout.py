# lst = [i for i in range(1, 11)]
# print(lst)

#
# x = "even" if 3 % 2 == 0 else "odd"
# print(x)


# lst = [int(input("Enter student's score: ")) for i in range(1, 11)]
# print(lst)
# print("Total scores = ", sum(lst))
# print("Max = ", max(lst))
# print("Min = ", min(lst))
# print("Average = ", sum(lst) / len(lst))
import math
def is_prime(num: int) -> bool:
    max_divisor = math.ceil(math.sqrt(num)) + 1
    for i in range(2, max_divisor):
        if num % i == 0:
            return False

    return True
# prime = int(input("Enter a number -> "))
# print(is_prime(prime))
#
# primes = (i for i in range(1, 10_000_000) if is_prime(i))
# print(type(primes))

# def cube(num: int) -> int:
#     return num ** 3
#
# cubes = [cube(i) for i in range(1, 11)]
# print(cubes)

#dict

primes = {k: v for k, v in enumerate(range(1, 10)) if is_prime(v)}
print(type(primes))
print(primes)