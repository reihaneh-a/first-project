import random

def guessNumber():

    number_to_guess = random.randint(1, 100)
    with open("pass.txt","w") as f:
        f.write(str(number_to_guess))
    attempts = 0
    max_attempts = 6
    print(" welcome to Guessing number between 1 and 100")


    while attempts < max_attempts:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < number_to_guess:
            print("low number from  guess number")

        elif guess > number_to_guess:
            print("high number from  guess number")

        else:
            print(f"correct number {number_to_guess} in{attempts} attempts.")
            break

    if guess != number_to_guess:
     print(f"sorry looser! the number was {number_to_guess}")

if __name__ == "__main__":
    guessNumber()


