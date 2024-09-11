

from random import randint

game = "Y"

while game.upper() == "Y":
    player_one_roll = randint(1,6)
    player_two_roll = randint(1,6)


    if-player_one_roll> player_two_roll:
        print(f"spelare ett vinner med rullet: {player_one_roll}")
    elif player_two_roll > player_one_roll:
        print(f"spelare two vinner med rullet: {player_two_roll}")
    else:
        print(f"ingen spelare vinner det är oavgjort med rullet:{player_one_roll}")



    game=input("vill du spela igen[Y/N] ")
