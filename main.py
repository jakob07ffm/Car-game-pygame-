import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Advanced Car Game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()
FPS = 60

CAR_WIDTH, CAR_HEIGHT = 50, 80
car_x = WIDTH // 2
car_y = HEIGHT - CAR_HEIGHT - 10
car_speed = 5

ROAD_WIDTH = WIDTH // 2
ROAD_COLOR = (50, 50, 50)

OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
obstacle_speed = 5
obstacles = []

def create_obstacle():
    x = random.randint(WIDTH // 4, WIDTH - OBSTACLE_WIDTH - WIDTH // 4)
    y = -OBSTACLE_HEIGHT
    return [x, y]

def draw_car(x, y):
    pygame.draw.rect(screen, BLUE, [x, y, CAR_WIDTH, CAR_HEIGHT])
    pygame.draw.polygon(screen, BLACK, [(x, y + CAR_HEIGHT), (x + CAR_WIDTH // 2, y + CAR_HEIGHT + 20), (x + CAR_WIDTH, y + CAR_HEIGHT)])

def draw_road():
    pygame.draw.rect(screen, ROAD_COLOR, [WIDTH // 4, 0, ROAD_WIDTH, HEIGHT])

def draw_obstacles(obstacles):
    for obs in obstacles:
        pygame.draw.rect(screen, RED, [obs[0], obs[1], OBSTACLE_WIDTH, OBSTACLE_HEIGHT])

def move_obstacles(obstacles):
    for obs in obstacles:
        obs[1] += obstacle_speed

def check_collision(car_x, car_y, obstacles):
    for obs in obstacles:
        if (car_x < obs[0] + OBSTACLE_WIDTH and car_x + CAR_WIDTH > obs[0] and
            car_y < obs[1] + OBSTACLE_HEIGHT and car_y + CAR_HEIGHT > obs[1]):
            return True
    return False

def game_loop():
    global car_x, car_y, obstacles
    obstacles = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > WIDTH // 4:
            car_x -= car_speed
        if keys[pygame.K_RIGHT] and car_x < WIDTH - CAR_WIDTH - WIDTH // 4:
            car_x += car_speed

        if random.randint(1, 20) == 1:
            obstacles.append(create_obstacle())
        
        move_obstacles(obstacles)
        
        if check_collision(car_x, car_y, obstacles):
            print("Game Over")
            pygame.quit()
            sys.exit()
        
        obstacles = [obs for obs in obstacles if obs[1] < HEIGHT]

        screen.fill(WHITE)
        draw_road()
        draw_car(car_x, car_y)
        draw_obstacles(obstacles)
        
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    game_loop()
