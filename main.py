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
    
# Основной игровой цикл
running = True
while running:
    screen.fill(color)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1  # Увеличиваем счет
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Меняем цвет фона

    # Отображение мишени
    screen.blit(target_image, (target_x, target_y))

    # Отображение счета
    display_text(f"Счет: {score}", 10, 10)

    # Таймер
    elapsed_time = time.time() - start_time
    remaining_time = max(game_duration - elapsed_time, 0)
    display_text(f"Время: {int(remaining_time)}", 700, 10)

    # Обновление экрана
    pygame.display.update()

    # Завершение игры по истечении времени
    if remaining_time <= 0:
        running = False

# Вывод финального счета
print(f"Игра окончена! Ваш счет: {score}")
pygame.quit