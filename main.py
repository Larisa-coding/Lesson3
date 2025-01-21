import pygame
import random
import time

pygame.init()
# Константы экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Установка заголовка и иконки
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/images.jpeg")
pygame.display.set_icon(icon)

# Загрузка изображения мишени
target_image = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

# Начальные координаты мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Счет
score = 0
font = pygame.font.Font(None, 36)

# Время игры и таймер
start_time = time.time()
game_duration = 30  # игра длится 30 секунд

# Функция для отображения текста на экране
def display_text(text, x, y):
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (x, y))
    

pygame.quit