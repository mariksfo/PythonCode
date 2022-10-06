import random


# x = random.randint(1,150)

# print(x)


choices = [
    'Ben',
    'Alex',
    'Melissa',
    'nia',
    'minju',
    'yuna'
]

places = [
    'hotel',
    'bar',
    'stadium',
    'moive theater',
    'ice cream parlor'
]

people = random.choices(choices, k=2)

print(people)

place = random.choice(places)

print(place)

print("{} went to the {} with {}".format(people[0], place, people[1]))

random.shuffle(places)
print(places)