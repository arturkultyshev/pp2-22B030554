import pygame
pygame.init()
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))
font = pygame.font.SysFont("Verdana", 15)
current_color = BLACK


# фунция для рисования прямой линии
def drawline(screen, x, y):
    pygame.draw.circle(screen, current_color, (x, y), 5)


# функция для рисования круга
def drawcircle(screen, x, y):
    pygame.draw.circle(screen, current_color, (x, y), 20)
    return False


# главная функция игры, в которой реализовано изменение цвета, считывание координатов мышки
isPressed = False
running = True
while running:
    (x, y) = pygame.mouse.get_pos()
    sample_text = 'Red - r, ' + 'Blue - b, ' + 'Green - g, ' + 'Black - l, ' + 'Eraser - e'
    text = font.render(sample_text, True, (0, 0, 0))
    screen.blit(text, (0, 0))
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_r]:
        current_color = RED
    if pressed[pygame.K_b]:
        current_color = BLUE
    if pressed[pygame.K_g]:
        current_color = GREEN
    if pressed[pygame.K_l]:
        current_color = BLACK
    if pressed[pygame.K_e]:
        current_color = WHITE

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if isPressed and event.type == pygame.MOUSEMOTION and 0 < x < 500 and 0 < y < 500:
            drawline(screen, x, y)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            isPressed = True
            (x, y) = pygame.mouse.get_pos()
            drawcircle(screen, x, y)
        elif event.type == pygame.MOUSEBUTTONUP:
            isPressed = False

    pygame.display.flip()
