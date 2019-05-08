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

def deepcopy (list):
    l=[]
    for x in list:
        l.append(x)
    return l

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
    
def strat_4(batch, winnings):
    first_draw=draw(batch)
    if first_draw==draw(batch):
        guess=first_draw
    else:
        guess=draw(batch)
    if guess==draw(batch):
        return winnings
    else:
        return 0
        
def strat_5(batch, winnings):
    total=deepcopy(batch)
    remaining=batch
    first_draw=draw(batch)
    remaining.remove(first_draw)
    second_draw=draw(remaining)
    remaining.remove(second_draw)
    if first_draw==second_draw:
        guess=first_draw
    else:
        guess=draw(remaining)
    if guess==draw(total):
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
    earned4=0
    earned5=0
    for a in range(intensity):
        marbles = gen_marbles(N)
        earned1 += run_rounds(1, marbles, strat_1)[1]
        earned2 += run_rounds(1, marbles, strat_2)[1]
        earned3 += run_rounds(1, marbles, strat_3)[1]
        earned4 += run_rounds(1, marbles, strat_4)[1]
        earned5 += run_rounds(1, marbles, strat_5)[1]
    print('''In {0} rounds: 
        Strategy 1 earned {1} per round. 
        Strategy 2 earned {2} per round.
        Strategy 3 earned {3} per round.
        Strategy 4 earned {4} per round.
        Strategy 5 earned {5} per round.'''.format(intensity, earned1/intensity, earned2/intensity, earned3/intensity, earned4/intensity, earned5/intensity))
    
find_winnings(1000)
