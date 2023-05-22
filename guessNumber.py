import random

number = random.randint(1,100)
start = 1
end = 100
num_guesses = 0

print("=======================================")
print(f"debug => the random number is {number}")
print("=======================================")
print("")
while True:
    guess = int(input(f"Guess a number between {start} to {end}: "))
    num_guesses += 1

    if guess == number:
        print("you guess the right number")
        break
    elif guess < number:
        start = guess
        print("too loo, try again")
    else:
        end = guess
        print("too high, try again")

