# def twoSum(list_of_number: list, target: int) -> list:
#     for i in range(len(list_of_number) - 1):
#         for j in range (i + 1, len(list_of_number)):
#             res = list_of_number[i] + list_of_number[j]
#             if target == res:
#                 return [i, j]
#
#     return []
#
# print(twoSum([1, 3, -8, 5, 3], 8))


def two_sum(list_of_numbers, list, target: int) -> list | int:
    map = {}
    for i in range(len(list_of_numbers)):
        compliment = target - list_of_numbers[i]

        if compliment in map:
            return [map[compliment], i]
        else:
            map[list_of_numbers[i]] = i

    return -1

print(two_sum([6, -1, 3, 0, -8, 5, 3], 6))
