# pygame-basic-shapes
# Henry Roeser
# 2/24/25

import pygame
import sys
import config


def init_game():  # Initialize game screen
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen


# Function to draw a rectangle
def draw_rectangle(screen, rect, color, thickness):  # Draws a rectangle on the pygame window
    pygame.draw.rect(screen, color, rect, thickness)


# Function to draw a circle
def draw_circle(screen, center, radius, color, thickness):  # Draws a circle on the pygame window
    pygame.draw.circle(screen, color, center, radius, thickness)


# Function to draw a line
def draw_line(screen, color, start_pos, end_pos, thickness):  # Draws a line on the pygame window
    pygame.draw.line(screen, color, start_pos, end_pos, thickness)


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False  # Return False to indicate quitting
    return True  # Continue running if no quit event



def draw_text(screen, text, font, text_col, x, y, bold=True, italic=True):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# Function to draw a polygon
def draw_polygon(screen, color, points, thickness = 0): # default thickness of 0 will fill the polygon with color
    pygame.draw.polygon(screen, color, points, thickness)

def main():
    screen = init_game()
    clock = pygame.time.Clock()  # Initialize the clock

    text_font1 = pygame.font.SysFont('Arial', 30, bold = False, italic = True) # System font

    text_font2 = pygame.font.Font('FreeMono.ttf', 50)

    text_font3 = pygame.font.SysFont('Times New Roman', 55, bold = True, italic = True) # System font

    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE)  # Use color from config
        
        # Call the function as many times as needed to draw different
        # messages on the Pygame window

        draw_text(screen, 'Hello World', text_font1, config.ORANGE, 220, 150, bold=True, italic=False)

        draw_text(screen, 'Henry was here!',text_font2, config.PURPLE, 120, 225, bold=False, italic=False)

        draw_text(screen, 'Good afternoon, Henry!',text_font3, config.RED, 400, 500, bold=True, italic=True)



        # update the window display
        pygame.display.flip()

        clock.tick(config.FPS)  # Use the clock to control the frame rate

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

