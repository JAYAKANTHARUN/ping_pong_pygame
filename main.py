#import pygame library
import pygame,sys

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

#colors
bgcolor=(124,252,0)
ballcolor=(255,165,0)
player1color=(255,0,0)
player2color=(0,0,0)
linecolor=(0,0,0)

#creating shapes
ball=pygame.Rect(screenwidth/2-10,screenheight/2-10,20,20)
player1=pygame.Rect(10, screenheight / 2 - 70, 10,120)
player2=pygame.Rect(screenwidth - 20, screenheight / 2 - 70, 10,120)

#run the window
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.quit()
            
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
