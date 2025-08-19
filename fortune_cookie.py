import random

fortune_quotes = ["you are poor", "you are rich", "you are super smart"]

welcome = "Hoped you enjoyed your meal, this is your fortune: "
fortune = random.choice(fortune_quotes)

print(welcome)
print(fortune)
