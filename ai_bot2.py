#ai bot and back end
import random

def equal(l):
	if len(set(l))==1:
		return True
	return False

def check_winner(m):
	winner=None
	if equal([m[0][0],m[1][1],m[2][2]]) and m[1][1]!='' or equal([m[0][2],m[1][1],m[2][0]]) and m[1][1]!='':
		winner=m[1][1]
		return winner
	else:
		for i in range(3):
			if all(m[i][j]==m[i][0] for j in range(3)) and m[i][0]!='':
				winner=m[i][0]
				return winner
		for i in range(3):
			if all(m[j][i]==m[0][i] for j in range(3)) and m[0][i]!='':
				winner=m[0][i]
				return winner
	return None

m=[['','',''],['','',''],['','','']]
		
def min_max(m,ai,human,turn,count):
	swap={'X':'O','O':'X'}
	winner=check_winner(m)
	if winner:
		return {ai:1,human:-1}[winner]
	elif count==9:
		return 0
	minn=float('inf')
	maxx=-float('inf')
	if turn==ai:
		for i in range(3):
			for j in range(3):
				if m[i][j]=='':
					m[i][j]=ai
					c=min_max(m,ai,human,swap[turn],count+1)
					m[i][j]=''
					maxx=max(c,maxx)
		return maxx
	else:
		for i in range(3):
			for j in range(3):
				if m[i][j]=='':
					m[i][j]=human
					c=min_max(m,ai,human,swap[turn],count+1)
					m[i][j]=''
					minn=min(minn,c)
		return minn




def bot_play(m,ai,human,count,turn,active):
	if active==False or turn==0:
		return
	mx=None
	my=None
	max_c=-float('inf')
	best_possible_move=[]
	for i in range(3):
		for j in range(3):
			if m[i][j]=='':
				m[i][j]=ai
				turn=human
				c=min_max(m,ai,human,turn,count+1)
				m[i][j]=''
				if c>max_c:
					max_c=c
					mx=i
					my=j
					best_possible_move=[[i,j]]
				elif c==max_c:
					best_possible_move.append([i,j])
	mx,my=random.choice(best_possible_move)			
	return mx,my
#m=[['','',''],['','O',''],['','','O']]
print(bot_play(m,'X','O',1,turn=True,active=True))
