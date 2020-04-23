import pygame
import os

pygame.init()

screen_width=1200
screen_height=550

win=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Goblin Smash")

clock=pygame.time.Clock()
bg=pygame.transform.scale(pygame.image.load("Game/bg.jpg"),(1200,550))

class platform(object):
	def __init__(self,x,y,width,height):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.up_col=False
		self.down_col=False
		self.hitbox=(self.x,self.y,self.width,self.height)
		
	def draw(self):
		pygame.draw.rect(win,(100,50,50),self.hitbox)     #rectangle drawn
		
		
	
				
		
		
		
		
class player(object):
	walkLeft=[pygame.transform.scale(pygame.image.load("Game/L1.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/L2.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/L3.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/L4.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/L5.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/L6.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/L7.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/L8.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/L9.png"),(50,50))]
	walkRight=[pygame.transform.scale(pygame.image.load("Game/R1.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/R2.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/R3.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/R4.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/R5.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/R6.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/R7.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/R8.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/R9.png"),(50,50))]
	standing_img=pygame.transform.scale(pygame.image.load("Game/standing.png"),(50,50))
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.width=50
		self.height=50
		self.right=True
		self.left=False
		self.vel=3
		self.standing=True
		self.walkCount=0
		self.lifes=3
		self.isjump=False
		self.jumpCount=10
		self.hitbox=(self.x,self.y,self.width,self.height)
	
	def draw(self):
	
		if self.walkCount+1>=18:
			self.walkCount=0
		if self.standing==False:
			if self.left==True:
				self.x-=self.vel
				win.blit(self.walkLeft[self.walkCount//2],(self.x,self.y))
				self.walkCount+=1
			elif self.right==True:
				self.x+=self.vel
				win.blit(self.walkRight[self.walkCount//2],(self.x,self.y))
				self.walkCount+=1
		else:
			self.walkCount=0
			if self.right==True:
				win.blit(self.walkRight[0],(self.x,self.y))
			else:
				win.blit(self.walkLeft[0],(self.x,self.y))
		text=font.render("Lifes",1,(100,200,100))
		win.blit(text,(10,10))
		if self.lifes>0:
			for i in range(self.lifes):
			
				pygame.draw.circle(win,(100,250,200),(50+(i*50),50),12)
		
		if self.lifes==0:
			#pygame.time.delay(10000)
			win.blit(self.standing_img,(self.x,self.y))
			text2=font.render("GAME OVER",1,(200,100,100))
			win.blit(text2,(600-text2.get_width()//2,10))
			
				
			
		self.hitbox=(self.x+15,self.y+10,self.width-30,self.height-10)		
		#pygame.draw.rect(win,(200,50,20),self.hitbox,1)		
			
	def hit(self):
		pygame.time.delay(500)
		self.lifes-=1
		self.x=50
		self.y=490
	"""def jump_up(self):
		if self.jumpCount>=0:
			vel=(self.jumpCount**2)*0.5
			if self.y-vel>0:
				self.y-=vel
				self.jumpCount-=1
			else:
				man.jumpCount=0
	
	def fall_down(self):
		if self.jumpCount<0:
			vel=(self.jumpCount**2)*0.5
			""""""for i in range(len(platforms)-1,0,-1):
				collide_up(platforms[i],self,vel)
				if platforms[i].up_col==True:
					self.jumpCount=10
					self.isjump=False
					for j in range(len(platforms)):
						if j!=i:
							platforms[j].up_col=False
					for pf in platforms:
						print(pf.up_col)
					print(" ")	
					break
			else:""""""
			self.y+=vel
			self.jumpCount-=1"""
				
		
			
			
class projectile(object):
	def __init__(self,color,x,y,radius,facing):
		self.x=x
		self.y=y
		self.radius=radius
		self.facing=facing
		self.vel=8*facing
		self.color=color
		
	def draw(self,win):
		pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
		
		
		
class enemy(object):
	walkLeft=[pygame.transform.scale(pygame.image.load("Game/L1E.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/L2E.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/L3E.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/L4E.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/L5E.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/L6E.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/L7E.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/L8E.png"),(50,50))]    #,pygame.transform.scale(pygame.image.load("Game/L11E.png"),(50,50))]
	walkRight=[pygame.transform.scale(pygame.image.load("Game/R1E.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/R2E.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/R3E.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/R4E.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/R5E.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/R6E.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/R7E.png"),(50,50)),pygame.transform.scale(pygame.image.load("Game/R8E.png"),(50,50))]   #,pygame.transform.scale(pygame.image.load("Game/R11E.png"),(50,50))]
	
	
	def __init__(self,x,y,dist_limit):
		self.x1=x
		self.x=x
		self.y=y
		self.x2=x+dist_limit
		self.width=50
		self.height=50
		self.hitbox=(self.x+17,self.y,24,45)
		self.walkCount=0
		self.vel=3
		self.visible=True
		self.health=10
		
		
		
	def move(self):
		if self.vel>0:
			if self.x+self.vel<self.x2:
				self.x+=self.vel
			else:
				self.vel*=-1
				self.walkCount=0
		else:
			if self.x+self.vel>self.x1:
				self.x+=self.vel
			else:
				self.vel*=-1
				self.walkCount=0	

	def draw(self):
		
		self.move()
		if self.walkCount+1>=24:
			self.walkCount=0
	
		if self.vel>0:
			win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
			self.walkCount+=1
			#self.hitbox=(self.x+13,self.y,20,45)
		else:
			win.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
			self.walkCount+=1
			#self.hitbox=(self.x+25,self.y,20,45)
			
		self.hitbox=(self.x+17,self.y,24,45)
		#pygame.draw.rect(win,(200,50,20),self.hitbox,1)
		pygame.draw.rect(win,(255,100,100),(self.x+7,self.y-10,self.width-10,5),1)
		pygame.draw.rect(win,(100,255,100),(self.x+7,self.y-10,(self.width-10)*(self.health/10),5))
	
	def hit(self):
		if self.health>0:
			self.health-=1
		else:
			goblins.remove(self)


class values:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.hitbox=(self.x-20,self.y-20,self.x+20,self.y+20)
		#self.color=color
		#self.radius=radius
		
	def draw(self):
		pygame.draw.circle(win,(245,197,0),(self.x,self.y),20)
		pygame.draw.circle(win,(235,235,0),(self.x,self.y),13)
		
	def hit(self):
		coins.remove(self)
		
		
			

def collide_up(pfi,avatar,vel):
	if avatar.hitbox[1]+avatar.hitbox[3]+vel<=pfi.hitbox[1]:
		if avatar.hitbox[0]<=pfi.x+pfi.width and avatar.hitbox[0]+avatar.hitbox[2]>=pfi.x:
			pfi.up_col=True
			avatar.y=pfi.y-50
			
			
"""def collide_down(pfi,avatar,vel):
	if pfi.up_col==False:
		if avatar.hitbox[1]-vel==pfi.hitbox[1]+pfi.hitbox[3]:
			if avatar.hitbox[0]<=pfi.x+pfi.width and avatar.hitbox[0]+avatar.hitbox[2]>=pfi.x:
				return True
			else:
				return False"""

"""def goblin_hit_bullet(bulet):
	for g in goblins:
			
		if bullet.y-bullet.radius > g.hitbox[1] and bullet.y+bullet.radius < g.hitbox[1]+g.hitbox[3]:
			if bullet.x+bullet.radius> g.hitbox[0] or bullet.x-bullet.radius<g.hitbox[0]+g.hitbox[2]:
				bullets.remove(bullet)
				g.hit()"""

def redrawGameWindow():

	win.blit(bg,(0,0))
	
	for pf in platforms:
		pf.draw()
		
	for coin in coins:
		coin.draw()	
	for e in goblins:
		e.draw()
	
	man.draw()	
	for bullet in bullets:
		bullet.draw(win)
	
	text2=font.render("Score : "+str(score),1,(200,200,10))
	win.blit(text2,(1150-text2.get_width(),10))
	if score==200:
		text3=font.render("You Won",1,(100,250,100))
		win.blit(text3,(600-text2.get_width()//2,10))
		man.lifes=0
		
		
	pygame.display.update()
	


font=pygame.font.SysFont("conicsans",30,True,True)	
goblins=[]	
platforms=[]
coins=[]	
man=player(50,490)
bullets=[]
shootctr=0
vel=0
score=0

#platform formation
platforms.append(platform(0,540,140,10))
platforms.append(platform(130,420,300,10))
platforms.append(platform(700,420,400,10))
platforms.append(platform(300,280,450,10))
platforms.append(platform(700,150,400,10))
platforms.append(platform(100,150,400,10))

#goblin formation
goblins.append(enemy(180,377,200))
goblins.append(enemy(700,377,300))
goblins.append(enemy(350,237,350))
goblins.append(enemy(780,107,290))
goblins.append(enemy(100,107,320))

#coins formation
for pf in range(1,len(platforms)):
	for i in range(1,5):
		coins.append(values(platforms[pf].x-30+i*70,platforms[pf].y-30))

platforms[0].up_col=True

run=True
while run:
	
	clock.tick(27)
	
	keys=pygame.key.get_pressed()
	
	if man.lifes>0:
		if shootctr==3:
			shootctr=0
		if shootctr>0:
			shootctr+=1
			
			
		for gb in goblins:
			if gb.hitbox[0]<man.hitbox[0]+man.hitbox[2] and gb.hitbox[0]+gb.hitbox[2]>man.hitbox[0]:
				if gb.hitbox[1]<man.hitbox[1]+man.hitbox[3] and gb.hitbox[1]+gb.hitbox[3]>man.hitbox[1]:
					man.hit()
					
					
		
		#player movements
		if keys[pygame.K_LEFT] and man.x>man.vel:
			man.left=True
			man.right=False
			man.standing=False
		elif keys[pygame.K_RIGHT] and man.x+man.vel+man.width<screen_width:
			man.right=True
			man.left=False
			man.standing=False
		else:
			man.standing=True
			
		man.draw()	
		
		#player jump
		k=man.y-50
		if man.isjump!= True:
			if keys[pygame.K_UP]:
				man.isjump=True
				man.walkCount=0
		else:
			if man.jumpCount>=-10:
				neg=1
				vel=(man.jumpCount**2)*0.5
				if man.jumpCount>0:
					
						
					if man.y-vel>0:	
						man.y-=vel*neg
						man.jumpCount-=1
					else:
						man.jumpCount=0
						
					for pf in range(len(platforms)-1,-1,-1):
						if platforms[pf].x<man.hitbox[0]+man.hitbox[2] and platforms[pf].x+platforms[pf].width>man.hitbox[0]:
							if man.hitbox[2]>platforms[pf].y+platforms[pf].height and man.hitbox[2]+man.hitbox[4]<platforms[pf].y:
								man.jumpCount=0
								
						
				else:
					for i in range(len(platforms)-1,0,-1):
						collide_up(platforms[i],man,vel)
						if platforms[i].up_col==True:
							man.jumpCount=10
							man.isjump=False
							for j in range(len(platforms)):
								if j!=i:
									platforms[j].up_col=False
							break
					else:
						neg=-1
						man.y-=vel*neg
						man.jumpCount-=1
			else:
				man.jumpCount=10
				man.isjump=False
						
						
		for pf in platforms:
			if pf.up_col==True:
				if man.hitbox[0]+man.hitbox[2]>pf.x and man.hitbox[0]<pf.x+pf.width:
					break
				else:	
					pf.up_col=False
					for pfi in platforms:
						collide_up(pfi,man,vel)
						if pfi.up_col==True:
							break
					else:
						"""pygame.time.delay(500)
						man.x=50
						man.y=490"""
						man.hit()
						platforms[0].up_col=True
						
		#bullet hit			
		for bullet in bullets:
			for g in goblins:
				if bullet.y-bullet.radius > g.hitbox[1] and bullet.y+bullet.radius < g.hitbox[1]+g.hitbox[3]:
					if bullet.x+bullet.radius> g.hitbox[0] and bullet.x-bullet.radius<g.hitbox[0]+g.hitbox[2]:
						bullets.remove(bullet)
						g.hit()
			
				
			if bullet.x+bullet.vel>=0 and bullet.x+bullet.vel<=screen_width:
				bullet.x+=bullet.vel	
			else:
				bullets.remove(bullet)
				
					
			
		#bullet throw
		if keys[pygame.K_SPACE] and shootctr==0:
			facing=0
			if len(bullets)<10:
				if man.left==True:
					facing=-1
					bullets.append(projectile((100,100,100),man.x+20,round(man.y+man.height//2),4,facing))
				elif man.right==True:
					facing=+1
					bullets.append(projectile((100,100,100),round(man.x+man.width-20),round(man.y+man.height//2),4,facing))
			shootctr=1		
		
		#coin get
		for coin in coins:
			if coin.hitbox[0]<man.hitbox[0]+man.hitbox[2] and coin.hitbox[2]>man.hitbox[0]:
				if coin.hitbox[1]<man.hitbox[1]+man.hitbox[3] and coin.hitbox[3]>man.hitbox[1]:
					coin.hit()
					score+=10
			
					
		
			
		#quiting function
		for event in pygame.event.get():     
			if event.type==pygame.QUIT:
				run=False
		
		redrawGameWindow()
	else:
		run=False
pygame.time.delay(5000)	
pygame.quit()	