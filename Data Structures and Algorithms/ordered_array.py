import random

randomList = []

for i in range(10):
    random_integer = random.randint(0, 9)
    randomList.append(random_integer)

print(randomList)
