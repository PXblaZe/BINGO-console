# Author's name: Sumit Gupta
# Version: 0.1.21

from time import sleep
from random import randint
from pymysql import connect, cursors

#Variable:--->
getUID = None

#Creating DB & Table:--->
try:
    con = connect(host = 'localhost', user = 'root', password = 'sunbeam')
    csr = con.cursor()
    csr._defer_warnings = True
    csr.execute('CREATE DATABASE IF NOT EXISTS Users')
    csr.execute('USE Users')
    csr.execute('CREATE TABLE IF NOT EXISTS PlrData(UserID varchar(100) NOT NULL PRIMARY KEY, PWD varchar(100),Fname varchar(30), Lname varchar(30), DOB DATE, TMP INTEGER, TMW INTEGER, TML INTEGER, TMD INTEGER, FWR INTEGER, LWR INTEGER, FLR INTEGER, LLR INTEGER, FDR INTEGER, LDR INTEGER, log int(1))')
    con.commit()
finally:
    csr.close()
    con.close()
################################################################################



#Methods:--->
def dply(L1, L2, hw='*', rev=False):
    if rev:
        print('----------------')
        for i in L1:
            print('|', end="")
            if i in L2:
                print(str(i).rjust(2), end='')
            else:
                print(hw.rjust(2), end='')
            if not (L1.index(i) + 1) % 5: print('|\n----------------')
    else:
        print('----------------')
        for i in L1:
            print('|', end="")
            if i in L2:
                print(hw.rjust(2), end='')
            else:
                print(str(i).rjust(2), end='')
            if not (L1.index(i) + 1) % 5: print('|\n----------------')


def login():
    try:
        global getUID
        con = connect(host = 'localhost', user = 'root', password = 'sunbeam')
        csr = con.cursor()
        csr.execute('USE Users')
        csr.execute('SELECT UserID, log FROM PlrData')
        for k in range(csr.rowcount):
            i, j = csr.fetchone()
            if j == 1:
                getUID = i
                return 1
        else:
            return 0
    finally:
        con.close()
    

def logout():
    try:
        con = connect(host = 'localhost', user = 'root', password = 'sunbeam')
        csr = con.cursor()
        csr.execute('USE Users')
        csr.execute('UPDATE PlrData SET log = 0 where log = 1')
    finally:
        con.commit()
        con.close()

def signUp():
    print('\n')
    fn = input('First Name: ')
    ln = input('Last Name: ')
    dob = input('Date of Birth (yyy-mm-dd): ')
    ud = input('User ID: ')
    pwd = input('Password: ')
    cp = ''
    while pwd != cp:
        cp = input('Confirm Password: ')
    try:
        con = connect(host = 'localhost', user = 'root', password = 'sunbeam')
        csr = con.cursor()
        csr.execute('USE Users')
        cmd = 'INSERT INTO PlrData VALUES(\''+ud+'\', \''+pwd+'\', \''+fn+'\', \''+ln+'\', \''+dob+'\''+',0 '*11+')'
        csr.execute(cmd)
    finally:
        con.commit()
        con.close()
    
def signIn():
    try:
        print('\n')
        uid = input('User ID: ')
        pwd = input('Password: ')
        con = connect(host = 'localhost', user = 'root', password = 'sunbeam')
        csr = con.cursor()
        csr.execute('USE Users')
        csr.execute('SELECT UserID, PWD FROM PlrData')
        for k in range(csr.rowcount):
            i, j = csr.fetchone()
            if uid == i and pwd == j:
                getUID = i
                csr.execute('UPDATE PlrData SET log = 1 WHERE UserID = \''+getUID+'\'')
                break
        else:
            print('UserID or Password is Incorrect!!!')
            sl = ''
            while not sl.lower() in ['y','n']:
                sl = input('Try Again (Y/n): ')
            if sl.lower() == 'n':pass
            elif sl.lower() == 'y':signIn()
            else:print('Invalid Input!!!')
    finally:
        con.commit()
        con.close()
    

def play():
    C = []
    c1 = []
    p1 = []
    P = []
    cc = list(range(12))
    pc = list(range(12))
    while True:
        i = randint(1, 25)
        if not i in C:
            C.append(i)
        if len(C)==25:
            break
    while True:
        i = randint(1, 25)
        if not i in P:
            P.append(i)
        if len(P)==25:
            break

    print('\n\n####################################################################')
    print('                ===||===  ||===||   \\===   \\===')
    print('                   ||     ||   ||    \\      \\')
    print('                   ||     ||===||  ===\\   ===\\')
    print('####################################################################\n\n')
    TW = None
    SC = '-1'
    print('SELECT   -   PRESS KEY')
    print('------       ---------')
    print('Head     -           0')
    print('Tail     -           1')
    while not SC in ['0', '1']:
        SC = input('Select your choice(0/1): ')
    TS = randint(0, 1)
    SC = int(SC)
    if SC==TS:
        TW = 1
        print('\n\n\n\n\nYOU WON THE TOSS !!!\n\n\n\n')
    else:
        TW = 0
        print('\n\n\n\n\nYOU LOSE THE TOSS !!!\n\n\n\n')
    sleep(2)
    print('####################################################################')
    print('                        |> || |\ | /-   |--|')
    print('                        |> || | \| |__\ |__|')
    print('####################################################################\n\n')
    if TW:
        print('Player:--->')
        print('===========')
        dply(P, p1)
        print('\n\nComputer:--->')
        print('=============')
        dply(C, c1, rev=1)
    else:
        print('Computer:--->')
        print('=============')
        dply(C, c1, rev=1)
        print('\n\nPlayer:--->')
        print('===========')
        dply(P, p1)
    input('\n\n\nPress ENTER key to start...')
    print('\n\n')
    Round = 1
    while True:
        if (12-len(cc)) >= 7 and (12-len(pc)) >= 7:
            print('\n\n####################################################################')
            print('              ||=\\    ||==//   //\\   \\    //\\    //')
            print('              ||  ))  || //   //==\\   \\  //  \\  //')
            print('              ||=//   ||  \\  //    \\   \\//    \\//')
            print('####################################################################\n\n')
            if TW:
                print('Player:--->')
                print('===========')
                dply(P, p1)
                print('\n\nComputer:--->')
                print('=============')
                dply(C, c1, rev=1)
            else:
                print('Computer:--->')
                print('=============')
                dply(C, c1, rev=1)
                print('\n\nPlayer:--->')
                print('===========')
                dply(P, p1)
            return -1, (Round-1)
        elif (12-len(cc)) >= 7:
            print('\n\n####################################################################')
            print('              ||     ||===||   \\===  ||===')
            print('              ||     ||   ||    \\    ||==')
            print('              ||===  ||===||  ===\\   ||===')
            print('####################################################################\n\n')
            if TW:
                print('Player:--->')
                print('===========')
                dply(P, p1)
                print('\n\nComputer:--->')
                print('=============')
                dply(C, c1, rev=1)
            else:
                print('Computer:--->')
                print('=============')
                dply(C, c1, rev=1)   
                print('\n\nPlayer:--->')
                print('===========')
                dply(P, p1)
            return 0, (Round-1)
        elif (12-len(pc)) >= 7:
            print('\n\n####################################################################')
            print('                \\    //    //  ||===||  ||\\  ||')
            print('                 \\ //  \\ //    ||   ||  || \\ ||')
            print('                  \\     \\      ||===||  ||  \\||')
            print('####################################################################\n\n')
            if TW:
                print('Player:--->')
                print('===========')
                dply(P, p1)
                print('\n\nComputer:--->')
                print('=============')
                dply(C, c1, rev=1)
            else:
                print('Computer:--->')
                print('=============')
                dply(C, c1, rev=1)
                print('\n\nPlayer:--->')
                print('===========')
                dply(P, p1)
            return 1, (Round-1)
        if not TW:
            print('\n\n####################################################################')
            print('                          Round', Round)
            print('####################################################################\n\n')
            print('Computer:--->')
            print('=============')
            toc = None
            while True:
                i = randint(1, 25)
                if not i in c1:
                    c1.append(i)
                    p1.append(i)
                    toc = i
                    break
            dply(C, c1, rev=1)
            print("\nComputer's Turn:", toc)
            print('\n\nPlayer:--->')
            print('===========')
            dply(P, p1)
            while True:
                n = input('\nYour turn(Enter a no. b/w 1-25): ')
                if n.isdigit() and (0 < int(n) < 26) and (not int(n) in p1):
                    n = int(n)
                    p1.append(n)
                    c1.append(n)
                    break
                else:
                    print('Wrong Input !!!')
            Round += 1
        else:
            print('\n\n####################################################################')
            print('                          Round', Round)
            print('####################################################################\n\n')
            print('Player:--->')
            print('===========')
            dply(P, p1)
            while True:
                n = input('\nYour turn(Enter a no. b/w 1-25): ')
                if n.isdigit() and (0 < int(n) < 26) and (not int(n) in p1):
                    n = int(n)
                    p1.append(n)
                    c1.append(n)
                    break
                else:
                    print('Wrong Input !!!')
            print('\n\nComputer:--->')
            print('=============')
            trn = None
            while True:
                i = randint(1, 25)
                if not i in c1:
                    c1.append(i)
                    p1.append(i)
                    trn = i
                    break
            dply(C, c1, rev=1)
            print("\nComputer's Turn:", trn)
            Round += 1

        for j in cc:
            if j==0:
                c = []
                for i in range(5):
                    if C[i * 6] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))

            if j==1:
                c = []
                for i in range(5):
                    if C[(i + 1) * 4] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))
            if j==2:
                c = []
                for i in range(5):
                    if C[i * 4] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))
            if j==3:
                c = []
                for i in range(1, 22, 5):
                    if C[i] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))
            if j==4:
                c = []
                for i in range(2, 23, 5):
                    if C[i] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))
            if j==5:
                c = []
                for i in range(3, 24, 5):
                    if C[i] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))
            if j==6:
                c = []
                for i in range(4, 25, 5):
                    if C[i] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))
            if j==7:
                c = []
                for i in range(5):
                    if C[i] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))
            if j==8:
                c = []
                for i in range(5, 10):
                    if C[i] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))
            if j==9:
                c = []
                for i in range(10, 15):
                    if C[i] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))
            if j==10:
                c = []
                for i in range(15, 20):
                    if C[i] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))
            if j==11:
                c = []
                for i in range(20, 15):
                    if C[i] in c1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: cc.pop(cc.index(j))

        for j in pc:
            if j==0:
                c = []
                for i in range(5):
                    if P[i * 6] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))

            if j==1:
                c = []
                for i in range(5):
                    if P[(i + 1) * 4] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))
            if j==2:
                c = []
                for i in range(5):
                    if P[i * 4] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))
            if j==3:
                c = []
                for i in range(1, 22, 5):
                    if P[i] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))
            if j==4:
                c = []
                for i in range(2, 23, 5):
                    if P[i] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))
            if j==5:
                c = []
                for i in range(3, 24, 5):
                    if P[i] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))
            if j==6:
                c = []
                for i in range(4, 25, 5):
                    if P[i] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))
            if j==7:
                c = []
                for i in range(5):
                    if P[i] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))
            if j==8:
                c = []
                for i in range(5, 10):
                    if P[i] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))
            if j==9:
                c = []
                for i in range(10, 15):
                    if P[i] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))
            if j==10:
                c = []
                for i in range(15, 20):
                    if P[i] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))
            if j==11:
                c = []
                for i in range(20, 15):
                    if P[i] in p1:
                        c.append(1)
                    else:
                        c.append(0)
                else:
                    if not 0 in c: pc.pop(pc.index(j))


################################################################################

# Main Program:--->
print('\n\n\n\n\n\n####################################################################')
print('   \\    //    //  ||===  ||     ||===  ||===||  ||\\  //||  ||===')
print('    \\ //  \\ //    ||==   ||     ||     ||   ||  || \\// ||  ||==')
print('     \\     \\      ||===  ||===  ||===  ||===||  ||     ||  ||===')
sleep(0.6)
print()
print('                        ==||==  ||===||')
print('                          ||    ||   ||')
print('                          ||    ||===||')
sleep(0.6)
print()
print('                      |> || |\ | /-   |--|')
print('                      |> || | \| |__\ |__|')
print('####################################################################\n\n\n\n\n\n\n\n')
sleep(2)

while True:
    if login():
        try:
            con = connect(host = 'localhost', user = 'root', password = 'sunbeam', database = 'Users')
            csr = con.cursor()
            csr.execute('SELECT Fname, Lname FROM PlrData WHERE UserID = \''+getUID+'\'')
            fn, ln = csr.fetchone()
            ex = ''
            while True:
                print('Do you want to Sign In as',fn,ln,'(Y/n): ',end = '')
                ex = input().lower()
                if not ex in ['y', 'n']:
                    print('Invalid Input!!!')
                else:break
            if ex == 'n': logout()
            else: break
        finally:
            con.close()
    else:
        print('\n\nSELECT        PRESS KEY')
        print('------        ---------')
        print('Sign In               1')
        print('Sign Up               2')
        print('Exit                  3')
        key = ''
        while True:
            key = input('Enter the key: ')
            if not key in ['1', '2', '3']:
                print('Invalid Input!!!')
            else: break
        if key == '1':
            signIn()
            break
        elif key == '2':
            signUp()
        elif key == '3':
            print('\n\nExiting...')
            break

if login():
    try:
        con = connect(host = 'localhost', user = 'root', password = 'sunbeam', database = 'Users')
        csr = con.cursor()
        csr.execute('SELECT Fname FROM PlrData WHERE UserID = \''+getUID+'\'')
        name = csr.fetchone()[0]
        print('\n\n                            Hey,', name)
    finally:
        csr.close()
        con.close()

while login():    
    print('\n\n####################################################################')
    print('   ||\\  //||   //\\   || ||\\  ||   ||\\  //|| ||=== ||\\  || ||   ||')
    print('   || \\// ||  //==\\  || || \\ ||   || \\// || ||==  || \\ || ||   ||')
    print('   ||     || //    \\ || ||  \\||   ||     || ||=== ||  \\|| ||===||')
    print('####################################################################\n\n')
    print('SELECT        PRESS KEY')
    print('------        ---------')
    print('Play                  1')
    print('Profile               2')
    print('Options               3')
    print('Exit                  4')
    key = ''
    while True:
        key = input('Enter the key: ')
        if not key in ['1', '2', '3', '4']:
            print('Invalid Input!!!')
        else: break
    if key == '1':
        try:
            con = connect(host = 'localhost', user = 'root', password = 'sunbeam', database = 'Users')
            csr = con.cursor()
            rst, rds = play()
            if rst == -1:
                csr.execute('UPDATE PlrData SET TMD = TMD+1 WHERE log = 1')
                csr.execute('SELECT FDR, LDR FROM PlrData WHERE log = 1')
                f, l = csr.fetchone()
                if f == 0 and l ==  0:
                    csr.execute('UPDATE PlrData SET FDR = '+str(rds)+' WHERE log = 1')
                    csr.execute('UPDATE PlrData SET LDR = '+str(rds)+' WHERE log = 1')
                else:
                    if rds < f:
                        csr.execute('UPDATE PlrData SET FDR = '+str(rds)+' WHERE log = 1')
                    elif rds > l:
                        csr.execute('UPDATE PlrData SET LDR = '+str(rds)+' WHERE log = 1')
            elif rst:
                csr.execute('UPDATE PlrData SET TMW = TMW+1 WHERE log = 1')
                csr.execute('SELECT FWR, LWR FROM PlrData WHERE log = 1')
                f, l = csr.fetchone()
                if f == 0 and l ==  0:
                    csr.execute('UPDATE PlrData SET FWR = '+str(rds)+' WHERE log = 1')
                    csr.execute('UPDATE PlrData SET LWR = '+str(rds)+' WHERE log = 1')
                else:
                    if rds < f:
                        csr.execute('UPDATE PlrData SET FWR = '+str(rds)+' WHERE log = 1')
                    elif rds > l:
                        csr.execute('UPDATE PlrData SET LWR = '+str(rds)+' WHERE log = 1')
            else:
                csr.execute('UPDATE PlrData SET TML = TML+1 WHERE log = 1')
                csr.execute('SELECT FLR, LLR FROM PlrData WHERE log = 1')
                f, l = csr.fetchone()
                if f == 0 and l ==  0:
                    csr.execute('UPDATE PlrData SET FLR = '+str(rds)+' WHERE log = 1')
                    csr.execute('UPDATE PlrData SET LLR = '+str(rds)+' WHERE log = 1')
                else:
                    if rds < f:
                        csr.execute('UPDATE PlrData SET FLR = '+str(rds)+' WHERE log = 1')
                    elif rds > l:
                        csr.execute('UPDATE PlrData SET LLR = '+str(rds)+' WHERE log = 1')
            csr.execute('UPDATE PlrData SET TMP = TMP+1 WHERE log = 1')
            input('Press ENTER to go Back To Main Menu...')
        finally:
            con.commit()
            con.close()
    elif key == '2':
        print('\n\n####################################################################')
        print('         ||==||  ||==//  ||===||  ||===  ||  ||     ||===')
        print('         ||==||  ||=//   ||   ||  ||==   ||  ||     ||==')
        print('         ||      || \\    ||===||  ||     ||  ||===  ||===')
        print('####################################################################\n\n')
        print('SELECT             PRESS KEY')
        print('------             ---------')
        print('Your Card                  1')
        print('Top Winners                2')
        print('Top Loser                  3')
        print('Top Drawer                 4')
        print('Player\'s Card              5')
        try:
            con = connect(host = 'localhost', user = 'root', password = 'sunbeam', database = 'Users')
            csr = con.cursor()
            pk = ''
            while True:
                pk = input('Enter the key: ')
                if not pk in ['1', '2', '3', '4', '5']:
                    print('Invalid Input!!!')
                else: break
            if pk == '1':
                csr.execute('SELECT  Fname, Lname, DOB, TMP, TMW, TML, TMD, FWR, LWR, FLR, LLR, FDR, LDR FROM PlrData WHERE log = 1')
                FD = csr.fetchone()
                ml = 0
                for i in FD:
                    if ml < len(str(i)):ml = len(str(i))+1
                for i in range(len(FD)):
                    print('+'+'-'*(ml+16), end = '+\n|')
                    if i == 0:
                        print('First Name'.ljust(15)+'|'+str(FD[i]).rjust(ml),end='|\n')
                    elif i == 1:
                        print('Last Name'.ljust(15)+'|'+str(FD[i]).rjust(ml),end='|\n')
                    elif i == 2:
                        print('Date of Birth'.ljust(15)+'|'+str(FD[i]).rjust(ml),end='|\n')
                    elif i == 3:
                        print('Matches Played'.ljust(15)+'|'+str(FD[i]).center(ml),end='|\n')
                    elif i == 4:
                        print('Matches Won'.ljust(15)+'|'+str(FD[i]).center(ml),end='|\n')
                        wr = ''
                        if not FD[i-1]: wr = '0 %'
                        else:
                            wr = str((FD[i]/FD[i-1])*100)
                            wr = wr[:wr.index('.')]+' %'
                        print('+'+'-'*(ml+16), end='+\n|')
                        print('Win Ratio'.ljust(15)+'|'+wr.center(ml),end='|\n')
                    elif i == 5:
                        print('Matches Lose'.ljust(15)+'|'+str(FD[i]).center(ml),end='|\n')
                        lr = ''
                        if not FD[i-2]: lr = '0 %'
                        else:
                            lr = str((FD[i]/FD[i-2])*100)
                            lr = lr[:lr.index('.')]+' %'
                        print('+'+'-'*(ml+16), end='+\n|')
                        print('Lose Ratio'.ljust(15)+'|'+lr.center(ml),end='|\n')
                    elif i == 6:
                        print('Matches Draw'.ljust(15)+'|'+str(FD[i]).center(ml),end='|\n')
                        dr = ''
                        if not FD[i-3]: dr = '0 %'
                        else:
                            dr = str((FD[i]/FD[i-3])*100)
                            dr = dr[:dr.index('.')]+' %'
                        print('+'+'-'*(ml+16), end='+\n|')
                        print('Draw Ratio'.ljust(15)+'|'+dr.center(ml),end='|\n')
                    elif i == 7:
                        print('Fastest Win'.ljust(15)+'|'+(str(FD[i])+' Rounds').rjust(ml),end='|\n') 
                    elif i == 8:
                        print('Longest Win'.ljust(15)+'|'+(str(FD[i])+' Rounds').rjust(ml),end='|\n')
                    elif i == 9:
                        print('Fastest Lose'.ljust(15)+'|'+(str(FD[i])+' Rounds').rjust(ml),end='|\n') 
                    elif i == 10:
                        print('Longest Lose'.ljust(15)+'|'+(str(FD[i])+' Rounds').rjust(ml),end='|\n')
                    elif i == 11:
                        print('Fastest Draw'.ljust(15)+'|'+(str(FD[i])+' Rounds').rjust(ml),end='|\n') 
                    elif i == 12:
                        print('Longest Draw'.ljust(15)+'|'+(str(FD[i])+' Rounds').rjust(ml),end='|\n')
                else: 
                    print('+'+'-'*(ml+16)+'+\n')
                    input('Press ENTER to go Back To Main Menu ...')
            elif pk == '2':
                csr.execute('SELECT Fname, Lname, TMP, TMW FROM PlrData ORDER BY TMW DESC')
                dts = csr.fetchall()
                n = 11
                tp = 7
                tw = 4
                for i in dts:
                    if len(i[0]+' '+i[1]) > n: n = len(i[0]+' '+i[1])
                    if len(str(i[2])) > tp: tp = len(str(i[2]))
                    if len(str(i[3])) > tw: tw = len(str(i[3]))
                print('+'+'-'*(n+12+tp+tw),end = '+\n|')
                print('Player Name'.center(n)+'|'+'Matches'.center(tp)+'|'+'Wins'.center(tw)+'|Win Ratio|')
                print('+'+'-'*(n+12+tp+tw)+'+')
                for i in dts:
                    wr = ''
                    if i[2] == 0: wr = '0 %'
                    else:
                        wr = str((i[3]/i[2])*100)
                        wr = wr[:wr.index('.')]+' %'
                    print('|'+(i[0]+' '+i[1]).ljust(n)+'|'+str(i[2]).center(tp)+'|'+str(i[3]).center(tw)+'|'+wr.rjust(9), end = '|\n')
                    print('+'+'-'*(n+12+tp+tw)+'+')
                else:input('Press ENTER to go Back To Main Menu ...')
            elif pk == '3':
                csr.execute('SELECT Fname, Lname, TMP, TML FROM PlrData ORDER BY TMW DESC')
                dts = csr.fetchall()
                n = 11
                tp = 7
                tw = 5
                for i in dts:
                    if len(i[0]+' '+i[1]) > n: n = len(i[0]+' '+i[1])
                    if len(str(i[2])) > tp: tp = len(str(i[2]))
                    if len(str(i[3])) > tw: tw = len(str(i[3]))
                print('+'+'-'*(n+13+tp+tw),end = '+\n|')
                print('Player Name'.center(n)+'|'+'Matches'.center(tp)+'|'+'Loses'.center(tw)+'|Lose Ratio|')
                print('+'+'-'*(n+13+tp+tw)+'+')
                for i in dts:
                    wr = ''
                    if i[2] == 0: wr = '0 %'
                    else:
                        wr = str((i[3]/i[2])*100)
                        wr = wr[:wr.index('.')]+' %'
                    print('|'+(i[0]+' '+i[1]).ljust(n)+'|'+str(i[2]).center(tp)+'|'+str(i[3]).center(tw)+'|'+wr.rjust(10), end = '|\n')
                    print('+'+'-'*(n+13+tp+tw)+'+')
                else:input('Press ENTER to go Back To Main Menu ...')
            elif pk == '4':
                csr.execute('SELECT Fname, Lname, TMP, TMD FROM PlrData ORDER BY TMW DESC')
                dts = csr.fetchall()
                n = 11
                tp = 7
                tw = 5
                for i in dts:
                    if len(i[0]+' '+i[1]) > n: n = len(i[0]+' '+i[1])
                    if len(str(i[2])) > tp: tp = len(str(i[2]))
                    if len(str(i[3])) > tw: tw = len(str(i[3]))
                print('+'+'-'*(n+13+tp+tw),end = '+\n|')
                print('Player Name'.center(n)+'|'+'Matches'.center(tp)+'|'+'Draws'.center(tw)+'|Draw Ratio|')
                print('+'+'-'*(n+13+tp+tw)+'+')
                for i in dts:
                    wr = ''
                    if i[2] == 0: wr = '0 %'
                    else:
                        wr = str((i[3]/i[2])*100)
                        wr = wr[:wr.index('.')]+' %'
                    print('|'+(i[0]+' '+i[1]).ljust(n)+'|'+str(i[2]).center(tp)+'|'+str(i[3]).center(tw)+'|'+wr.rjust(10), end = '|\n')
                    print('+'+'-'*(n+13+tp+tw)+'+')
                else:input('Press ENTER to go Back To Main Menu ...')
            elif pk == '5':
                u = input('\n\nUserID: ')
                p = input('Password: ')
                mt = False
                csr.execute('SELECT UserID, PWD FROM PlrData')
                up = csr.fetchall()
                for i in up:
                    if i[0] == u and i[1] == p:
                        mt = True
                        break
                if mt:
                    csr.execute('SELECT  Fname, Lname, DOB, TMP, TMW, TML, TMD, FWR, LWR, FLR, LLR, FDR, LDR FROM PlrData WHERE UserID = \''+u+'\'')
                    FD = csr.fetchone()
                    ml = 0
                    for i in FD:
                        if ml < len(str(i)):ml = len(str(i))+1
                    for i in range(len(FD)):
                        print('+'+'-'*(ml+16), end = '+\n|')
                        if i == 0:
                            print('First Name'.ljust(15)+'|'+str(FD[i]).rjust(ml),end='|\n')
                        elif i == 1:
                            print('Last Name'.ljust(15)+'|'+str(FD[i]).rjust(ml),end='|\n')
                        elif i == 2:
                            print('Date of Birth'.ljust(15)+'|'+str(FD[i]).rjust(ml),end='|\n')
                        elif i == 3:
                            print('Matches Played'.ljust(15)+'|'+str(FD[i]).center(ml),end='|\n')
                        elif i == 4:
                            print('Matches Won'.ljust(15)+'|'+str(FD[i]).center(ml),end='|\n')
                            wr = ''
                            if not FD[i-1]: wr = '0 %'
                            else:
                                wr = str((FD[i]/FD[i-1])*100)
                                wr = wr[:wr.index('.')]+' %'
                            print('+'+'-'*(ml+16), end='+\n|')
                            print('Win Ratio'.ljust(15)+'|'+wr.center(ml),end='|\n')
                        elif i == 5:
                            print('Matches Lose'.ljust(15)+'|'+str(FD[i]).center(ml),end='|\n')
                            lr = ''
                            if not FD[i-2]: lr = '0 %'
                            else:
                                lr = str((FD[i]/FD[i-2])*100)
                                lr = lr[:lr.index('.')]+' %'
                            print('+'+'-'*(ml+16), end='+\n|')
                            print('Lose Ratio'.ljust(15)+'|'+lr.center(ml),end='|\n')
                        elif i == 6:
                            print('Matches Draw'.ljust(15)+'|'+str(FD[i]).center(ml),end='|\n')
                            dr = ''
                            if not FD[i-3]: dr = '0 %'
                            else:
                                dr = str((FD[i]/FD[i-3])*100)
                                dr = dr[:dr.index('.')]+' %'
                            print('+'+'-'*(ml+16), end='+\n|')
                            print('Draw Ratio'.ljust(15)+'|'+dr.center(ml),end='|\n')
                        elif i == 7:
                            print('Fastest Win'.ljust(15)+'|'+(str(FD[i])+' Rounds').rjust(ml),end='|\n') 
                        elif i == 8:
                            print('Longest Win'.ljust(15)+'|'+(str(FD[i])+' Rounds').rjust(ml),end='|\n')
                        elif i == 9:
                            print('Fastest Lose'.ljust(15)+'|'+(str(FD[i])+' Rounds').rjust(ml),end='|\n') 
                        elif i == 10:
                            print('Longest Lose'.ljust(15)+'|'+(str(FD[i])+' Rounds').rjust(ml),end='|\n')
                        elif i == 11:
                            print('Fastest Draw'.ljust(15)+'|'+(str(FD[i])+' Rounds').rjust(ml),end='|\n') 
                        elif i == 12:
                            print('Longest Draw'.ljust(15)+'|'+(str(FD[i])+' Rounds').rjust(ml),end='|\n')
                    else: 
                        print('+'+'-'*(ml+16)+'+\n')
                        input('Press ENTER to go Back To Main Menu ...')
                else:
                    input('UserID or password not matched!!!\nPress ENTER to go Back To Main Menu ...')
        finally:
            con.commit()
            con.close()
    elif key == '3':
        print('\n\n####################################################################')
        print('     ||===||  ||==||  ===||===  ||  ||===||  ||\\  ||   \\===')
        print('     ||   ||  ||==||     ||     ||  ||   ||  || \\ ||    \\')
        print('     ||===||  ||         ||     ||  ||===||  ||  \\||  ===\\')
        print('####################################################################\n\n')
        print('SELECT                   PRESS KEY')
        print('------                   ---------')
        print('User ID                          1')
        print('Password                         2')
        print('First Name                       3')
        print('Last Name                        4')
        print('Date of Birth                    5')
        print('All Details                      6')
        print('Back TO Main Menu                7')
        try:
            con = connect(host = 'localhost', user = 'root', password = 'sunbeam', database = 'Users')
            csr = con.cursor()
            csr.execute('SELECT UserID, PWD, Fname, Lname, DOB  FROM PlrData WHERE UserID = \''+getUID+'\'')
            u, p, f, l, d = csr.fetchone()
            sel = ''
            while True:
                sel = input('Enter the key: ')
                if not sel in ['1', '2', '3', '4', '5', '6', '7']:
                    print('Invalid Input!!!')
                else: break
            if sel == '1':
                cu = ''
                while True:
                    cu = input('\n\nCurrent User ID: ')
                    if cu == u:
                        nu = input('New User ID: ')
                        csr.execute('UPDATE PlrData SET UserID = \''+nu+'\' WHERE log = 1')
                        getUID = nu
                        break
                    else:
                        print('User ID not matched !!!')
                        t = ''
                        while True:
                            t = input('\nTry Again (Y/n): ').lower()
                            if not t in ['y', 'n']:
                                print('Invalid Input!!!')
                            else: break
                        if t == 'y':pass
                        else:break
            elif sel == '2':
                cpd = ''
                while True:
                    cpd = input('\n\nCurrent Password: ')
                    if cpd == p:
                        npd = input('New Password: ')
                        csr.execute('UPDATE PlrData SET PWD = \''+npd+'\' WHERE log = 1')
                        break
                    else:
                        print('Password not matched !!!')
                        t = ''
                        while True:
                            t = input('\nTry Again (Y/n): ').lower()
                            if not t in ['y', 'n']:
                                print('Invalid Input!!!')
                            else: break
                        if t == 'y':pass
                        else:break
            elif sel == '3':
                print('\n\nFirst Name:',f)
                nf = input('Enter new First Name: ')
                csr.execute('UPDATE PlrData SET Fname = \''+nf+'\' WHERE log = 1')
            elif sel == '4':
                print('\n\nLast Name:',l)
                nl = input('Enter new Last Name: ')
                csr.execute('UPDATE PlrData SET Lname = \''+nl+'\' WHERE log = 1')
            elif sel == '5':
                print('\n\nDate Of Birth:',d)
                nd = input('Enter new Date Of Birth (yyyy-mm-dd): ')
                csr.execute('UPDATE PlrData SET DOB = \''+nd+'\' WHERE log = 1')
            elif sel == '6':
                cu = ''
                while True:
                    cu = input('\n\nCurrent User ID: ')
                    if cu == u:
                        nu = input('New User ID: ')
                        csr.execute('UPDATE PlrData SET UserID = \''+nu+'\' WHERE log = 1')
                        getUID = nu
                        break
                    else:
                        print('User ID not matched !!!')
                        t = ''
                        while True:
                            t = input('\nTry Again (Y/n): ').lower()
                            if not t in ['y', 'n']:
                                print('Invalid Input!!!')
                            else: break
                        if t == 'y':pass
                        else:break
                cpd = ''
                while True:
                    cpd = input('\n\nCurrent Password: ')
                    if cpd == p:
                        npd = input('New Password: ')
                        csr.execute('UPDATE PlrData SET PWD = \''+npd+'\' WHERE log = 1')
                        break
                    else:
                        print('Password not matched !!!')
                        t = ''
                        while True:
                            t = input('\nTry Again (Y/n): ').lower()
                            if not t in ['y', 'n']:
                                print('Invalid Input!!!')
                            else: break
                        if t == 'y':pass
                        else:break
                print('\n\nFirst Name:',f)
                nf = input('Enter new First Name: ')
                csr.execute('UPDATE PlrData SET Fname = \''+nf+'\' WHERE log = 1')
                print('\n\nLast Name:',l)
                nl = input('Enter new Last Name: ')
                csr.execute('UPDATE PlrData SET Lname = \''+nl+'\' WHERE log = 1')
                print('\n\nDate Of Birth:',d)
                nd = input('Enter new Date Of Birth (yyyy-mm-dd): ')
                csr.execute('UPDATE PlrData SET DOB = \''+nd+'\' WHERE log = 1')
            else: pass
        finally:
            con.commit()
            if not sel == '7': print('\nSuccessfully changed ...')
            con.close()
    else:
        ex = ''
        while True:
            ex = input('Do you want Sign Out (Y/n): ').lower()
            if not ex in ['y', 'n']:
                print('Invalid Input!!!')
            else:break
        if ex == 'y':logout()
        print('\n\nExiting...')
        break
