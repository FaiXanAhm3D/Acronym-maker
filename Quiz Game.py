#project: 1
#Quiz game
print("Lets play quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
else :
    print("Okay! let's play :)")

q = input("What does CPU stand for? ")

if q.lower() == "central processing unit":
    print("You got that right!")
else :
    print("Incorrect !")

q2 = input("Main parts of cpu ? ")

if q2.lower() == "cu and alu":
    print("Correct")
else:
    print("Incorrect")

q3 = input("What does ROM stands for ? ")

if q3.lower() == "read only memory":
    print("Correct")
else:
    print("Incorrect")
