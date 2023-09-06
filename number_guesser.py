from random import randint
correct_guess = False
counter = 0

num = int(input("Pick a number between 1 and 100: "))
if num < 0 or num > 100:
    num = int(input("Please pick a number BETWEEN 0 AND 100: "))


while not correct_guess:
    guess = randint(0, 100)
    if guess == num:
        print(f"The number is {num}! It took {counter} attempt(s)")
        correct_guess = True
    else:
        counter += 1