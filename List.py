def twoSum(list_of_number: list, target: int) -> list:
    for i in range(len(list_of_number) - 1):
        for j in range (i + 1, len(list_of_number)):
            res = list_of_number[i] + list_of_number[j]
            if target == res:
                return [i, j]

    return []

print(twoSum([1, 3, -8, 5, 3], 8))
