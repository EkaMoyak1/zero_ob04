import pygame
pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()
pygame.display.set_caption("Тестовый проект")
image = pygame.image.load("img/image.jpg")
image = pygame.transform.scale(image, (100, 100))
image_rect = image.get_rect()
speed = 5

image2 = pygame.image.load("img/image2.jpg")
image2 = pygame.transform.scale(image2, (100, 100))
image2_rect = image2.get_rect()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            image_rect.x = mouse_x - image_rect.width // 2
            image_rect.y = mouse_y - image_rect.height // 2

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        image_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        image_rect.x += speed
    if keys[pygame.K_UP]:
        image_rect.y -= speed
    if keys[pygame.K_DOWN]:
        image_rect.y += speed

    if image_rect.left < 0:
        image_rect.left = 0
    if image_rect.right > window_size[0]:
        image_rect.right = window_size[0]
    if image_rect.top < 0:
        image_rect.top = 0
    if image_rect.bottom > window_size[1]:
        image_rect.bottom = window_size[1]

    if image_rect.colliderect(image2_rect):
        image_rect.x = 0
        image_rect.y = 0

    screen.fill((0, 0, 0))
    screen.blit(image, image_rect)
    screen.blit(image2, image2_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

