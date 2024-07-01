import pygame
pygame.init()

# Размер, название
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Тестовый экран")

# Изображения
image = pygame.image.load("")
image_rect = image.get_rect()

run = True

#Цикл пока экран не закроют на крестик
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    #Экран
    screen.fill((0, 0, 0))
    screen.blit(image, image_rect)
    pygame.display.flip()

pygame.quit()
