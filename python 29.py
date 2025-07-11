import random
lucky = random.randint(1,100)
chances = 5
while chances >= 1:
    guess = input("Enter your guess : ")
    if guess.lower() == "authorized_answer":
        print("The lucky number is ",lucky)
        process=input("Do you want to 'QUIT' or 'CONTINUE' ? : ")
        if process.lower() == "quit":
            break
        elif process.lower() == "continue":
            chances=2
            continue
    elif int(guess)==lucky:
        print("Guess is correct!")
        break
    elif int(guess)<lucky:
        print("Low")
    else:
        print("High")
    chances-=1
else:
    print("Game over!! lucky number is", lucky)
