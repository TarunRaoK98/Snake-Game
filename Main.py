import pygame,sys,time
import random as R
from pygame.locals import *


FPS = 25
BLACK = pygame.Color( 0 , 0  , 0  )
WHITE = pygame.Color(255, 255, 255)
RED   = pygame.Color(255, 0  , 0  )
GREEN = pygame.Color( 0 , 255, 0  )
BLUE  = pygame.Color( 0 , 0  , 255)
SCREENX=640
SCREENY=480
SPEED=10

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
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('GAME OVER', False, BLACK)
    SCREEN.blit(textsurface,(0,0))
    textsurface = myfont.render('SCORE : '+str(snake.score), False, BLACK)
    SCREEN.blit(textsurface,(0,30))
    time.sleep(5)

class Snake:
    def __init__(self):
        self.head = pygame.Rect(SCREENX/2,SCREENY/2,10,10)
        self.body=[self.head]
        self.score = 0
        self.speed=SPEED
    def add(self):
        l=len(self.body)
        self.body.append(self.body[l-1])
    def draw(self):
        l=len(self.body)
        for i in range(l-1,0,-1):
            snake.body[i]=pygame.Rect(snake.body[i-1])
        snake.body[0]=self.head
        for i in snake.body:
            pygame.draw.rect(SCREEN,BLUE if i==snake.body[0] else RED,(i.left,i.top,i.width,i.height))

pygame.init()
pygame.display.set_caption('Snake Game')
SCREEN = pygame.display.set_mode((SCREENX,SCREENY))
fpsClock=pygame.time.Clock()

direction=''
suicide=False
snake=Snake()
apple = pygame.Rect(R.randint(0,SCREENX-snake.head.width),R.randint(0,SCREENY-snake.head.height),20,20)

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
            elif(event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if (direction=='right'):
        snake.head.x+=snake.speed
    elif(direction=='down'):
        snake.head.y+=snake.speed
    elif(direction=='left'):
        snake.head.x-=snake.speed
    elif(direction=='up'):
        snake.head.y-=snake.speed

    if(snake.head.x==0 or snake.head.x==SCREENX) and (direction!='up' and direction !='down'):
        snake.head.x=SCREENX-snake.head.x
    if(snake.head.y==0 or snake.head.y==SCREENY) and (direction!='right' and direction !='left'):
        snake.head.y=SCREENY-snake.head.y

    if collision(apple,snake.body[0]):
         apple.left=R.randint(apple.width,SCREENX-apple.width)
         apple.top=R.randint(apple.height,SCREENY-apple.height)
         snake.add()
         snake.score+=1

    for i in snake.body[3:]:
        if collision(i,snake.body[0]):
            suicide=True
    if suicide:
        game_over()
    snake.draw()
    pygame.draw.rect(SCREEN,GREEN,(apple.left,apple.top,apple.width,apple.height))
    pygame.display.update()
    fpsClock.tick(FPS)