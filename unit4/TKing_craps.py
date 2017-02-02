import random

def instructions():
    instructions= input("Do you know how to play craps:[Y]/[N]: ")
    if instructions == "N":
        print("--------------------------------")
        print("First the Player places a bet")
        print("-----------------------------------------------------------------------------------")
        print("When the first pair of dice are rolled, a few outcomes can happen based on the sum:")
        print("-----------------------------------------------------------------------------------")
        print("If the player rolls a 2, 3, or 12 in this phase, they lose their bet, and the round ends")
        print("If the player rolls a 7 or 11 in this phase, they win their bet, and the round ends")
        print("If the player rolls any other number ( 4,5,6,8,9,10), then they continue to Phase 3, with their roll becoming their \"point number\" ")
        print("If the player reaches Phase 3, which most rounds they do, then they keep rolling die until they roll a 7 or they roll their point number.")
        print("-----------------------------------------------------------------------------------")
        print("If the player rolls their point number first, they win their bet, and the round ends.")
        print("If the player rolls a 7 first, they lose their bet, and the round ends.")
        print("If the player rolls any other number, they keep rolling in Phase 3.")
        print("-----------------------------------------------------------------------------------")
        print("You start out with $100")
        print("--------------------------------")
    else:
        print("-------------")
        print("Lets Play!!")
        print("-------------")
        print("You start out with $100")
        print("-------------------------")
            

    
def rolldice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = dice1 + dice2
    print("Rolled two dice [{}] and [{}] the sum is [{}]".format(dice1,dice2,dice3))
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

def check_first_roll(dice3):
    while True:
        if dice3 == 2 or dice3 == 3 or dice3 == 12:
            print ("You lost the roll.")
            return ("loss")
        elif dice3 == 7 or dice3 == 11:
            print ("You won the roll.")
            return ("win")
        else:
            print ("Your point number is {}.".format(dice3))
            return (dice3)
            
        roll = 0
        if roll == dice3:
            print("You won the roll.")
            return ("win")
        elif roll == 7:
            print("You lost the roll")
        return ("loss")
    else:
        print("You didn't win or lose. Reroll!")
        return roll
    
    
    


    
def check_point_number(dice3):
    roll = dice3
    while True:
        new_roll = rolldice()
        if roll == new_roll:
            print("You won the roll.")
            return ("win")
        elif new_roll == 7:
            print("You lost the roll")
            return ("loss")
        else:
            print("You didn't win or lose. Reroll!")


    
         
        
        
        
    

def main():
    print("Welcome to Craps!!")
    instructions()
    player_money = 100
    get_bet()
    bet = get_bet()
    dice = rolldice()
    check_first_roll(dice)
    check_point_number(dice)
    new_money = player_money + bet
    nw_money = player_money - bet
    if check_point_number(dice) =="win":
        print("You now have ${}".format(new_money))
    else:
        print("You now have ${}".format(nw_money))
main()
