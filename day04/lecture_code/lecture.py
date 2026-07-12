#import random
from random import choice, randint, shuffle

# result = random.choice(["max", "Max"])
result = choice(["max", "Max"])
number = randint(1, 10)

cards = ["Ace", "Jack", "Queen", "King"]

shuffle(cards)

print(result)
print(number)

print("Cards Order:")
for card in cards:
    print(card)
