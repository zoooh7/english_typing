import pygame
import sys
import csv
from random import *

import time

# 초기화
pygame.init()

# 화면 크기 및 색상 정의
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
GREEN = (123, 255, 0)
RED = (255, 0, 0)

# 문자열 속도와 위치 설정
string_speed = 0.1
string_x = randint(100,700)
string_y = 0

# 화면 설정
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("영타 연습 게임")

clock = pygame.time.Clock()

# 폰트 설정
font = pygame.font.Font(None, 36)

# 미리 입력한 문자열
predefined_string = []
word_file = open(r"C:\Users\오주현\Documents\wordforgame.txt", "r", encoding = "utf8")
while True:
    line = word_file.readline()
    if not line:
        break
    else:
        line = line.strip()
        line = line.lower()
        predefined_string.append(line)
word_file.close()
user_input = ""

score = 0
miss = 0
global level
level = 1
global typing
typing = False

writing_string = sample(predefined_string,1)[0]


def draw_text(text, color, x, y):
    text_surface = font.render(str(text), True, color)
    screen.blit(text_surface, (x, y))


#레벨 넘어가도록 하는 함수->작동 안됨(수정 필요)
# 이 함수에서 사용하는 변수? : level, string_speed, *DELAY*, WIDTH, HEIGHT, miss
# 문제점 : 레벨이 넘어간 이후 화면 플립이 2초마다 됨->DELAY 걸어둔게 계속 루프에 걸리는듯 -> 루프 탈출 방안 필요
# 이 또한 첫 번째 단어에서만 해결하면 됨
# 계속 else 구문이 돌아가는 이유? if delay가 아니기 때문에 else로 넘어와서 처리됨
def check_delay(level, DELAY):
    print(level, DELAY)
    if DELAY == True:
        typing = True
    else:
        DELAY = True
        draw_text(f"Level {level}", GREEN, WIDTH/2-30, HEIGHT/2)
        miss = 0
        
        global string_speed
        string_speed += 0.25
        level += 1
        
        pygame.display.flip()
        pygame.time.delay(2000)
    print(level, DELAY,  "\n")
    return

#전체 작동 프로그램
global DELAY
running = True
DELAY = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif typing:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key == pygame.K_RETURN:
                    if user_input == writing_string:
                        score += 1
                        string_x = randint(100,700)
                        string_y = 0
                        writing_string = sample(predefined_string,1)[0]
                    else:
                        miss += 1
                        string_x = randint(100,700)
                        string_y = 0
                        writing_string = sample(predefined_string,1)[0]
                    user_input = ""
                else:
                    user_input += event.unicode


# ###목표!!###
# if score % 10 == 0:
#     check_delay(1 + score / 10, DELAY)
# #이런식으로 10 레벨마다는 알아서 레벨 올라가게끔

#레벨 구별하기
    if score == 3:
        check_delay(1, DELAY)
    elif score == 6:
        check_delay(2, DELAY)
    elif score == 30:
        check_delay(3, DELAY)
    else:
        DELAY = False

    if miss == 5:
        draw_text("FAIL", RED, WIDTH/2-30, HEIGHT/2)
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False


    screen.fill(BLACK)
#게임 시작 후 화면 표시
    if typing:
        draw_text("TYPING...", GREEN, 10, 10)
        draw_text(user_input, RED, 10, 50)
#첫 화면 표시
    else:
        draw_text("ENGLISH TYPING GAME", GREEN, 10, 10)
        draw_text("PRESS ENTER TO START.", GREEN, 10, 50)
        draw_text("LEVEL 1~4", GREEN, WIDTH/3, HEIGHT/2-30)
        draw_text("MISS 5 TIMES = FAIL", GREEN, WIDTH/3, HEIGHT/2)
        draw_text("MISSES WILL BE RESETTED EACH LEVEL", GREEN, WIDTH/3, HEIGHT/2+30)

#게임중 화면 표시
    draw_text(f"score: {score}", GREEN, 10, HEIGHT - 40)
    draw_text(f"miss: {miss}", GREEN, 10, HEIGHT - 70)
    draw_text(f"level: {level}", GREEN, 10, HEIGHT - 500)


    # 문자열을 아래로 이동
    if typing:
        string_y += string_speed
        if string_y > HEIGHT:
            string_x = randint(0,WIDTH)
            string_y = 0
            writing_string = sample(predefined_string, 1)[0]# 다음 문자열로 교체
            miss += 1
        draw_text(writing_string, GREEN, string_x, string_y)

    pygame.display.flip()

    if not typing and pygame.key.get_pressed()[pygame.K_RETURN]:
        typing = True

# 게임 종료
pygame.quit()
sys.exit()