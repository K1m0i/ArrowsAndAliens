import pygame
from elf import Elf
from alien import Alien

pygame.init()

# colors
WHITE = (255, 255, 255)

# window
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("ArrowsAndAliens")

# Background
background = pygame.image.load("images/background.png")

player = Elf(WHITE, 40, 40)
player.rect.x = 300
player.rect.y = 420

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)

carryOn = True
clock = pygame.time.Clock()

while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                carryOn = False

    # Moving the player model when the user uses the "A/D" keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.moveLeft(5)
    if keys[pygame.K_d]:
        player.moveRight(5)

    # --- Game logic should go here
    all_sprites_list.update()

    # --- Drawing code should go here
    # Background fill
    screen.blit(background, (0, 0))

    # Now let's draw all the sprites in one go
    all_sprites_list.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
