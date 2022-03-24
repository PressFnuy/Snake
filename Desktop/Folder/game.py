import pygame
from random import randrange
import time as t
pygame.init()
pygame.display.set_caption("Snake")
RES = 800
SIZE = 40
x,y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
immuneapple = randrange(SIZE, 400, SIZE), randrange(SIZE, 400, SIZE)
dirs = {'W': True, 'S':True, 'A': True, 'D': True}
dirs2 = {'UP': True, 'DOWN': True, 'RIGHT': True, 'LEFT': True}
length = 1
snake = [(x, y)]
dx, dy = 0, 0
font_score = pygame.font.SysFont('Arial', 26, bold = True)
font_end = pygame.font.SysFont('Arial', 32, bold = True)
fps = 5
bust = 0
fps_ = 0
wind = pygame.display.set_mode([RES, RES])
score = 0
clock = pygame.time.Clock()
img = pygame.image.load('bg2.jpg').convert()

while True:
    wind.blit(img, (0, 0))
    [(pygame.draw.rect(wind,pygame.Color('green'), (i, j, SIZE, SIZE, ))) for i,j in snake]
    pygame.draw.rect(wind,pygame.Color('red'), (*apple , SIZE, SIZE))
    pygame.draw.rect(wind, pygame.Color('yellow'), (*immuneapple, SIZE, SIZE))
    render_score = font_score.render(f'SCORE: {score}',1,pygame.Color('white'))
    wind.blit(render_score, (5,5))
    clock.tick(fps)
    pygame.display.flip()
    if bust == 1:
        fps_ += 1
        if fps_ ==fps * 12:
            bust = 0
            fps_ = 0                 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    x+=dx*SIZE
    y+=dy*SIZE
    key = pygame.key.get_pressed()

#Управление / Control
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S':False, 'A': True, 'D': True}
    
    if key[pygame.K_UP] and dirs2['UP']:
        dx, dy = 0, -1 
        dirs2 = {'UP': True, 'DOWN': False, 'RIGHT': True, 'LEFT': True}
    
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S':True, 'A': True, 'D': True}
    
    if key[pygame.K_DOWN] and dirs2['DOWN']:
        dx, dy = 0, 1 
        dirs2 = {'UP': False, 'DOWN': True, 'RIGHT': True, 'LEFT': True}
    
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S':True, 'A': True, 'D': False}
    
    if key[pygame.K_LEFT] and dirs2['LEFT']:
        dx, dy = -1, 0
        dirs2 = {'UP': True, 'DOWN': True, 'RIGHT': False, 'LEFT': True}
    
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S':True, 'A': False, 'D': True}
    
    if key[pygame.K_RIGHT] and dirs2['RIGHT']:
        dx, dy =  1, 0
        dirs2 = {'UP': True, 'DOWN': True, 'RIGHT': True, 'LEFT': False}
    snake.append((x, y))
    snake = snake[-length:]

    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length+= 1
        fps+=1
        score += 1
    if snake[-1] == immuneapple:
        immuneapple = randrange(SIZE, 400, SIZE), randrange(SIZE, 200, SIZE)
        length+= 4
        fps +=  2
        bust = 1
        score += 3
    if bust == 0:
        if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
           while True:
               text = 'GAME OVER!'
               render_end = font_end.render(text, 1, pygame.Color('white'))
               wind.blit(render_end, (295, 350))
               pygame.display.flip()
               if key[pygame.K_r]:
                   length = 1
                   fps = 4
                   score = 0
                   dx, dy = 0, 0
                   x,y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
                   apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
                   immuneapple = randrange(SIZE, 400, SIZE), randrange(SIZE, 400, SIZE)
                   pygame.display.flip()
                   clock.tick(fps)
                   break
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       exit()
                    
        pygame.display.flip()
        clock.tick(fps)
