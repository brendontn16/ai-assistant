import pygame
import sys
import win32gui
import win32con
import win32api

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800 * 2, 600 * 2
screen = pygame.display.set_mode((width, height), pygame.NOFRAME)  # NOFRAME removes the window border
pygame.display.set_caption("Sliding Image Example")

# Load the image
image = pygame.image.load('YALO TITLE.png')
image_rect = image.get_rect()
image_rect.x = -image_rect.width
image_rect.y = height // 2 - image_rect.height // 2

# Get window handle and make it transparent
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0, 0, 0), 0, win32con.LWA_COLORKEY)

# Make window always stay on top
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, width, height, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with the transparent color
    screen.fill((0, 0, 0))

    # Update image position more quickly
    image_rect.x += 10  # Increase this value for faster movement

    if image_rect.x > width:
        image_rect.x = -image_rect.width  # Reset position

    # Draw the image
    screen.blit(image, image_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(75)

# Quit Pygame
pygame.quit()
sys.exit()






