from random import randint, choice

N=10 #number of marbles
W=10 #money you receive if you win

def gen_marbles(n):
    global red_marbles, green_marbles
    marbles=[]
    red_marbles=randint(0,n)
    green_marbles=n-red_marbles
    for x in range(red_marbles):
        marbles.append('red')
    for x in range(green_marbles):
        marbles.append('green')
    return marbles
    
def draw(l):
    return choice(l)

def strat_1(batch, winnings):
    if draw(batch) == 'red':
        return winnings
    else:
        return 0
        
def strat_2(batch, winnings):
    if draw(batch) == 'green':
        return winnings
    else:
        return 0
        
def strat_3(batch, winnings):
    guess=draw(batch)
    if draw(batch)==guess:
        return winnings
    else:
        return 0
        
def run_rounds(num, batch, strat):
    winnings=0
    for x in range(num):
        winnings+=strat(batch, W)
    return ([num, winnings])

def find_winnings(intensity):
    earned1=0
    earned2=0
    earned3=0
    for a in range(intensity):
        marbles = gen_marbles(N)
        earned1 += run_rounds(1, marbles, strat_1)[1]
        earned2 += run_rounds(1, marbles, strat_2)[1]
        earned3 += run_rounds(1, marbles, strat_3)[1]
    print('''In {0} rounds: 
        Strategy 1 earned {1} per round. 
        Strategy 2 earned {2} per round.
        Strategy 3 earned {3} per round.'''.format(intensity, earned1/intensity, earned2/intensity, earned3/intensity))
    
find_winnings(10000)