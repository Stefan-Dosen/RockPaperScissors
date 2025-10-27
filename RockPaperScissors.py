from random import choice

items =["rock","paper","scissors"]
comp_score=0
player_score=0
rounds = int(input("how many rounds would you like to play: "))
for i in range(rounds):
    play = input("rock, paper, scissors: ")
    if play not in items:
        print("Invalid choice!")
        continue
        
    chosen = choice(items)

    wins = {
        "rock":"scissors",
        "scissors":"paper",
        "paper":"rock"
    }

    if play==chosen:
        print("tie")
    elif wins[play]==chosen:
        print(f"{play} beats {chosen}")
        player_score+=1
    else:
        print(f"{play} loses to {chosen}")
        comp_score+=1

print(f"you lost {comp_score} rounds and won {player_score}")