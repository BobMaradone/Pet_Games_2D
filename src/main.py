import pygame
import sys

def main():
    # 1. Инициализация PyGame
    pygame.init()
    
    # 2. Создание окна (ширина, высота)
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Моя 2D RPG")  # Название в заголовке окна
    
    # 3. Игровые часы (для контроля FPS)
    clock = pygame.time.Clock()
    
    # 4. Цвет фона (R, G, B)
    background_color = (40, 40, 60)  # Тёмно-синий
    
    # 5. ГЛАВНЫЙ ИГРОВОЙ ЦИКЛ
    running = True
    while running:
        # 5.1. Обработка событий (нажатия клавиш, закрытие окна)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False  # Выход по Esc
        
        # 5.2. "Очистка" экрана — заливка цветом фона
        screen.fill(background_color)
        
        # 5.3. ЗДЕСЬ ПОТОМ БУДЕТ ОТРИСОВКА ИГРОКА, ВРАГОВ, ПРЕДМЕТОВ
        
        # 5.4. Обновление экрана (показ нарисованного)
        pygame.display.flip()
        
        # 5.5. Поддержка 60 кадров в секунду
        clock.tick(60)
    
    # 6. Корректное завершение
    pygame.quit()
    sys.exit()

# Стандартная проверка для запуска
if __name__ == "__main__":
    main()