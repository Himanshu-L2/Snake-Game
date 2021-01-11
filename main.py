import pygame

import random

# Variables
width = 1280
height = 720
fps = 30
exit_game = False
game_over = False
score = 0
# displaying score
def mytext(text , color , x , y):
    font = pygame.font.SysFont('areial',25)
    screentext = font.render(text,True,color)
    screen.blit(screentext,(x,y))

# Color
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)

# Snake
snake_x = 50
snake_y = 50
snake_s = 25
vel_x = 0
vel_y = 0
snake_list = []
snake_len = 1

# Making snake bigger when it eats food
def plotsnake(window,color,snake_list,snake_s):
    for x , y in snake_list:
        pygame.draw.rect(window,color,(x,y,snake_s,snake_s))

# food
food_x = random.randint(150, width-150)
food_y = random.randint(150,height-150)
food_s = 25

# initialize and screen settings
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width,height))
icon = pygame.image.load('001-snake.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# Game Loop
while not exit_game:
    if game_over:
        screen.fill(white)
        mytext ("Game Over" , blue ,610,300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

        clock.tick(fps)
        pygame.display.update()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                vel_y = -5
                vel_x = 0
            if event.key == pygame.K_DOWN:
                vel_y = 5
                vel_x = 0
            if event.key == pygame.K_LEFT:
                vel_y = 0
                vel_x = -5
            if event.key == pygame.K_RIGHT:
                vel_y = 0
                vel_x = 5

        head = []
        head.append(snake_x)
        head.append(snake_y)
        snake_list.append(head)
        if len(snake_list) > snake_len:
            del snake_list[0]

        snake_x = snake_x + vel_x
        snake_y=snake_y+ vel_y
        if head in snake_list[:-1]:
            game_over= True
        if snake_x<0 or snake_x>width or snake_y<0 or snake_y>height:
            game_over=True
        screen.fill(black)
        plotsnake(screen,green,snake_list,snake_s)
        pygame.draw.rect(screen, red, (food_x, food_y, food_s, food_s))

        if abs(snake_x -food_x)<25 and abs(snake_y-food_y)<25 :
            score = score+10
            food_x = random.randint(150, width-150)
            food_y = random.randint(150, height-150)
            snake_len = snake_len+10
            fps = fps + 0.5

        mytext("Score : "+ str(score) , white ,5,5)
        clock.tick(fps)
        pygame.display.update()

pygame.quit()
quit()