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
        
def run_rounds(num, batch, strat):
    winnings=0
    for x in range(num):
        winnings+=strat(batch, W)
    print('In {0} rounds, '.format(num)+str(strat)+' made {0} dollars.'.format(winnings)) 
    return ([num, winnings])

marbles = gen_marbles(N)
run_rounds(100, marbles, strat_1)