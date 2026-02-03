from random import randint

secret_number = randint(1 , 100)
attempts = 0


print("Welcome to our number guessing game ")
print("Choose a number between 1 and 100.")

while True : 
    guess = int(input("Your guess:"))
    attempts += 1 

    if guess < secret_number :
        print("It is bigger.")
    elif guess > secret_number : 
        print("It is smaller.")
    else : 
        print("Well done, you won.")
        print("Number of attempts: {attempts}")
        break
