print("Think of a number between 1 and 100")
input("Press Enter when you're ready")

low = 1
high = 100
attempts = 0

while True:
    guess = (low + high) // 2
    print(f"My guess is: {guess}")
    attempts += 1

    feedback = input(
        "Is it too high (h), too low (l), or correct (c)? "
    ).lower()
    

    if feedback == "h":
        high = guess - 1
    elif feedback == "l":
        low = guess + 1
    elif feedback == "c":
        print(f"Yaaaaay! I guessed your number in {attempts} attempts!")
        break
    else:
        print("Please enter only h, l, or c.")