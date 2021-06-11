import random
import time


# useful lists for decisions
signs = [1,2,3,4,5,6]
bat_bowl = ['Bat', 'Bowl']


# User class for user object
class User:
    def __init__(self,name):
        self.name = name
        self.runs = 0
    
    def hit(self,run):
        self.runs = self.runs + run

    def throw(self):
        return random.randint(0,6)
    
    def set_status(self, stat):
        self.stat = stat
    
    def get_status(self):
        return self.stat


# Computer class for comp object
class Computer:
    def __init__(self):
        self.name = 'Computer'
        self.runs = 0

    def hit(self,run):
        self.runs = self.runs + run

    def throw(self):
        return random.randint(0,6)
    
    def set_status(self, stat):
        self.stat = stat
    
    def get_status(self):
        return self.stat


# function for toss decision
def toss_coin():
    choices = ['Heads', 'Tails']
    random.shuffle(choices)
    return choices[0]


# Inform Computer's choice if it wins the toss
def announce():
    random.shuffle(bat_bowl)
    user_obj.set_status(bat_bowl[0])
    comp_obj.set_status(bat_bowl[1])
    print('Computer chose to {} first, {} will have to {} first.'.format(comp_obj.get_status(), playerName, user_obj.get_status()))


# particular bowl
def rollout():
    throw_user = user_obj.throw()
    throw_comp = comp_obj.throw()
    time.sleep(2)
    return [throw_user, throw_comp]


# Game welcome
print("Welcome to CricWar!")


# Initialisation of players
playerName = input("Enter your name: ")
user_obj = User(playerName)
comp_obj = Computer()

# toss event
toss = input("It's time for the toss, what is your call 'Heads' or 'Tails'? ")
if(toss == 'Heads' or toss == 'Tails'):
    toss_result = toss_coin()
    print('{} it is!'.format(toss_result))
else:
    print('Inavlid Choice')
    exit()

if(toss == toss_result):
    inning = input("It is {}'s choice to choose to either Bat or Bowl first: ".format(playerName))
    if inning == 'Bat' or inning == 'Bowl':
        if inning == 'Bat':
            user_obj.set_status('Bat') 
            comp_obj.set_status('Bowl')
        else:
            user_obj.set_status('Bowl') 
            comp_obj.set_status('Bat')
        print('{} chose to {} first, Computer will have to {} first.'.format(playerName, user_obj.get_status(), comp_obj.get_status()))
    else:
        print('Invalid Choice')
        exit()
else:
    announce()

# Game starts
print('Let us start playing....')

# first inning
while True:
    dice = rollout()
    if dice[0] == dice[1]:
        print('Out!')
        if user_obj.get_status() == 'Bat':
            print('{} scored {} run(s), Target for Computer: {} run(s).'.format(playerName, user_obj.runs, user_obj.runs + 1))
        else:
            print('Computer scored {} run(s), Target for {}: {} run(s).'.format(comp_obj.runs, playerName, comp_obj.runs + 1))
        break
    else:
        if user_obj.get_status() == 'Bat':
            user_obj.hit(dice[0])
            print('{} run(s)!'.format(dice[0]))
        else:
            comp_obj.hit(dice[1])
            print('{} run(s)!'.format(dice[1]))

# Break
print('Time for a Short Break, we will resume shortly!!')
time.sleep(5)
print('Second Inning begins')


# Second Inning
while True:
    if user_obj.get_status() == 'Bat' and comp_obj.runs > user_obj.runs:
            print('Computer wins!!')
            break
    elif user_obj.get_status() == 'Bowl' and comp_obj.runs < user_obj.runs:
            print('{} wins!!'.format(user_obj.name))
            break

    thread = rollout()

    if thread[0] == thread[1]:
        print('Out!')
        if user_obj.get_status() == 'Bat':
            if comp_obj.runs < user_obj.runs:
                print('{} wins!!'.format(user_obj.name))
            elif comp_obj.runs == user_obj.runs:
                print('It is a tie')
            else:
                print('Computer wins!')
        else:
            if comp_obj.runs > user_obj.runs:
                print('Computer wins!!')
            elif comp_obj.runs == user_obj.runs:
                print('It is a tie')
            else:
                print('{} wins!'.format(user_obj.name))
        break
    else:
        if user_obj.get_status() == 'Bat':
            comp_obj.hit(thread[1])
            print('{} run(s)!'.format(thread[1]))
        else:
            user_obj.hit(thread[0])
            print('{} run(s)!'.format(thread[0]))

# End of the game