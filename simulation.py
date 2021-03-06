#CLICK "GO" FOR EASIEST RUN OF SIMULATION

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
        
def run_rounds(num, size, strat):
    winnings=0
    for x in range(num):
        batch=gen_marbles(size)
        winnings+=strat(batch, W)
    return ([num, winnings])

def find_winnings(intensity, s1, s2, s3, s4, s5):
    earned1=0
    earned2=0
    earned3=0
    earned4=0
    earned5=0
    for a in range(intensity):
        if s1==True:
            earned1 += run_rounds(1, N, strat_1)[1]
        if s2==True:
            earned2 += run_rounds(1, N, strat_2)[1]
        if s3==True:
            earned3 += run_rounds(1, N, strat_3)[1]
        if s4==True:
            earned4 += run_rounds(1, N, strat_4)[1]
        if s5==True:
            earned5 += run_rounds(1, N, strat_5)[1]
    rep='''In {0} rounds: 
        '''.format(intensity)
    if s1==True:
        rep+='''Strategy 1 earned {0} per round. 
        '''.format(earned1/intensity)
    if s2==True:
        rep+='''Strategy 2 earned {0} per round.
        '''.format(earned2/intensity)
    if s3==True:
        rep+='''Strategy 3 earned {0} per round.
        '''.format(earned3/intensity)
    if s4==True:
        rep+='''Strategy 4 earned {0} per round.
        '''.format(earned4/intensity)
    if s5==True:
        rep+='''Strategy 5 earned {0} per round.'''.format(earned5/intensity)
    print(rep)
    
def str_to_bool(s):
    if s=='y' or s=='Y':
        return True
    else:
        return False

running=True
while running==True:
    direc=input('Press ENTER without typing to exit. Type D to find D. Type P to find P. Type R to find R, type S to find S, and type anything else to run general simulation. ')
    if direc=='':
        running=False
    elif direc=='D':
        length=input('How many rounds to find D? Enter a number like 1 or 100. ')
        D_1=run_rounds(int(length), N,strat_1)
        D_2=run_rounds(int(length), N,strat_2)
        print('D='+str((D_1[1]+D_2[1])/(D_1[0]+D_2[0])))
    elif direc=='P':
        length=input('How many rounds to find P? Enter a number like 1 or 100. ')
        D_1=run_rounds(int(length), N,strat_1)
        D_2=run_rounds(int(length), N,strat_2)
        D=(D_1[1]+D_2[1])/(D_1[0]+D_2[0])
        P_1=run_rounds(int(length), N,strat_3)
        PD=P_1[1]/P_1[0]
        print('P='+str(PD-D))
    elif direc=='R':
        length=input('How many rounds to find R? Enter a number like 1 or 100. ')
        D_1=run_rounds(int(length), N,strat_1)
        D_2=run_rounds(int(length), N,strat_2)
        D=(D_1[1]+D_2[1])/(D_1[0]+D_2[0])
        R_1=run_rounds(int(length), N,strat_4)
        RD=R_1[1]/R_1[0]
        print('R='+str(RD-D))
    elif direc=='S':
        length=input('How many rounds to find P? Enter a number like 1 or 100. ')
        D_1=run_rounds(int(length), N,strat_1)
        D_2=run_rounds(int(length), N,strat_2)
        D=(D_1[1]+D_2[1])/(D_1[0]+D_2[0])
        S_1=run_rounds(int(length), N,strat_5)
        SD=S_1[1]/S_1[0]
        print('S='+str(SD-D))
    else:
        s1_direc=str_to_bool(input('Include strategy 1 in simulation? Enter "Y" or "y" without quotes for yes. '))
        s2_direc=str_to_bool(input('Include strategy 2 in simulation? Enter "Y" or "y" without quotes for yes. '))
        s3_direc=str_to_bool(input('Include strategy 3 in simulation? Same directions apply. '))
        s4_direc=str_to_bool(input('Include strategy 4 in simulation? '))
        s5_direc=str_to_bool(input('Include strategy 5 in simulation? '))
        length=input('How many rounds? Enter a number like 1 or 100. ')
        find_winnings(int(length),s1_direc, s2_direc, s3_direc, s4_direc, s5_direc)
        
        