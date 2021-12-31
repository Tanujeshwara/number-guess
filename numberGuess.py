import random
print("Number Guessing Game")

number = random.randint(1,9)

chances=0

print("Guess a number between 1 and 9")

while chances<5:
    guess=int(input("Enter the number :"))

    if guess==number:
        print("THAT WAS A GREAT GUESS")

    elif guess<number:
        print("Your guess was too less : Guess a higher number")

    else:
        print("Your guess was too high : Guess a lower number")


chances +=1

if not chances<5 :
    print("Better luck next time!! The number is ", number)


