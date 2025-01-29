import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 16

# Load images
grass_image = pygame.image.load('assets/images/backgrounds/Grass_Middle.png')

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Bullet Heaven')

# Function to draw the world
def draw_world():
    for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
        for x in range(0, SCREEN_WIDTH, TILE_SIZE):
            screen.blit(grass_image, (x, y))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the world
    draw_world()

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
# Load player spritesheet
player_spritesheet = pygame.image.load('assets/images/player/player.png')

# Function to get a specific frame from the spritesheet
def get_frame(sheet, frame, width, height):
    image = pygame.Surface((width, height), pygame.SRCALPHA)
    image.blit(sheet, (0, 0), (frame * width, 0, width, height))
    return image

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.frames = [get_frame(player_spritesheet, i, 32, 32) for i in range(6)]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.animation_timer = 0
        self.animation_speed = 100  # milliseconds per frame

    def update(self, dt):
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]

# Create player instance
player = Player()
player_group = pygame.sprite.Group(player)

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    dt = clock.tick(60)  # milliseconds since last frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the world
    draw_world()

    # Update and draw the player
    player_group.update(dt)
    player_group.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()