import random
guesses = 0

name = input("What is your name? ")
print("Hello! " + name + ", are you ready to play?" )
number = random.randint(1, 50)

print("Ok " + name + ", I am thinking of a number between 1 and 50, take a guess, you have 7 chances.")

while guesses < 7:
    print("Take a guess:") 
    guess = input()
    guess = int(guess)

    guesses = guesses + 1

    if guess < number:
        print("Too low")

    if guess > number:
        print("Too high.")

    if guess == number:
        break

if guess == number:
    guesses = str(guesses)
    print("Congratulations, " + name + "! You guessed the number in " + guesses + " guesses!")

if guess != number:
    number = str(number)
    print("Sorry " + name + " The number I was thinking of was " + number)
