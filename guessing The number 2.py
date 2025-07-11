number = 7
attempts = 0
total_attempts = 3
while attempts<total_attempts:
    a1=int(input("Guess the secret number = "))
    attempts+=1
    if number==a1:
        print("You won")
        break
else:
    print("You lose")
