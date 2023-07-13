import random

def roll_dice():
    min_value = 1
    max_value = 6
    return random.randint(min_value,max_value)

while True:
    players_number = input("Enter the number of players (2-4): ")
    if players_number.isdigit():
        players_number = int(players_number)
        if 2<= players_number <= 4:
            break
        else:
            print("The players number must be between 2 and 4. Try again... ")
    else:
        print("Invalid, try again... ")

max_score = 50
player_scores = [0 for _ in range(players_number)]

print(player_scores)

while(max(player_scores) < max_score):
    for i in range(players_number):
        print(f"Player {i +1} turn has started.")
        print(f"Your total score is: {player_scores[i]}")
        current_score = 0
        while True:
            wanna_roll = input("Do you want to roll the dice? (y): ")
            if wanna_roll.lower() != 'y':
                break
            value = roll_dice()
            if value == 1:
                current_score=0
                print("You rolled a 1, your turn is done!")
                break
            else:
                current_score += value 
                print(f"You rolled a {value}. \nYour current score is {current_score}.")
        
        player_scores[i] += current_score
        print(f"Total score: {player_scores[i]}") 

winning_score = max(player_scores)
winning_index = player_scores.index(winning_score) + 1
print(f"Player {winning_index} is the winer with the total score of: {winning_score}")  