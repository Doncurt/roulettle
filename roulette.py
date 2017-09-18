import random
#These three variables denote user input for the gambling game
bank_account=1000
bet_amount=0
bet_color=None
bet_number=0
#represents the double zero on the american standard roullete board
green=[0,37]
#black and red arrays are used to denote the patter on an american roullette board
black=[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
red =[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
'''
Takes the user defined values for the user betting amount 
@params string color int number int ammount
@return array
'''
def take_bet(color,number, amount):

    bet_color = color
    bet_number=number
    bet_amount = amount
    return bet [color,number,amount]


'''
returns random number betweeen 0 and 37. based on the pre defined array values
@params None
@return int result
'''
def roll_ball():

    pass
'''
check to see if player bet is correct compare with bet_number to number_rolled) must be defined
@params
@return
'''
def check_results():

    pass
'''
Returns total amount won or lost by user based on results
@params
@return

'''
def payout():

    pass
'''


'''

def play_game():
    pass
