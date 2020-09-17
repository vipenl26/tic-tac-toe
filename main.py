'''@author Vipen Loka'''
import pygame
import sys
from ai_bot2 import check_winner,m,bot_play
####################################################

first_play=1 # switch 1 or 0 for yes or no
bot_active=1# swithc 1 or o for yes or no
#####################################################
bot_turn=[1,0][first_play]

turn=0
swap=[1,0]
count=0
game_over=False
move_check=[[False for i in range(3)]for j in range(3)]


def draw_X(x,y):
	pygame.draw.line(screen,(0,0,0),(200*x+10,200*y+10),(200*(x+1)-10,200*(y+1)-10),6)
	pygame.draw.line(screen,(0,0,0),(200*(x+1)-10,200*y+10),(200*x+10,200*(y+1)-10),6)

def draw_O(x,y):
	pygame.draw.circle(screen,(0,0,0),(100+x*200,100+y*200),95,4)

def final_decision(winner):
	if winner:
		font=pygame.font.SysFont(None,60)#font for setting font size and style
		screen_text=font.render(winner+' is Winner!!',True,(0,0,0))
		screen.blit(screen_text,[200,600])
	else:
		font=pygame.font.SysFont(None,60)#font for setting font size and style
		screen_text=font.render('Tie!!',True,(0,0,0))
		screen.blit(screen_text,[200,600])



def click(t):
	# print(m)
	global turn,count,game_over,bot_turn
	x=t[0]//200
	y=t[1]//200
	if move_check[x][y] or game_over:
		return
	else:
		move_check[x][y]=True
	if turn:
		draw_O(x,y)
		m[x][y]='O'
	else:
		draw_X(x,y)
		m[x][y]='X'
	turn=swap[turn]
	count+=1
	winner=check_winner(m)
	if winner or count==9:
		game_over=True
		final_decision(winner)
	bot_turn=[1,0][bot_turn]



pygame.init()

pygame.display.set_mode((600,650))

pygame.display.set_caption('Tic Tac Toe')
screen=pygame.display.get_surface()

screen.fill((255,255,255))
caty=0
#pygame.draw.rect(screen,(0,0,0),(10,100,50,50))
pygame.draw.line(screen,(0,0,0),(200,0),(200,600),5)
pygame.draw.line(screen,(0,0,0),(400,0),(400,600),5)
pygame.draw.line(screen,(0,0,0),(0,200),(600,200),5)
pygame.draw.line(screen,(0,0,0),(0,400),(600,400),5)


while 1:
	for i in pygame.event.get():
		# print(i)
		if i.type==pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif i.type==pygame.MOUSEBUTTONDOWN:
			click(i.pos)
		if count<9:	
			cords=bot_play(m,['X','O'][first_play],['O','X'][first_play],count,bot_turn,bot_active)
			
			if cords:
				click([cords[0]*200,cords[1]*200])


	pygame.display.update()