

from random import randint
import math




player_name_one= input("vad heter du spelare ett")
player_name_two = input("vad heter du spelare två")


rounds_changer= input ("hur många rundor vill ni sköra") 

win_need= math.ceil(int(rounds_changer)/2) 

t=input("hur många sidor vi du köra med") 




dice= 1,math.ceil(int(t))

game = "Y"

player_one_point=0
player_two_point=0 
rounds=0   




while game.upper() == "Y":
    rounds +=1 
    player_one_roll = randint(dice)
    player_two_roll = randint(dice)


    if-player_one_roll> player_two_roll:
        print(f"{player_name_one } vinner med rullet: {player_one_roll}")
        player_one_point +=1
    elif player_two_roll > player_one_roll:
        print(f"{player_name_two} vinner med rullet: {player_two_roll}")
        player_two_point +=1
    else:
        print(f"ingen spelare vinner det är oavgjort med rullet:{player_one_roll}")
    
    if player_one_point == win_need +1 :
        print(f"{player_name_one} har vunit")
        game=input("vill du spela igen[Y/N] ")
        player_one_point = 0 
        player_two_point = 0 
    

    elif player_two_point == win_need +1 :
        print(f"{player_name_two} har vunit")
        game=input("vill du spela igen[Y/N] ")
        player_one_point = 0
        player_two_point = 0
        
    elif rounds == rounds_changer :
        print("oavgjor inga spelare van :(")
        game=input("vill du spela igen [Y/N]")
        player_one_point = 0
        player_two_point = 0