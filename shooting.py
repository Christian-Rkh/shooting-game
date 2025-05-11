import pygame
import random
import sys


# 초기화
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("우주선 생존 슈터")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW= (255, 255, 0)

# FPS 설정
clock = pygame.time.Clock()
FPS = 60

# 플레이어 설정
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - 100
player_speed = 8
player_health = 3

# 탄환 설정
bullet_width = 5
bullet_height = 10
bullet_speed = -10
bullets = [] # 각 탄환: [x, y]

# 적 설정
enemy_width = 50
enemy_height = 50
enemy_speed = 3
enemy_list = [] # 각 적: [x, y]

# 점수 및 폰트
score = 0
font = pygame.font.SysFont("Arial", 24)

# 아이템 설정
items = [] # 각 아이템: [x, y]
def game_loop():
    global player_x, bullets
    running = True
    while running:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
            player_x += player_speed
        if keys[pygame.K_SPACE]:
            if len(bullets) < 5:
                bullets.append([player_x + player_size // 2, player_y])

        pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

        bullets = [[b[0], b[1] + bullet_speed] for b in bullets if b[1] > 0]

        for b in bullets:
            pygame.draw.rect(screen, YELLOW, (b[0], b[1], bullet_width, bullet_height))

        pygame.display.flip()
        clock.tick(60)
    
game_loop()

pygame.quit()
sys.exit()
