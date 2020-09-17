import random

# Rolls classes
class Roll:
    def __init__(self):
        self.name = ''
class Rock(Roll):
    def __init__(self):
        super().__init__()
        self.name = 'Rock'
class Paper(Roll):
    def __init__(self):
        super().__init__()
        self.name = 'Paper'
class Scissors(Roll):
    def __init__(self):
        super().__init__()
        self.name = 'Scissors'

choices = {
    'r': Rock(),
    'p': Paper(),
    's': Scissors() }

# parent class for user and computer
class Player():
    def __init__(self, name):
        self.name = name
        self.round_choice = None   
        self.score = 0 
    def make_achoice(self):
        pass

# Roles classes
class User(Player):
    # initialize the user
    def __init__(self, name):
        super().__init__(name)
    def make_achoice(self):
        ''' Inputs user's choice '''
        # user input/objects map
        print('Choose the roll: [r]ock, [p]aper, [s]cissors')
        attacker_choice = input()
        self.round_choice = choices[attacker_choice]
        # test
        assert self.round_choice.name in ('Rock', 'Paper', 'Scissors')

    def finalize_round(self, defender_choice, round_result):
        '''Save a score and prints a result
        :params: defender's choice name , round result from a table'''
        # test var
        temp_score = self.score
        # save a score
        if round_result == 'win':
            self.score += 1   
            # test
            assert self.score == temp_score + 1
        
class Computer(Player):
    # initialize the user
    def __init__(self, name):
        super().__init__(name)
    def make_achoice(self):
        ''' Generates computer's choice randomly'''
        # defender choice is randomly generated
        defender_choice = random.choice(list(choices.values()))
        self.round_choice = defender_choice

        # test
        assert defender_choice.name in ('Rock', 'Paper', 'Scissors')
    
    def finalize_round(self, round_result):
        ''' Increases a computer's score if user lost
        :params: round's result'''
        # test var
        temp_score = self.score
        # save a score
        if round_result == 'lose':
            self.score += 1      
            # test
            assert self.score == temp_score + 1