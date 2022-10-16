import pygame,sys

pygame.init()

clock=pygame.time.Clock()

screenwidth=1000
screenheight=700
screen=pygame.display.set_mode((screenwidth,screenheight)) 

name=pygame.display.set_caption("Ping Pong Game")

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.quit()
           
    pygame.display.flip() 
    clock.tick(144)            
