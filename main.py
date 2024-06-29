import pygame
import sys
import math

pygame.init()

win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Car_game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


car_x = 400 
car_y = 400
car_speed = 0
car_img_bad = pygame.image.load("car_pixel.png")
car_img = pygame.transform.scale(car_img_bad, (32, 52))
car_angle = 0
car_acceleration = 0.1
car_turn_speed = 5

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

    win.fill(GREEN)

    if keys[pygame.K_w]:
        car_speed += car_acceleration
    if keys[pygame.K_s]:
        car_speed -= car_acceleration     
    
    if keys[pygame.K_d]:
        car_angle -= car_turn_speed
       
    if keys[pygame.K_a]:
        car_angle += car_turn_speed

    rotated_car_img = pygame.transform.rotate(car_img, car_angle)
    new_rect = rotated_car_img.get_rect(center=(car_x, car_y))

    win.blit(rotated_car_img, new_rect.topleft)    
    
    pygame.display.flip()
    
pygame.quit()
sys.exit()
