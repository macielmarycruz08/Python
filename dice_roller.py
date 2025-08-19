import random

dice_rolls = [1, 2, 3, 4, 5, 6]

dice = random.choice(dice_rolls)

print(dice)
if dice == 1:
    print("You are orange!")
elif dice == 2:
    print("You are yellow!")
elif dice == 3:
    print("You are pink!")
elif dice == 4:
    print("You are purple!")
elif dice == 5:
    print("You are red!")
elif dice == 6:
    print("You are blue!")
