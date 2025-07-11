secret_number = 7
i=3
i_limit = 0
while i>i_limit:
    print(f"You have {i} chance")
    guess = int(input("Guess the number: "))
    i -= 1
    if guess == secret_number:
        print("You got it right !")
        break
else:
    print("You failed XO")

