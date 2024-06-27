import pygame
import sys

pygame.init()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Car_game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


car_width = 50
car_height = 50
car_x = 400 - car_width // 2
car_y = 400
car_speed = 5

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        car_y -= car_speed
    
    pygame.draw.rect(win, RED, (car_x, car_y, car_width, car_height))
    
    pygame.display.flip()
    
pygame.quit()
sys.exit()
