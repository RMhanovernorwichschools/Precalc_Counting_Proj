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
    marble=draw(batch)
    if marble == 'red':
        return winnings
    else:
        return 0
        
def strat_2(batch, winnings):
    marble=draw(batch)
    if marble == 'green':
        return winnings
    else:
        return 0
        
def run_rounds(num, batch, strat):
    winnings=0
    for x in range(num):
        winnings+=strat(batch, W)
    return ([num, winnings])

def find_D(intensity):
    for a in range(intensity):
        marbles = gen_marbles(N)
        earned1 = run_rounds(intensity, marbles, strat_1)[1]
        earned2 = run_rounds(intensity, marbles, strat_2)[1]
        print('In 