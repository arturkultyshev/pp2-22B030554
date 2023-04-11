import pygame
pygame.init()
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))
font = pygame.font.SysFont("Verdana", 15)
current_color = BLACK


# фунция для рисования прямой линии
def drawline(screen, x, y):
    pygame.draw.circle(screen, current_color, (x, y), 5)


# функция для рисования круга
def drawcircle(screen, x, y):
    pygame.draw.circle(screen, current_color, (x, y), 20)


def drawrectangle(screen, x, y):
    pygame.draw.rect(screen, current_color, pygame.Rect(x, y, 80, 40))


def drawsquare(screen, x, y):
    pygame.draw.rect(screen, current_color, pygame.Rect(x, y, 80, 80))


def drawrighttriangle(screen, x, y):
    pygame.draw.polygon(screen, current_color, ((x, y), (x + 80, y), (x, y - 80)))


def drawequilateraltriangle(screen, x, y):
    pygame.draw.polygon(screen, current_color, ((x, y), (x + 80, y), (x + 40, y - 40)))


def drawrhombus(screen, x, y):
    pygame.draw.polygon(screen, current_color, ((x, y), (x + 30, y - 50), (x + 60, y),  (x + 30, y + 50)))


def eraser(screen, x, y):
    pygame.draw.circle(screen, WHITE, (x, y), 20)

# главная функция игры, в которой реализовано изменение цвета, считывание координатов мышки
isPressed = False
running = True
ind = 0
funcs = ['line', 'eraser', 'circle', 'rectangle', 'square', 'equilateraltriangle', 'righttriangle', 'rhombus']
while running:
    current_func = funcs[ind]
    print(current_func)
    (x, y) = pygame.mouse.get_pos()

    sample_text = f"Red - r, Blue - b, Green - g, Black - l, current_func:{current_func}"
    text = font.render(sample_text, True, (0, 0, 0))
    pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, 530, 20))
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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if ind + 1 > len(funcs) - 1:
                ind = 0
            else:
                ind += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if ind - 1 < 0:
                ind = len(funcs) - 1
            else:
                ind -= 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            isPressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            isPressed = False
            (x, y) = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION and isPressed == True and current_func == 'line':
            (x, y) = pygame.mouse.get_pos()
            drawline(screen, x, y)
        if event.type == pygame.MOUSEMOTION and isPressed == True and current_func == 'eraser':
            (x, y) = pygame.mouse.get_pos()
            eraser(screen, x, y)

        if event.type == pygame.MOUSEBUTTONDOWN and 0 < x < 800 and 0 < y < 600 and current_func == 'circle':
            (x, y) = pygame.mouse.get_pos()
            drawcircle(screen, x, y)

        if event.type == pygame.MOUSEBUTTONDOWN and 0 < x < 800 and 0 < y < 600 and current_func == 'rectangle':
            (x, y) = pygame.mouse.get_pos()
            drawrectangle(screen, x, y)

        if event.type == pygame.MOUSEBUTTONDOWN and 0 < x < 800 and 0 < y < 600 and current_func == 'square':
            (x, y) = pygame.mouse.get_pos()
            drawsquare(screen, x, y)

        if event.type == pygame.MOUSEBUTTONDOWN and 0 < x < 800 and 0 < y < 600 and current_func == 'equilateraltriangle':
            (x, y) = pygame.mouse.get_pos()
            drawequilateraltriangle(screen, x, y)

        if event.type == pygame.MOUSEBUTTONDOWN and 0 < x < 800 and 0 < y < 600 and current_func == 'righttriangle':
            (x, y) = pygame.mouse.get_pos()
            drawrighttriangle(screen, x, y)

        if event.type == pygame.MOUSEBUTTONDOWN and 0 < x < 800 and 0 < y < 600 and current_func == 'rhombus':
            (x, y) = pygame.mouse.get_pos()
            drawrhombus(screen, x, y)

        if event.type == pygame.MOUSEBUTTONUP:
            isPressed = False

    pygame.display.flip()
