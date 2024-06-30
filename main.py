import pygame
import sys
import math

pygame.init()

win_width = 1000
win_height = 1000
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Car_game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
TRACK_GREEN = (10, 169, 19)
BLUE = (0, 0, 255)

car_x = 500
car_y = 500
car_speed = 0
car_img_bad = pygame.image.load("car_pixel.png")
car_img = pygame.transform.scale(car_img_bad, (32, 52))
car_angle = 0
car_acceleration = 0.05
car_turn_speed = 5
car_max_speed = 7
car_friction = 0.05

track1_img = pygame.image.load("track.png")

clock = pygame.time.Clock()
FPS = 60

def color_check():
    global car_x, car_y, car_speed
    car_center_x = int(car_x)
    car_center_y = int(car_y)
    color_under_car = win.get_at((car_center_x, car_center_y))

    if color_under_car == TRACK_GREEN:
        print("Game Over! The car drove on green ground.")
        car_speed = 0
        return False
    return True

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
        car_speed += car_acceleration
    if keys[pygame.K_s]:
        car_speed -= car_acceleration

    if keys[pygame.K_a] and car_speed != 0:
        car_angle -= car_turn_speed
    if keys[pygame.K_d] and car_speed != 0:
        car_angle += car_turn_speed

    if car_speed > car_max_speed:
        car_speed = car_max_speed
    if car_speed < -car_max_speed:
        car_speed = -car_max_speed

    if not keys[pygame.K_w] and not keys[pygame.K_s]:
        if car_speed > 0:
            car_speed = max(0, car_speed - car_friction)
        elif car_speed < 0:
            car_speed = min(0, car_speed + car_friction)

    radians = math.radians(car_angle)
    car_x += car_speed * math.sin(radians)
    car_y -= car_speed * math.cos(radians)

    if car_x <= 20:
        car_x = 20
    if car_x >= 980:
        car_x = 980
    if car_y <= 20:
        car_y = 20
    if car_y >= 980:
        car_y = 980

    win.blit(track1_img, (0, 0))
    
    rotated_car_img = pygame.transform.rotate(car_img, -car_angle)
    new_rect = rotated_car_img.get_rect(center=(car_x, car_y))
    win.blit(rotated_car_img, new_rect.topleft)

    pygame.display.flip()

    color_check()


pygame.quit()
sys.exit()
