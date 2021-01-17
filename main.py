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
background = pygame.image.load('Background.png')

# BGM and Effects
pygame.mixer.init()
pygame.mixer.music.load('Background Music.mp3')
pygame.mixer.music.play(-1)
death = pygame.mixer.Sound('Death.mp3')
eat = pygame.mixer.Sound('Eat.mp3')

#Start Menu
def game_start():
    screen.blit(background,(0,0))
    mytext('Press S to continue',black ,580,325,25)
    mytext('Press Q to Exit' , black ,600,350,25)

#end screen
over_img = pygame.image.load('Game Over screen.png')
def gameover():
    restart = 1

    screen.blit(over_img,(0,0))
    mytext("Your score is : " + str(score), white, 600, 400, 30)
    mytext('Press R to restart the game .', white, 550, 450, 30)
    mytext('Press Q to Exit.',white,600,475,30)
    if score >= 300 and score < 500:
        mytext('You are a GOOD Player!',white,575 , 425, 30)
    if score < 300 :
        mytext('You are a NOOB!', white , 600 , 425,30)
    if score >= 500 and score < 750:
        mytext('You are a PRO!', white, 600, 425, 30)
    if score >= 750:
        mytext('You are a INSANE!', white, 425, 375, 30)

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
mine_img = pygame.image.load('mine.png')
def mine():
    screen.blit(mine_img, (mine_x, mine_y))

mine2_x = random.randint(150, width - 150)
mine2_y = random.randint(150, height - 150)
def mine2():
    screen.blit(mine_img, (mine2_x, mine2_y))

mine3_x = random.randint(150, width - 150)
mine3_y = random.randint(150, height - 150)
def mine3():
    screen.blit(mine_img, (mine3_x, mine3_y))

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
food = pygame.image.load('food.png')

# power ups
slow_x = random.randint(150, width - 150)
slow_y = random.randint(150, height - 150)
slow_img = pygame.image.load('slow.png')
def slow():
    screen.blit(slow_img,(slow_x,slow_y))
'''
short_x = random.randint(150, width - 150)
short_y = random.randint(150, height - 150)
short_img = pygame.image.load('slow.png')
def short():
    screen.blit(short_img,(short_x,short_y))'''

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
                pygame.mixer.music.unpause()

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
                screen.blit(food,(food_x,food_y))

                if high_score == 500:
                    if  high_score - score == 10 or score == high_score :
                        mytext("You are going to break the HIGH SCORE." , white , 450 ,5,25)

                if score == 510 or score == 520:
                    mytext("You broke the HIGH SCORE !!!",white,450,5,25)

                if score > high_score :
                    high_score = score

                if score >= 150:
                    mine()
                    mine2()
                    mine3()

                if score%100 == 0 and score != 0:
                    slow()

                if abs(snake_x -food_x)<40 and abs(snake_y-food_y)<40 :
                    score = score+10
                    food_x = random.randint(150, width-150)
                    food_y = random.randint(150, height-150)
                    snake_len = snake_len+10
                    fps = fps + 0.5
                    pygame.mixer.Sound.play(eat)

                    if score >= 150:
                        mine_y , mine_x = random.randint(150, height-150),random.randint(150, width-150)
                        mine2_y, mine2_x = random.randint(150, height - 150), random.randint(150, width - 150)
                        mine3_y, mine3_x = random.randint(150, height - 150), random.randint(150, width - 150)

                    if score%100 == 0 and score != 0:
                        slow_y, slow_x = random.randint(150, height - 150), random.randint(150, width - 150)

                if score >= 150 :

                    if abs(snake_x - mine_x) < 25 and abs(snake_y - mine_y) < 25:
                        pygame.mixer.Sound.play(death)
                        game_over = True

                if score% 100 == 0 and score != 0:

                    if abs(snake_x - slow_x) < 25 and abs(snake_y - slow_y) < 25:
                        fps = fps - 1.5
                        score = score + 20
                        mine_y, mine_x = random.randint(150, height - 150), random.randint(150, width - 150)
                        mine2_y, mine2_x = random.randint(150, height - 150), random.randint(150, width - 150)
                        mine3_y, mine3_x = random.randint(150, height - 150), random.randint(150, width - 150)
                        slow_y, slow_x = random.randint(150, height - 150), random.randint(150, width - 150)
                        food_x = random.randint(150, width - 150)
                        food_y = random.randint(150, height - 150)
                        pygame.mixer.Sound.play(eat)

                if mine_x== food_x and mine_y == food_y:
                    mine_y, mine_x = random.randint(150, height - 150), random.randint(150, width - 150)

                elif mine_x == slow_x and mine_y == slow_y:
                    mine_y, mine_x = random.randint(150, height - 150), random.randint(150, width - 150)

                if mine2_x== food_x and mine2_y == food_y:
                    mine2_y, mine2_x = random.randint(150, height - 150), random.randint(150, width - 150)

                elif mine2_x == slow_x and mine2_y == slow_y:
                    mine2_y, mine2_x = random.randint(150, height - 150), random.randint(150, width - 150)

                if mine3_x== food_x and mine3_y == food_y:
                    mine3_y, mine3_x = random.randint(150, height - 150), random.randint(150, width - 150)

                elif mine3_x == slow_x and mine3_y == slow_y:
                    mine2_y, mine2_x = random.randint(150, height - 150), random.randint(150, width - 150)

                mytext("Score : "+ str(score) , white ,5,5,25)
                mytext("Snake speed : " + str(fps) , white , 125,5 , 25)
                mytext('High Score : '+str(high_score),white,305,5,25)
                clock.tick(fps)
                pygame.display.update()

pygame.quit()
quit()