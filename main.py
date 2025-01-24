import pygame
import random
import math

# Define the characters and their 2D representations
characters = {
    '0': [
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111'
    ],
    '1': [
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111',
        '11111'
    ],
    '2': [
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '11111          ',
        '11111          ',
        '11111          ',
        '11111          ',
        '11111          ',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111'
    ],
    '3': [
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111'
    ],
    '4': [
        '11111          ',
        '11111     ',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111'
    ],
    '5': [
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '11111          ',
        '11111          ',
        '11111          ',
        '11111          ',
        '11111          ',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111'

    ],
    '6': [
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '11111          ',
        '11111          ',
        '11111          ',
        '11111          ',
        '11111          ',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111'
    ],
    '7': [
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
    ],
    '8': [
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',

    ],
    '9': [
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '11111     11111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '          11111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
        '111111111111111',
    ]
}
pygame.init()  # Initialize pygame

# Set up the window
window_width = 500
window_height = 500

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Animate Number Shapes in 3D")

# window colors
window_color = (0, 0, 0)
character_color = (255, 255, 255)

# rotation speeds
x_rspeed = random.uniform(0.005, 0.025)
y_rspeed = random.uniform(0.005, 0.025)
z_rspeed = random.uniform(0.005, 0.025)

# Getting user input
character = input("Enter the numerical character you want: ")

# Define the initial rotation angles
x_angle = 0
y_angle = 0
z_angle = 0

# Define pause states for each number
pause_states = {char: False for char in characters.keys()}

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                character = input("Enter the numerical character you want: ")
            elif event.key == pygame.K_p:  # Press 'p' key to pause/resume
                pause_states[character] = not pause_states[character]

    if not pause_states[character]:
        # Clear the screen
        window.fill(window_color)

        # Rotate the 2D character and draw the 3D representation
        for i, line in enumerate(characters[character]):
            for j, char in enumerate(line):
                if char == '1':
                    # Draw 5 points for each character depth
                    for depth in range(5):
                        # Calculate the 3D coordinates based on the rotation angles
                        x = j - len(line) / 2
                        y = i - len(characters[character]) / 2
                        z = depth - 2  # Adjust the depth

                        # Rotate around the x-axis
                        y_rotated = y * math.cos(x_angle) - z * math.sin(x_angle)
                        z_rotated = y * math.sin(x_angle) + z * math.cos(x_angle)

                        # Rotate around the y-axis
                        x_rotated = x * math.cos(y_angle) + z_rotated * math.sin(y_angle)
                        z_rotated = -x * math.sin(y_angle) + z_rotated * math.cos(y_angle)

                        # Rotate around the z-axis
                        x_rotated_final = x_rotated * math.cos(z_angle) - y_rotated * math.sin(z_angle)
                        y_rotated_final = x_rotated * math.sin(z_angle) + y_rotated * math.cos(z_angle)

                        # Convert the 3D coordinates to 2D screen coordinates
                        scale = 10
                        x_screen = int(x_rotated_final * scale + window_width / 2)
                        y_screen = int(y_rotated_final * scale + window_height / 2)

                        # Draw the point
                        pygame.draw.line(window, character_color, (x_screen, y_screen), (x_screen, y_screen))

        # Update the rotation angles
        x_angle += x_rspeed
        y_angle += y_rspeed
        z_angle += z_rspeed

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit the program
pygame.quit()