import pygame
import random
import sys


# 초기화
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step05. score system and item")
# pygame.display.set_caption("우주선 생존 슈터")
clock = pygame.time.Clock()

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW= (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

items = []
item_timer = 0

# FPS 설정
clock = pygame.time.Clock()
FPS = 60

# 플레이어 설정
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - 100
player_speed = 8
player_health = 3
font = pygame.font.SysFont("Arial", 24)
WHITE = (255, 255, 255)

# 탄환 설정
bullet_width = 5
bullet_height = 10
bullet_speed = -10
bullets = [] # 각 탄환: [x, y]

enemy_width, enemy_height = 50, 50
enemy_speed = 3
enemy_list = []
enemy_timer = 0

player_health = 3
font = pygame.font.SysFont("Arial", 24)
WHITE = (255, 255, 255)

# 적 설정
enemy_width = 50
enemy_height = 50
enemy_speed = 3
enemy_list = [] # 각 적: [x, y]

def create_item():
    return [random.randint(0, WIDTH-30), 0]

def detect_collision(rect1, rect2):
    return rect1.colliderect(rect2)

# 점수 및 폰트
score = 0
font = pygame.font.SysFont("Arial", 24)

# 아이템 설정
items = [] # 각 아이템: [x, y]
def game_loop():
    global player_x, bullets, enemy_list, enemy_timer, player_health, items, item_timer, score

    running = True
    can_shoot = True  # 게임 시작할 때 한 번만 선언

    while running:
        screen.fill(BLACK)

        # 키 입력 (계속 누르고 있는 것)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
            player_x += player_speed

        # 이벤트 입력 (딱 한 번 발생하는 것)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and can_shoot:
                    if len(bullets) < 5:
                        bullets.append([player_x + player_size // 2, player_y])
                    can_shoot = False  # 한 번 쏘고 나면 다시 못 쏘게 막음

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    can_shoot = True  # 스페이스바 떼면 다시 발사 가능

        # 플레이어 그리기
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        pygame.draw.rect(screen, BLUE, player_rect)

        # 탄환 이동 및 그리기
        bullets = [[b[0], b[1] + bullet_speed] for b in bullets if b[1] > 0]
        for b in bullets:
            pygame.draw.rect(screen, YELLOW, (b[0], b[1], bullet_width, bullet_height))

        # 적 생성
        if enemy_timer == 0:
            x_pos = random.randint(0, WIDTH - enemy_width)
            enemy_list.append([x_pos, 0])
        enemy_timer = (enemy_timer + 1) % 30

        # 적 이동 및 그리기
        enemy_list = [[e[0], e[1] + enemy_speed] for e in enemy_list if e[1] < HEIGHT]
        for e in enemy_list:
            pygame.draw.rect(screen, RED, (e[0], e[1], enemy_width, enemy_height))

        
        for b in bullets[:]:
            bullet_rect = pygame.Rect(b[0], b[1], bullet_width, bullet_height)
            for e in enemy_list[:]:
                enemy_rect = pygame.Rect(e[0], e[1], enemy_width, enemy_height)
                if detect_collision(bullet_rect, enemy_rect):
                    bullets.remove(b)
                    enemy_list.remove(e)
                    score += 10
                    break

        if item_timer == 0:
            items.append(create_item())
        item_timer = (item_timer + 1) % 300
        items = [[i[0], i[1] + 3] for i in items if i[1] < HEIGHT]
        for i in items:
            pygame.draw.rect(screen, GREEN, (i[0], i[1], 30, 30))
        
        for it in items[:]:
            item_rect = pygame.Rect(it[0], it[1], 30, 30)
            if detect_collision(player_rect, item_rect):
                player_health += 1
                items.remove(it)



        for e in enemy_list[:]:
            enemy_rect = pygame.Rect(e[00], e[1], enemy_width, enemy_height)
            if detect_collision(player_rect, enemy_rect):
                player_health -= 1
                enemy_list.remove(e)
                if player_health <= 0:
                    running = False

        health_text = font.render(f"Health:{player_health}", True, WHITE)
        screen.blit(health_text, (10, 10))

        score_text = font.render(f"Score: {score}", True , WHITE)
        screen.blit(score_text, (10, 40))

        pygame.display.flip()
        clock.tick(FPS)
game_loop()

pygame.quit()
sys.exit()
