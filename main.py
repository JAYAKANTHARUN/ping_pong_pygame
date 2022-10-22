#import pygame library
import pygame,sys,random

#player animation
def playeranimation():
    if player1.top<=10:
        player1.top=10
    if player1.bottom>=screenheight-10:
        player1.bottom=screenheight-10
    if player2.top<=10:
        player2.top=10
    if player2.bottom>=screenheight-10:
        player2.bottom=screenheight-10

#ball animation
def ballanimation():
    global ballspeedx,ballspeedy
    
    #speed
    ball.x+=ballspeedx
    ball.y+=ballspeedy   
    
    #bounce back and regeneration
    if ball.top<=10 or ball.bottom>=screenheight-10:
        ballspeedy*=-1
    if ball.left<=10 or ball.right>=screenwidth-10:
        ballstart() 
        
    #collide with player
    if ball.colliderect(player1) or ball.colliderect(player2):
        ballspeedx*=-1            

#ball regeneration
def ballstart():
    global ballspeedx,ballspeedy
    ball.center = (screenwidth/2, screenheight/2)
    ballspeedy *= random.choice((1,-1)) # this is done to move the ball after colliding with side walls
    ballspeedx *= random.choice((1,-1))                        

pygame.init()

clock=pygame.time.Clock()

#creating new window
screenwidth=1000
screenheight=700
screen=pygame.display.set_mode((screenwidth,screenheight)) 

#name for window
name=pygame.display.set_caption("Ping Pong Game")

#icon for game
icon=pygame.image.load("image.jpg")
pygame.display.set_icon(icon)

#colours
bgcolor=(144,238,144)
ballcolor=(255,165,0)
player1color=(255,0,0)
player2color=(0,0,0)
linecolor=(0,0,0)
scorecolor=(32,78,41)

#creating shapes
ball=pygame.Rect(screenwidth/2-10,screenheight/2-10,20,20)
player1=pygame.Rect(10, screenheight / 2 - 70, 10,120)
player2=pygame.Rect(screenwidth - 20, screenheight / 2 - 70, 10,120)

#speed 
ballspeedx=3 * random.choice((1,-1))#this is done so that ball will move in random direction after colliding with side walls
ballspeedy=3 * random.choice((1,-1))
player1speed=0
player2speed=0
speed=4

#score details
player1score=0
player2score=0
scorefont=pygame.font.Font("freesansbold.ttf",32)

#run the window
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.quit()
        
        #configuring buttons
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_s:
                player1speed+=speed
            if event.key==pygame.K_w:
                player1speed-=speed
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_s:
                player1speed-=speed
            if event.key==pygame.K_w:
                player1speed+=speed 
                
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                player2speed+=speed
            if event.key==pygame.K_UP:
                player2speed-=speed 
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_DOWN:
                player2speed-=speed
            if event.key==pygame.K_UP:
                player2speed+=speed    
    
    player1.y+=player1speed
    player2.y+=player2speed
    
    ballanimation()
    
    playeranimation()
    
    #drawing objects and Lines        
    screen.fill(bgcolor)        
    pygame.draw.rect(screen,player1color,player1)
    pygame.draw.rect(screen,player2color,player2)
    pygame.draw.ellipse(screen,ballcolor,ball)
    pygame.draw.line(screen,linecolor,[10,10],[screenwidth-10,10])
    pygame.draw.line(screen,linecolor,[10,10],[10,screenheight-10])
    pygame.draw.line(screen,linecolor,[10,screenheight-10],[screenwidth-10,screenheight-10])
    pygame.draw.line(screen,linecolor,[screenwidth-10,10],[screenwidth-10,screenheight-10])
    pygame.draw.line(screen,linecolor,[screenwidth/2,10],[screenwidth/2,screenheight-10])       
            
    #updating window       
    pygame.display.flip() 
    clock.tick(144)            
