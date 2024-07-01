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
TRACK_GREEN = (10, 168, 18)
BLUE = (0, 0, 255)

car_x = 500
car_y = 200
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

nitro_img_small = pygame.image.load("nitro.png")
nitro_img = pygame.transform.scale(nitro_img_small, (21, 33))
nitro_time = 5000
nitro_active = False

menu_img_small = pygame.image.load("menu.jpg")
menu_img = pygame.transform.scale(menu_img_small, (1000, 1000))

last_time = pygame.time.get_ticks()

pygame.font.init()
font = pygame.font.Font(None, 36)

def nitro():
    global keys, nitro, nitro_last, car_max_speed, nitro_active, last_time
    
    current_time = pygame.time.get_ticks()
    if current_time - last_time >= nitro_time:
        nitro_active = True

    if keys[pygame.K_SPACE] and nitro_active:
        car_max_speed = 12
        win.blit(nitro_img, (0, 0))
    else:
        car_max_speed = 7

def get_color_at_position(x, y):
    return track1_img.get_at((int(x), int(y)))[:3]

menu_running = True
running = False
running_mouse = False
while menu_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                running = True
                menu_running = False
            if event.key == pygame.K_m:
                running_mouse = True
                menu_running = False
                
    win.blit(menu_img, (0, 0))
    
    pygame.display.flip()

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()

    win.blit(track1_img, (0, 0))

    if keys[pygame.K_w]:
        car_speed += car_acceleration
    if keys[pygame.K_s]:
        car_speed -= car_acceleration

    if keys[pygame.K_a] and not car_speed == 0:
        car_angle -= car_turn_speed
    if keys[pygame.K_d] and not car_speed == 0:
        car_angle += car_turn_speed

    if car_speed > car_max_speed:
        car_speed = car_max_speed
    if car_speed < -car_max_speed:
        car_speed = -car_max_speed

    if not keys[pygame.K_w] and not keys[pygame.K_s] and not car_speed <= 0:
        car_speed = max(0, car_speed - car_friction)
    if not keys[pygame.K_w] and not keys[pygame.K_s] and car_speed < 0:
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

    car_center_color = get_color_at_position(car_x, car_y)
    if car_center_color == TRACK_GREEN:
        car_speed = 0

    rotated_car_img = pygame.transform.rotate(car_img, -car_angle)
    new_rect = rotated_car_img.get_rect(center=(car_x, car_y))

    nitro()

    win.blit(rotated_car_img, new_rect.topleft)

    speed_text = font.render(f'Speed: {car_speed:.2f}', True, WHITE)
    win.blit(speed_text, (100, 10))

    pygame.display.flip()

while running_mouse:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_mouse = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running_mouse = False

    keys = pygame.key.get_pressed()

    win.blit(track1_img, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    # Berechne den Winkel zum Mauszeiger
    dx = mouse_pos[0] - car_x
    dy = mouse_pos[1] - car_y
    target_angle = math.degrees(math.atan2(-dy, dx))
    
    # Winkel des Autos anpassen
    angle_diff = (target_angle - car_angle + 180) % 360 - 180
    if angle_diff > 0:
        car_angle += car_turn_speed
    elif angle_diff < 0:
        car_angle -= car_turn_speed
    
    car_angle %= 360

    # Bewegung des Autos
    radians = math.radians(car_angle)
    car_x += car_speed * math.cos(radians)
    car_y -= car_speed * math.sin(radians)

    if car_speed < car_max_speed:
        car_speed += car_acceleration
    
    if car_x <= 20:
        car_x = 20
    if car_x >= 980:
        car_x = 980
    if car_y <= 20:
        car_y = 20
    if car_y >= 980:
        car_y = 980

    car_center_color = get_color_at_position(car_x, car_y)
    if car_center_color == TRACK_GREEN:
        car_speed = 0

    rotated_car_img = pygame.transform.rotate(car_img, -car_angle)
    new_rect = rotated_car_img.get_rect(center=(car_x, car_y))

    nitro()

    win.blit(rotated_car_img, new_rect.topleft)

    speed_text = font.render(f'Speed: {car_speed:.2f}', True, WHITE)
    win.blit(speed_text, (100, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
