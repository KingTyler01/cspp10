import random
def rolldice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = dice1 + dice2
    print(dice3)
    return dice3



def get_bet(): 
    player_money = 100
    bet = 0
    while True:
        bet = int(input("How much would you like to bet? "))
        if  bet > player_money:
            print("You can not bet more than you have in your bank.")
        else:
            print("That is a valid bet")
            return bet

def get_range(dice3):
    if dice3 > 7:
        print("Over 7")
        return "Over 7"
    elif dice3 < 7:
        print( "Under 7")
        return "Under 7"
    else:
        print("7")
        return "7"
rolldice()
        

    

rolldice()
rnge = get_range(dice3)
    
        





    
