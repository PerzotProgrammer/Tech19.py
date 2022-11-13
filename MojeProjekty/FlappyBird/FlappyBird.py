import pygame
import random
from os import path
from sys import exit


pygame.init()

window_x = 800
window_y = 1000

player_x = window_x/4
player_y = window_y/4

player_grav = 0

background = pygame.image.load(path.dirname(__file__) + "/res/Background.png")

font = pygame.font.Font(path.dirname(__file__) + "/res/font.ttf",100)
font_color = "#00ff00"
score = font.render("0",False,font_color)
score_num = 0

player_surf = pygame.image.load(path.dirname(__file__) + "/res/Flapper.png")
player_rect = player_surf.get_rect(topleft = (player_x, player_y))

floortop_surf = pygame.image.load(path.dirname(__file__) + "/res/Floortop.png")
top_rect = floortop_surf.get_rect(topleft = (0, 0))
floor_rect = floortop_surf.get_rect(topleft = (0, window_y - 64))
rand = 0

wall_surf = pygame.image.load(path.dirname(__file__) + "/res/Wall.png")
wall_up_rect = wall_surf.get_rect(bottomleft = (window_x, 400))
wall_dn_rect = wall_surf.get_rect(topleft = (window_x, 600))

screen = pygame.display.set_mode((window_x,window_y))
pygame.display.set_caption("Flapper")
pygame.display.set_icon(player_surf)
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

#STEROWANIE
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w] or keys[pygame.K_SPACE]:
            player_grav = -5
    else:
        player_grav += 0.5

    player_rect.y += player_grav


#RUCH RUR
    wall_up_rect.x -= 5
    wall_dn_rect.x -= 5

#InProgress  PRAWIDŁOWE PRZESUWANIE RUR
    if wall_up_rect.x <= 0 - wall_up_rect.width:
        if rand <= 0 and wall_dn_rect.y >= window_y - floor_rect.y:
            rand = random.randint(1,300)
        elif rand > 0 and wall_up_rect.y <= 0 + top_rect.y:
            rand = random.randint(-300,1)
        else:
            rand = 0
            wall_up_rect.y = -650
            wall_dn_rect.y = 600

        wall_up_rect.x = window_x
        wall_up_rect.y += rand
        wall_dn_rect.x = window_x
        wall_dn_rect.y += rand
#PUNKTACJA
    if wall_up_rect.x == player_rect.x:
        score_num += 1
        score = font.render(str(score_num),False, font_color)

#WARUNKI PRZEGRANEJ
    if player_rect.colliderect(floor_rect) or player_rect.colliderect(top_rect) or player_rect.colliderect(wall_up_rect) or player_rect.colliderect(wall_dn_rect):
        wall_up_rect.x = window_x
        wall_dn_rect.x = window_x
        player_grav = 0
        player_rect.y = player_y
        score_num = 0
        score = font.render(str(score_num),False, font_color)

    screen.blit(background, (0,0))    
    
    screen.blit(player_surf, player_rect)
    
    screen.blit(wall_surf, wall_up_rect)
    screen.blit(wall_surf, wall_dn_rect)
    screen.blit(floortop_surf, floor_rect)
    screen.blit(floortop_surf, top_rect)

    screen.blit(score,(window_x/2, 100))

    pygame.display.update()
    clock.tick(60)

    #DEBUG
    # print("Player",player_rect)
    # print("Floor",floor_rect)
    # print("Top",top_rect)