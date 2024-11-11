import random
import time

tries = 0

random_number = random.randint (1, 1000)

while True:
    tries = tries + 1
    guess = int(input("Guess the number between 1 and 1000 "))
  
    if guess < random_number:
        print("Too low, try again ")
    if guess > random_number:
        print("Too high, try again")
    if guess == random_number:
        print(f"Good job, the number was {random_number} and you guessed in {tries} tries, restart program to try again")
        break
time.sleep(5)