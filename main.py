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
car_img_bad = pygame.image.load("car_pixel.png")
car_img = pygame.transform.scale(car_img_bad, (200, 200))
car_angle = 0

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
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                car_angle = 0

    keys = pygame.key.get_pressed()

    win.fill(GREEN)

    if keys[pygame.K_w]:
        car_y -= car_speed
    if keys[pygame.K_s]:
        car_y += car_speed
    if keys[pygame.K_d]:
        car_x += car_speed
        if keys[pygame.K_SPACE]:
            car_angle = 315
    if keys[pygame.K_a]:
        car_x -= car_speed

    

    rotated_car_img = pygame.transform.rotate(car_img, car_angle)

    if car_angle > 0:
        win.blit(rotated_car_img, (car_x, car_y))
    else:
        win.blit(car_img, (car_x, car_y))
    
    pygame.display.flip()
    
pygame.quit()
sys.exit()
