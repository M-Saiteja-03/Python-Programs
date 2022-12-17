#map()

my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = list(map(str.upper, my_pets))
print(uppered_pets)

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, circle_areas, range(1,7)))
print(result)

#reduce()

from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]
print("working of reduce()")
def custom_sum(first, second):
    print(first, second)
    return first + second

result = reduce(custom_sum, numbers)
print("final result:",result)
