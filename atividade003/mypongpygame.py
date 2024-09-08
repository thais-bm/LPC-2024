# Jucimar Jr
# Thais Carolina - 2415310037
# 2024
import math

import pygame
import random
from math import sin, cos, radians

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 215, 0)

INITIAL_Y_POSITION = 300

SCORE_MAX = 2

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MyPong - PyGame Edition - 2024-09-07")

# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
score_text = score_font.render('00 x 00', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (680, 50)

# victory text
victory_font = pygame.font.Font('assets/PressStart2P.ttf', 100)
victory_text = victory_font.render('VICTORY', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (450, 350)

# sound effects
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('assets/258020__kodack__arcade-bleep-sound.wav')

# player 1
player_1_width = 20
player_1_height = 150
player_1 = pygame.image.load("assets/player.png")
player_1_y = INITIAL_Y_POSITION
PLAYER_1_X = 50
player_1_move_up = False
player_1_move_down = False

# player 2 - robot
player_2_width = 20
player_2_height = 150
player_2 = pygame.image.load("assets/player.png")
player_2_y = INITIAL_Y_POSITION
PLAYER_2_X = 1180

# ball
ball = pygame.image.load("assets/ball.png")
ball_x = 640
ball_y = 360
ball_dx = 5
ball_dy = 5
ball_speed = math.sqrt(ball_dx**2 + ball_dy**2)
MAX_ANGLE = 45

# score
score_1 = 0
score_2 = 0

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_1_move_up = True
            if event.key == pygame.K_DOWN:
                player_1_move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_1_move_up = False
            if event.key == pygame.K_DOWN:
                player_1_move_down = False

    # checking the victory condition
    if score_1 < SCORE_MAX and score_2 < SCORE_MAX:

        # clear screen
        screen.fill(COLOR_BLACK)

        # ball collision with the wall
        if ball_y > 700:
            ball_dy *= -1
            bounce_sound_effect.play()
        elif ball_y <= 0:
            ball_dy *= -1
            bounce_sound_effect.play()

        # ball collision with the player 1 's paddle
        if PLAYER_1_X <= ball_x <= PLAYER_1_X + 50: # X
            if player_1_y <= ball_y <= player_1_y+150: # Y
                if ball_dx < 0:
                    # Its the difference between the ball_y pos and the middle of the paddle-y pos
                    # Normalized: -1 to +1
                    # Max angle: 45 degrees or pi/4
                    pos_center_ball_y = (ball_y - (player_1_y+150)/2) / 75
                    collide_angle = pos_center_ball_y * math.pi/4

                    ball_dx *= -1
                    bounce_sound_effect.play()

        # ball collision with the player 2 's paddle
        if PLAYER_2_X <= ball_x <= PLAYER_2_X + 50:
            if player_2_y <= ball_y <= player_2_y+150:
                if ball_dx > 0:
                    ball_dx *= -1
                    bounce_sound_effect.play()

        # scoring points
        # Making more sensible by using -30
        # Making more sensible by using 1260
        if ball_x < -30:
            ball_x = 640
            ball_y = 360
            ball_dy *= -1
            ball_dx *= -1
            score_2 += 1
            scoring_sound_effect.play()
        elif ball_x > 1250:
            ball_x = 640
            ball_y = 360
            ball_dy *= -1
            ball_dx *= -1
            score_1 += 1
            scoring_sound_effect.play()

        # ball movement
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy

        # player 1 up movement
        if player_1_move_up:
            player_1_y -= 5
        else:
            player_1_y += 0

        # player 1 down movement
        if player_1_move_down:
            player_1_y += 5
        else:
            player_1_y += 0

        # player 1 collides with upper wall
        if player_1_y <= 0:
            player_1_y = 0

        # player 1 collides with lower wall
        elif player_1_y >= 570:
            player_1_y = 570

        # player 2 "Artificial Intelligence"
        """if ball_y > player_2_y+random.randint(25,30):
            player_2_y += 5
        if ball_y < player_2_y-random.randint(25,30):
            player_2_y -= 5"""

        player_2_y = ball_y

        if player_2_y <= 0:
            player_2_y = 0
        elif player_2_y >= 570:
            player_2_y = 570

        # update score hud
        score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, COLOR_WHITE, COLOR_BLACK)

        # debug info
        victory_font_2 = pygame.font.Font('assets/PressStart2P.ttf', 20)

        ball2_text = victory_font_2.render(f'Ball X vel: {ball_dx:.2f} -- Ball Y vel: {ball_dy} --- Ball speed: {ball_speed}', True, COLOR_YELLOW, COLOR_BLACK)
        ball2_text_rect = ball2_text.get_rect()
        ball2_text_rect.topleft = (20, 600)

        ball_text = victory_font_2.render(f'Ball X: {ball_x:.2f} -- Ball Y: {ball_y}', True, COLOR_YELLOW, COLOR_BLACK)
        ball_text_rect = ball_text.get_rect()
        ball_text_rect.topleft = (20, 630)

        p1_text = victory_font_2.render(f'Player 1 X: {PLAYER_1_X} -- P1 y: {player_1_y}', True, COLOR_YELLOW,
                                        COLOR_BLACK)
        p1_text_rect = p1_text.get_rect()
        p1_text_rect.topleft = (20, 650)
        p2_text = victory_font_2.render(f'Player 2 X: {PLAYER_2_X} -- P2 y: {player_2_y}', True, COLOR_YELLOW,
                                        COLOR_BLACK)
        p2_text_rect = p2_text.get_rect()
        p2_text_rect.topleft = (20, 670)

        # drawing objects
        screen.blit(ball, (ball_x, ball_y))
        screen.blit(ball2_text, ball2_text_rect)
        screen.blit(player_1, (PLAYER_1_X, player_1_y))
        screen.blit(player_2, (PLAYER_2_X, player_2_y))
        screen.blit(score_text, score_text_rect)
        screen.blit(ball_text, ball_text_rect)
        screen.blit(p1_text, p1_text_rect)
        screen.blit(p2_text, p2_text_rect)
    else:
        # drawing victory
        screen.fill(COLOR_BLACK)
        screen.blit(score_text, score_text_rect)
        screen.blit(victory_text, victory_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()

