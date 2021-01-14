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
def mytext(text , color , x , y , s):
    font = pygame.font.SysFont('areial',s)
    screentext = font.render(text,True,color)
    screen.blit(screentext,(x,y))

# Color
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)

# mines
mine_x = random.randint(150, width - 150)
mine_y = random.randint(150, height - 150)
mine_s = 25
def mine() -> object:
    pygame.draw.rect(screen, red, (mine_x, mine_y, mine_s, mine_s))

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

# power ups
power_x = random.randint(150, width - 150)
power_y = random.randint(150, height - 150)
power_s = 25
def power():
    pygame.draw.rect(screen, white, (power_x, power_y, power_s, power_s))

# initialize and screen settings
pygame.init()
screen = pygame.display.set_mode((width,height))
icon = pygame.image.load('001-snake.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# Game Loop
while not exit_game:

    if game_over:
        screen.fill(white)
        mytext ("Game Over" , blue ,500,250 , 100)
        mytext("Your score is : " + str(score) , black , 600,325 , 25)

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

        if food_x == snake_list or food_y == snake_list:
            food_x = random.randint(150, width - 150)
            food_y = random.randint(150, height - 150)

        screen.fill(black)
        plotsnake(screen,green,snake_list,snake_s)
        pygame.draw.rect(screen, blue, (food_x, food_y, food_s, food_s))

        if score >= 150:
            mine()
        if score%100 == 0 and score != 0:
            power()

        if abs(snake_x -food_x)<25 and abs(snake_y-food_y)<25 :
            score = score+10
            food_x = random.randint(150, width-150)
            food_y = random.randint(150, height-150)
            snake_len = snake_len+10
            fps = fps + 0.5
            if score >= 150:
                mine_y , mine_x = random.randint(150, height-150),random.randint(150, width-150)
            if score%100 == 0 and score != 0:
                power_y,power_x = random.randint(150, height-150),random.randint(150, width-150)

        if score >= 150 :
            if abs(snake_x - mine_x) < 25 and abs(snake_y - mine_y) < 25:
                game_over = True
        if score% 100 == 0 and score != 0:
            if abs(snake_x - power_x) < 25 and abs(snake_y - power_y) < 25:
                fps = fps - 1.5
                score = score + 20
                mine_y, mine_x = random.randint(150, height - 150), random.randint(150, width - 150)
                power_y, power_x = random.randint(150, height - 150), random.randint(150, width - 150)
                food_x = random.randint(150, width - 150)
                food_y = random.randint(150, height - 150)

        if mine_x== food_x and mine_y == food_y:
            mine_y, mine_x = random.randint(150, height - 150), random.randint(150, width - 150)
        elif mine_x == power_x and mine_y == power_y:
            mine_y, mine_x = random.randint(150, height - 150), random.randint(150, width - 150)

        mytext("Score : "+ str(score) , white ,5,5,25)
        mytext("FPS : " + str(fps) , white , 150,5 , 25)
        clock.tick(fps)
        pygame.display.update()

pygame.quit()
quit()