import random


def game():
    secret = generate_number()
    attempts = 0
    while True:
        print("Enter 0 to stop game, or your guess (4 digit number): ")
        user_input = input("")
        if user_input == "0":
            return
        if not user_input.isdigit() or len(user_input) != 4:
            if user_input == "secret":
                print(secret)
                continue
            print("Wrong input, try again")
            continue
        attempts += 1
        bulls, cows = guess_attempt(secret, user_input)
        if bulls == 4:
            win(secret, attempts)
            return
        print(f"{bulls}A{cows}B")


def guess_attempt(secret, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] in secret:
            if secret.index(guess[i]) == i:
                bulls += 1
            else:
                cows += 1
    return bulls, cows


def generate_number():
    return str(random.randint(1000, 9999))


def win(secret, attempts):
    print(f"You won!\nSecret number was: {secret}\nThe number of attempts: {attempts}")


game()
