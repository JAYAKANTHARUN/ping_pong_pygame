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
bgcolor=(255,255,255)
ballcolor=(255,165,0)
player1color=(255,0,0)
player2color=(0,0,0)
linecolor=(0,0,0)

#creating shapes
ball=pygame.Rect(screenwidth/2-15,screenheight/2-15,30,30)
player1=pygame.Rect(10, screenheight / 2 - 70, 10,120)
player2=pygame.Rect(screenwidth - 20, screenheight / 2 - 70, 10,120)

#run the window
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.quit()
           
    pygame.display.flip() 
    clock.tick(144)            
