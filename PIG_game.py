import random

temp = 0 
user1_total = 0 
user2_total = 0 
user1_turn = True

options = ["r", "e", "q"]

while user1_total or user2_total <= 50: 
    roll = input("Type 'r' to role the dice/type 'e' to end your turn/type 'q' to quit: ").lower()
    
    if roll not in options:
        print("Invalid, try again")
        continue
    if roll == "r":
        this_roll = random.randint(1,6)
        if this_roll == 1:
            print("You rolled a 1. Your turn is over and all the points from this turn is gone.")
            temp = 0 
            print(temp)
            print("End of turn.")
            if user1_turn == True:
                user1_total = temp + user1_total
                print(f"Player 1 total score: {user1_total}")
                user1_turn = False
                temp = 0 
                continue
            else:
                user2_total = temp + user2_total
                print(f"Player 2 total score: {user2_total}")
                user1_turn = True
                temp = 0 
                continue
        else:
            temp = temp + this_roll
            print(this_roll)
            continue
    if roll == "e":
        print("End of turn.")
        if user1_turn == True:
            user1_total = temp + user1_total
            print(f"Player 1 total score: {user1_total}")
            user1_turn = False
            temp = 0 
            continue
        else:
            user2_total = temp + user2_total
            print(f"Player 2 total score: {user2_total}")
            user1_turn = True
            temp = 0 
            continue
    if roll == "q":
        break
else:
    if user1_total >= 50:
        print("Player 1 reached 50 points! Player 1 you win!")
    else:
        print("Player 2 reached 50 points! Player 2 you win!")
