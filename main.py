import random

import pygame

# Variables
width = 1280
height = 720
fps = 30
exit_game = False
game_over = False
score = 0
move = ''
restart = 0
high_score = 500
startgame = 1

#back ground
pygame.mixer.init()
background = pygame.image.load('Background.png')
pygame.mixer.music.load('Background Music.mp3')
pygame.mixer.music.play(-1)
death = pygame.mixer.Sound('Death.mp3')

#Start Menu
def game_start():
    screen.blit(background,(0,0))
    mytext('Press S to continue',black ,580,325,25)
    mytext('Press Q to Exit' , black ,600,350,25)

#end screen
def gameover():
    restart = 1
    screen.fill(white)
    mytext("Game Over", blue, 500, 250, 100)
    mytext("Your score is : " + str(score), black, 600, 325, 25)
    mytext('Press R to restart the game .', black, 550, 350, 25)
    mytext('Press Q to Exit.',black,600,400,25)
    if score >= 300 and score < 500:
        mytext('You are a GOOD Player!',black,575 , 375, 25)
    if score < 300 :
        mytext('You are a NOOB!', black , 600 , 375,25)
    if score >= 500 and score < 750:
        mytext('You are a PRO!', black, 600, 375, 25)
    if score >= 750:
        mytext('You are a INSANE!', black, 600, 375, 25)

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
        pygame.mixer.music.pause()
        gameover()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart = 0
                    game_over = False
                    snake_x = 50
                    snake_y = 50
                    snake_s = 25
                    vel_x = 0
                    vel_y = 0
                    snake_list = []
                    snake_len = 1
                    score = 0
                    fps = 30
                    food_x = random.randint(150, width - 150)
                    food_y = random.randint(150, height - 150)
                    food_s = 25
                if event.key == pygame.K_q:
                    exit_game=True
            if event.type == pygame.QUIT:
                exit_game = True

        clock.tick(fps)
        pygame.display.update()

    else:
        if startgame == 1:
            game_start()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        startgame = 0

                    if event.key == pygame.K_q:
                        exit_game = True
            clock.tick(fps)
            pygame.display.update()
        if startgame == 0 and restart == 0 :

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:

                        if snake_len != 1:

                            if move != 'down':

                                vel_y = -5
                                vel_x = 0
                                move = 'up'

                        elif snake_len==1:

                            vel_y = -5
                            vel_x = 0
                            move = 'up'

                    if event.key == pygame.K_DOWN:

                        if snake_len != 1:

                            if move != 'up':

                                vel_y = 5
                                vel_x = 0
                                move = 'down'

                        elif snake_len==1:

                            vel_y = 5
                            vel_x = 0
                            move = 'down'

                    if event.key == pygame.K_LEFT:

                        if snake_len != 1:

                            if move != 'right':

                                vel_y = 0
                                vel_x = -5
                                move = 'left'

                        elif snake_len==1:

                            vel_y = 0
                            vel_x = -5
                            move = 'left'

                    if event.key == pygame.K_RIGHT:

                        if snake_len != 1:

                            if move != 'left':

                                vel_y = 0
                                vel_x = 5
                                move = 'right'

                        elif snake_len==1:

                            vel_y = 0
                            vel_x = 5
                            move = 'right'

                head = []
                head.append(snake_x)
                head.append(snake_y)
                snake_list.append(head)

                if len(snake_list) > snake_len:
                    del snake_list[0]

                snake_x = snake_x + vel_x
                snake_y=snake_y+ vel_y

                if head in snake_list[:-1]:
                    pygame.mixer.Sound.play(death)
                    game_over= True

                if snake_x<0 or snake_x>width or snake_y<0 or snake_y>height:
                    pygame.mixer.Sound.play(death)
                    game_over=True

                screen.fill(black)
                screen.blit(background,(0,0))
                plotsnake(screen,green,snake_list,snake_s)
                pygame.draw.rect(screen, blue, (food_x, food_y, food_s, food_s))

                if high_score == 500:
                    if  high_score - score == 10 or score == high_score :
                        mytext("You are going to break the HIGH SCORE." , white , 450 ,5,25)

                if score == 510 or score == 520:
                    mytext("You broke the HIGH SCORE !!!",white,450,5,25)

                if score > high_score :
                    high_score = score

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
                    eat = pygame.mixer.Sound('Eat.mp3')
                    pygame.mixer.Sound.play(eat)

                    if score >= 150:
                        mine_y , mine_x = random.randint(150, height-150),random.randint(150, width-150)

                    if score%100 == 0 and score != 0:
                        power_y,power_x = random.randint(150, height-150),random.randint(150, width-150)

                if score >= 150 :

                    if abs(snake_x - mine_x) < 25 and abs(snake_y - mine_y) < 25:
                        pygame.mixer.Sound.play(death)
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
                mytext("Snake speed : " + str(fps) , white , 125,5 , 25)
                mytext('High Score : '+str(high_score),white,305,5,25)
                clock.tick(fps)
                pygame.display.update()

pygame.quit()
quit()