import random


options: list = ["R","P","S"]

while True:
    while True:
        user_choice = input("""
                            Select any of the following:
                            "R" for "rock", 
                            "P" for "paper", 
                            "S" for "scissors".
                            """).upper()
        if user_choice not in options:
            print("Invalid Input!!")
        else:
            break
        
    computer_choice = random.choice(options)

    print(f"Player ({user_choice}) : CPU ({computer_choice})")

    if computer_choice == user_choice:
        pass
    elif user_choice == "R" and computer_choice == "P":
        print("Computer wins")
        break
    elif user_choice == "P" and computer_choice == "R":
        print("User wins")
        break
    elif user_choice == "R" and computer_choice == "S":
        print("User Wins")
        break
    elif user_choice == "S" and computer_choice == "R":
        print("Computer Wins")    
        break
    elif user_choice == "P" and computer_choice == "S":
        print("Computer Wins")
        break
    elif user_choice == "S" and computer_choice == "P":
        print("User Wins")
        break
        
