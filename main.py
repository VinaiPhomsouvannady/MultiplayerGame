import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,400))

pygame.display.set_caption("EPIC MULTIPLAYER SHOOTER VERSUS")
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/Pixeltype.ttf',50)

sky_surface = pygame.image.load('assets/Sky.png').convert()
ground_surface = pygame.image.load('assets/ground.png').convert()
text_surface = test_font.render('Our Game', False, 'Blue')

snail_surface = pygame.image.load('assets/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

player_surf = pygame.image.load('assets/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(325,25))
    screen.blit(snail_surface,snail_rect)
    snail_rect.left += -5
    if snail_rect.left < -100:
        snail_rect.left = 800
    player_rect.left += 5
    if player_rect.left > 900:
        player_rect.left = -100
    screen.blit(player_surf,player_rect)
    
    pygame.display.update()
    clock.tick(60)
