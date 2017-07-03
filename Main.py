import pygame,sys
import random as m
from pygame.locals import *

def collision(A,B):
    horizontal=False
    vertical=False
    if (A.left<=B.left) and (A.right>=B.left):
        vertical=True
    elif (A.left>B.left) and (A.left<B.right):
        vertical = True

    if (A.top<=B.top) and (A.bottom>=B.top):
        horizontal=True
    elif (A.top>B.top) and (A.top<B.bottom):
        horizontal = True
    return horizontal and vertical

def game_over():
    print 'bye'

FPS = 15
BLACK = pygame.Color( 0 , 0  , 0  )
WHITE = pygame.Color(255, 255, 255)
RED   = pygame.Color(255, 0  , 0  )
GREEN = pygame.Color( 0 , 255, 0  )
BLUE  = pygame.Color( 0 , 0  , 255)

class Snake:
    def __init__(self,head):
        self.body=[head]
        self.score = 0
    def add(self):
        l=len(self.body)
        self.body.append(self.body[l-1])
        
cat=pygame.image.load('head.png')
direction=''
length=1

pygame.init()
fpsClock=pygame.time.Clock()
SCREEN = pygame.display.set_mode((640,480))
pygame.display.set_caption('Snake Game')

head = pygame.Rect(320,240,10,10)
apple = pygame.Rect(m.randint(0,620),m.randint(0,460),20,20)
snake=Snake(head)

while True:
    # Init Screen
    SCREEN.fill(WHITE)
    for event in pygame.event.get():
        #Catch Events
        if(event.type==KEYDOWN):
            if (event.key==K_DOWN and direction!='up'):
                direction='down'
            elif(event.key==K_LEFT and direction!='right'):
                direction='left'
            elif(event.key==K_UP and direction!='down'):
                direction='up'
            elif(event.key==K_RIGHT and direction!='left'):
                direction='right'
            elif(event.key==K_LCTRL):
                snake.add()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if (direction=='right'):
        head.x+=10
    if(direction=='down'):
        head.y+=10
    if(direction=='left'):
        head.x-=10
    if(direction=='up'):
        head.y-=10

    if(head.x==0):
        head.x=640
    elif(head.x==640):
        head.x=0
    if(head.y==0):
        head.y=480
    elif(head.y==480):
        head.y=0

    l=len(snake.body)

    for i in range(l-1,0,-1):
        snake.body[i]=pygame.Rect(snake.body[i-1])
    snake.body[0]=head

    for i in snake.body:
        if i==snake.body[0]:
            pygame.draw.rect(SCREEN,BLUE,(i.left,i.top,i.width,i.height))
        else:
            pygame.draw.rect(SCREEN,RED,(i.left,i.top,i.width,i.height))
    pygame.draw.rect(SCREEN,GREEN,(apple.left,apple.top,apple.width,apple.height))
    pygame.display.update()
    if collision(apple,snake.body[0]):
         apple.left=m.randint(0,620)
         apple.top=m.randint(0,460)
         snake.add()
    fpsClock.tick(FPS)
