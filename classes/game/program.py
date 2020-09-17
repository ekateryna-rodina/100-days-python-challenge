import pandas as pd
import random
from actors import User, Computer

def main():
    showHeader()
    gameLoop()
    

def showHeader():
    print()
    print('--------------------------------- Rock Paper Scissors ---------------------------------')
    print('                                    Game is started')
    print()

def gameLoop():
    win_score = 3
    battleTable = pd.read_csv('https://raw.githubusercontent.com/talkpython/100daysofcode-with-python-course/master/days/13-15-text-games/data/battle-table.csv')
    battleTable = battleTable.set_index('Attacker')

    # create a computer player object
    defender = Computer('PyGame') 

    # create an user player object
    print(f'My name is {defender.name}. What is your name?')
    player_name = input()
    attacker = User(player_name)

    while True:
        # ask user for a choice
        attacker.make_achoice()
        defender.make_achoice()
  
        # what is the result of the round
        round_result = battleTable.loc[attacker.round_choice.name, defender.round_choice.name]

        assert round_result in ('win', 'lose', 'draw')
        
        # finalize round's result for both players
        attacker.finalize_round(defender.round_choice, round_result)
        defender.finalize_round(round_result)

        # print a round result
        print(f'{attacker.round_choice.name} {round_result} to {defender.round_choice.name}')

        # check game result
        if attacker.score == win_score:
            print('You won!')
            return
        elif defender.score == win_score:
            print('We are sorry for your loss!')
            print('The game is over')
            return
        

# if '__name__' == '__main__':
#     main()
main()