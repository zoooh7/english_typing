import pygame
import sys
from random import *

#기본 초기화
pygame.init()#pygame 리셋

# 화면 크기 설정
screen_width = 1000#가로 길이
screen_height = 640#세로 길이
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("영타연습")# 게임 이름

# FPS
clock = pygame.time.Clock()

score = 0 # 초기 점수

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/오주현/Desktop/python workspace/pygame_basic/background.png")

# 폰트 설정
font = pygame.font.Font(None, 36)

# 미리 입력한 문자열
predefined_string = "HelloWorld"
user_input = ""
score = 0
typing = False

def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# 문자열 속도와 위치 설정
string_speed = 2
string_x = 400
string_y = 0

enemy = predefined_string
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0] #캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = randint(0,screen_width-enemy_width)  #랜덤한 위치
enemy_y_pos = 0

running = True
while running:
    for event in pygame.event.get():
        enemy_y_pos += 0.5 * dt
    if enemy_y_pos >= screen_height:
        enemy_x_pos = randint(0,screen_width-enemy_width)
        enemy_y_pos = 0
        score += 1000
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
                running = False
        elif typing:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.key == pygame.K_RETURN:
                if user_input == predefined_string:
                    score += 1
                user_input = ""
            else:
                user_input += event.unicode

    screen.fill((0,0,0))

    if typing:
        draw_text("TYPING...", (124,252,0), 10, 10)
        draw_text(predefined_string, (124,252,0), 10, 50)
        draw_text(user_input, (255,0,0), 10, 90)
    else:
        draw_text("영타 연습 게임", (124,252,0), 10, 10)
        draw_text("PRESS ENTER.", (124,252,0), 10, 50)

    draw_text(f"점수: {score}", (124,252,0), 10, screen_height - 40)

    pygame.display.flip()

    if not typing and pygame.key.get_pressed()[pygame.K_RETURN]:
        typing = True

# 게임 종료
pygame.quit()
sys.exit()