def checkd(sym,m):
    if (m[0][0]==sym and m[1][1]==sym and m[2][2]==sym):
        return 1
    elif (m[1][1]==sym and m[0][2]==sym and m[2][0]==sym):
        return 1
    else:
        return 0
    
def checkc(sym,m):
    #check for columns
    flag=0
    for i in range(3):
        count=0
        for j in range(3):
            if(m[j][i]==sym):
                count+=1
        if(count==3):
            flag=1
            break
    if(flag==1):
        return 1
    else:
        return 0 
                
def checkr(sym,m):
    #checks for rows
    flag=0
    for i in range(3):
        count=0
        for j in range(3):
            if(m[i][j]==sym):
                count+=1
        if(count==3):
            flag=1
            break
    if(flag==1):
        return 1
    else:
        return 0  


##############################################################################
def move_count(m):
    c=0
    for i in m:
        for j in i:
            if j!='':
                c+=1
    return c

def min_max(m,d,turn,human='O',ai='X'):
    if checkd(['X','O'][turn],m) or checkc(['X','O'][turn],m) or checkr(['X','O'][turn],m):
        return [1,-1][turn]
    elif move_count(m)==9:
        return 0
    if (turn):#for ai bot turn
        score=-99999999
        for i in range(3):
            for j in range(3):
                if m[i][j]=='':
                    m[i][j]=ai
                    score=max(min_max(m,d+1,[1,0][turn],human,ai),score)
                    m[i][j]=''
        return score
    else:
        score=99999999
        for i in range(3):
            for j in range(3):
                if m[i][j]=='':
                    m[i][j]=human
                    score=min(min_max(m,d+1,[1,0][turn],human,ai),score)
                    m[i][j]=''
        return score
        
        
    




def bestMove(m,human='O',ai='X'):
    score=-99999999
    move=None
    for i in range(3):
        for j in range(3):
            if m[i][j]=='':
                m[i][j]=ai
                t=min_max(m,0,0,human,ai)
                if score<t:
                    score=t
                    move=[i,j]
                m[i][j]=''
    return move



                
            
            
