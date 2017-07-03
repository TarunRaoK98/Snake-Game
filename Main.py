import pygame,sys
import random as R
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
SCREENX=640
SCREENY=480
SPEED=10

class Snake:
    def __init__(self,head):
        self.body=[head]
        self.score = 0
        self.speed=SPEED
    def add(self):
        l=len(self.body)
        self.body.append(self.body[l-1])
    def draw(self,head):
        l=len(self.body)
        for i in range(l-1,0,-1):
            snake.body[i]=pygame.Rect(snake.body[i-1])
        snake.body[0]=head
        for i in snake.body:
            pygame.draw.rect(SCREEN,BLUE if i==snake.body[0] else RED,(i.left,i.top,i.width,i.height))            
            
pygame.init()
pygame.display.set_caption('Snake Game')
SCREEN = pygame.display.set_mode((SCREENX,SCREENY))
fpsClock=pygame.time.Clock()
direction=''

head = pygame.Rect(320,240,10,10)
snake=Snake(head)
apple = pygame.Rect(R.randint(0,SCREENX-head.width),R.randint(0,SCREENY-head.height),20,20)

while True:
    SCREEN.fill(WHITE)
    for event in pygame.event.get():
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
            elif(event.ket==K_ESCAPE):
                pygame.quit()
                sys.exit()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if (direction=='right'):
        head.x+=snake.speed
    elif(direction=='down'):
        head.y+=snake.speed
    elif(direction=='left'):
        head.x-=snake.speed
    elif(direction=='up'):
        head.y-=snake.speed
    if(head.x==0 or head.x==SCREENX):
        head.x=SCREENX-head.x
    if(head.y==0 or head.y==SCREENX):
        head.y=SCREENY-head.y
        
    if collision(apple,snake.body[0]):
         apple.left=m.randint(0,620)
         apple.top=m.randint(0,460)
         snake.add()
            
    snake.draw(head)
    pygame.draw.rect(SCREEN,GREEN,(apple.left,apple.top,apple.width,apple.height))            
    pygame.display.update()
    fpsClock.tick(FPS)
