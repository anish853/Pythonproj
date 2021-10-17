import random
user_wins=0
computer_wins=0
options = ["rock","paper","scissors"]
while True:
    user_input=input("Type Rock,Paper,Scissors or Q to quit.").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue
    random_number = random.randint(0,2)
    computer_input=options[random_number]
    print("computer pick=",computer_input)

    if user_input == "rock" and computer_input == "scissors":
        print("u won")
        user_wins=user_wins+1

    elif user_input == "scissors" and computer_input == "rock":
        print("u loss")
        computer_wins=computer_wins+1

    elif user_input == "rock" and computer_input == "paper":
        print("u loss")
        computer_wins=computer_wins+1

    elif user_input == "paper" and computer_input == "rock":
        print("u won")
        user_wins=user_wins+1

    elif user_input == "paper" and computer_input == "scissors":
        print("u loss")
        computer_wins=computer_wins+1

    elif user_input == "scissors" and computer_input == "paper":
        print("u won")
        user_wins=user_wins+1

    elif user_input == computer_input:
        print("DRAW")


    else:
        print("print a valid choice")


print("user points:", user_wins)
print("PC points:", computer_wins)
print("BYEE")






