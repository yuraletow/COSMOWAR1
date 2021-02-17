import pygame

successes, failures = pygame.init()
print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))

screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

running = True

image = pygame.Surface((32, 32))
image.fill(WHITE)
rect = image.get_rect()  # Отрисуем белый квадрат игрока
velocity = [0, 0]

while running:  # Игра работает в бесконечном цикле. Обрабатывает новые события по очереди.
    dt = clock.tick(FPS) / 1000 # Получаем время в секундах с прошлого события
    screen.fill(BLACK)  # Черный фон
    for event in pygame.event.get(): # Получаем новые события и обрабатываем их
        if event.type == pygame.QUIT: # Событие выхода из игры, ставим running=False, while остановится, игра закончится
            running = False
        elif event.type == pygame.KEYDOWN: # Если была нажата кнопка
            if event.key == pygame.K_w: # Этими ифами мы проверяем какая кнопка была нажата и меняем скорость игрока.
                velocity[1] = -200 * dt  # 200 пикселей в секунду по оси y(вторая позиция в списке). минус значит вверх
            elif event.key == pygame.K_s:
                velocity[1] = 200 * dt # по оси y вниз
            elif event.key == pygame.K_a:
                velocity[0] = -200 * dt # по оси x влево
            elif event.key == pygame.K_d:
                velocity[0] = 200 * dt # по оси x вправо
        elif event.type == pygame.KEYUP: # Если пользователь отпустил кнопку, то ставим скорость по соответсвующей оси = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                velocity[1] = 0
            elif event.key == pygame.K_a or event.key == pygame.K_d:
                velocity[0] = 0

    rect.move_ip(velocity) # Двигаем игрока с соответсвующей скоростью

    screen.blit(image, rect) # обновляем экран
    pygame.display.update()

print("Выходим из игры")
quit()

if not 0<=image.left <=720:
    velocity[1]=0
if not 0<=image.top <=720:
    velocity[1]=0