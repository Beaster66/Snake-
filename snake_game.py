import pygame
import random

pygame.init()
pygame.mixer.init()
eat_sound = pygame.mixer.Sound("eat.wav")
gameover_sound = pygame.mixer.Sound("gameover.wav")
move_sound = pygame.mixer.Sound("move.wav")   
pygame.mixer.music.load("music.wav")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

WIDTH = 600
HEIGHT = 400
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    value = score_font.render("Sinu Tulemus: " + str(score), True, YELLOW)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, GREEN, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def gameLoop():
    game_over = False
    game_close = False
    x1 = WIDTH / 2
    y1 = HEIGHT / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
    clock = pygame.time.Clock()

    pygame.mixer.music.play(-1)  # ← add here, loops forever

    while not game_over:
        while game_close == True:   
            dis.fill(BLACK)
            message("Sa Kaotasid! Vajuta SPACE-Mängida Uuesti või ESC-Väljuda", RED)
            your_score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                elif event.key == pygame.K_LEFT:
                    if x1_change != SNAKE_BLOCK:
                        x1_change = -SNAKE_BLOCK
                        y1_change = 0
                        move_sound.play()
                elif event.key == pygame.K_RIGHT:
                    if x1_change != -SNAKE_BLOCK:
                        x1_change = SNAKE_BLOCK
                        y1_change = 0
                        move_sound.play()
                elif event.key == pygame.K_UP:
                    if y1_change != SNAKE_BLOCK:
                        y1_change = -SNAKE_BLOCK
                        x1_change = 0
                        move_sound.play()
                elif event.key == pygame.K_DOWN:
                    if y1_change != -SNAKE_BLOCK:
                        y1_change = SNAKE_BLOCK
                        x1_change = 0
                        move_sound.play()   

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
            gameover_sound.play()

        x1 += x1_change
        y1 += y1_change
        dis.fill(BLACK)
        pygame.draw.rect(dis, BLUE, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
                gameover_sound.play()

        our_snake(SNAKE_BLOCK, snake_List)
        your_score(Length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            eat_sound.play()   
            foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.mixer.music.stop()
    pygame.quit()
    quit()   

screen_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
dis = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)   
pygame.display.set_caption('Ussi Mäng')
gameLoop()   
