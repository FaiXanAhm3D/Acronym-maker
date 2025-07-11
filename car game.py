command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started")
    elif command == "stop":
        if not started:
            print("Car is already stopped you dumb!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("kya coder banega re tu !!!")
        print('''
start - to start the car
stop - to stop the car
quit - to quit
''')
    elif command == "quit":
        print("Get the hell out of here")
        break
else:
    print("Sorry we didn't understand that")
    
