# import random
#
# random.seed(45)
# rng = list(range(1, 100, 5))
# print(rng)
#
# rng.append(1_000)
# print(rng)
#
# rng.append([2, 3, 4])
# print(rng)
#
# rng.extend([2, 3, 4])
# print(rng)
#
# rng += [1, 2, 3]
# print(rng)
#
# rng.insert(0, 99)
# print(rng)
#
# popped = rng.pop(2)
# print(popped)
# print(rng)
#
# rng.remove(41)
# print(rng)
#
# rng.clear()
# print(rng)
#
# random.shuffle(rng)
# print(rng)
# print(random.choice(rng))
#
# fruits = {"Apple", "Mango", "Banana", "Cucumber", "Cherry", "Pineapple"}
# fruits.sort(key=len)
# print(fruits)

# {{()}}

# lst = [1, 2, 3, 4, 5, 8]
# print(any(True if i <= 7 else False for i in lst))
#
# print(all(True if i >= 7 else False for i in lst))
#
# print(max(["I", "Love", "Love"], key = len))

# l1 = [1, 2, 3, 4]
# l2 = [5, 6, 7, 8, 9]
# print(list(zip(l1, l2)))
#
# # print(list(zip(l1, l2, strict = True)))
#
# list_of_dict = [{"Name:" "Asake", "Gender:" "F"}, {"Name:" "Boyo", "Gender:" "M"}]
#
# mapped_list_of_dict = list(
#     map(lambda x: ("Mr. " if x["Gender"] == "M" else "Mrs. ") - x["name"], list_of_dict)
# )
# print(mapped_list_of_dict)
# print([("Mr. " if x["Gender"] == "M" else "Mrs. ") + x["name"] for x in list_of_dict])


 
