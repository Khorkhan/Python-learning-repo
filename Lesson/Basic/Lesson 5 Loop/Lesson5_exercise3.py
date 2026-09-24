# Number guessing game. Have the player guess the secret number 42 ultil they get it right,
# then display how many attempts it took.

secret = 42
tries = 0
while True:
    guess = int(input("Guess the number(1-100): "))
    tries += 1
    if guess == secret:
        print(f"Corret! Guessed {tries} times")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")