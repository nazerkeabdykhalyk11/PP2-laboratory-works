import pygame
import math

def main():
    pygame.init()
    
    # Create the main window and canvas surface
    screen = pygame.display.set_mode((640, 480))
    canvas = pygame.Surface(screen.get_size())  # Persistent drawing surface
    canvas.fill((0, 0, 0))  # Fill canvas with black color
    clock = pygame.time.Clock()
    
    # Variables
    radius = 15              # Size of brush/eraser/shapes
    mode = 'blue'            # Default color
    tool = 'brush'           # Default tool
    drawing = False          # Drawing flag
    points = []              # List of brush points for smooth drawing
    
    while True:
        # Check for modifier keys (for shortcuts)
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            # Exit conditions
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_w and ctrl_held) or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_F4 and alt_held) or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return

            # Tool and color selection via keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_c:
                    tool = 'circle'
                elif event.key == pygame.K_l:
                    tool = 'rectangle'
                elif event.key == pygame.K_e:
                    tool = 'eraser'
                elif event.key == pygame.K_p:
                    tool = 'brush'
                elif event.key == pygame.K_s:
                    tool = 'square'
                elif event.key == pygame.K_t:
                    tool = 'right_triangle'
                elif event.key == pygame.K_q:
                    tool = 'equilateral_triangle'
                elif event.key == pygame.K_h:
                    tool = 'rhombus'

            # Mouse button pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos  # Store initial position for shapes
                    if tool == 'brush':
                        points.append(event.pos)
                elif event.button == 3:  # Right click to decrease brush size
                    radius = max(1, radius - 1)

            # Mouse button released
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    end_pos = event.pos
                    color = getColor(mode)

                    # Draw shapes depending on selected tool
                    if tool == 'circle':
                        pygame.draw.circle(canvas, color, end_pos, radius)
                    elif tool == 'rectangle':
                        rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                        pygame.draw.rect(canvas, color, rect)
                    elif tool == 'square':
                        side = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                        rect = pygame.Rect(start_pos, (side, side))
                        pygame.draw.rect(canvas, color, rect)
                    elif tool == 'right_triangle':
                        x1, y1 = start_pos
                        x2, y2 = end_pos
                        points_tri = [(x1, y1), (x1, y2), (x2, y2)]
                        pygame.draw.polygon(canvas, color, points_tri)
                    elif tool == 'equilateral_triangle':
                        x1, y1 = start_pos
                        side = abs(end_pos[0] - x1)
                        height = int((math.sqrt(3)/2) * side)
                        points_eq = [(x1, y1), (x1 + side, y1), (x1 + side // 2, y1 - height)]
                        pygame.draw.polygon(canvas, color, points_eq)
                    elif tool == 'rhombus':
                        x1, y1 = start_pos
                        dx = abs(end_pos[0] - x1)
                        dy = abs(end_pos[1] - y1)
                        points_rh = [(x1, y1 - dy), (x1 - dx, y1), (x1, y1 + dy), (x1 + dx, y1)]
                        pygame.draw.polygon(canvas, color, points_rh)

            # Mouse is moving while button is held down
            if event.type == pygame.MOUSEMOTION and drawing:
                position = event.pos
                if tool == 'brush':
                    points.append(position)
                    if len(points) >= 2:
                        drawLineBetween(canvas, len(points)-2, points[-2], points[-1], radius, mode)
                elif tool == 'eraser':
                    pygame.draw.circle(canvas, (0, 0, 0), position, radius)

        # Display the canvas
        screen.blit(canvas, (0, 0))
        pygame.display.flip()
        clock.tick(60)

# Draw a smooth line between two points using circles
def drawLineBetween(surface, index, start, end, width, color_mode):
    # Create gradient color based on brush index and selected mode
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = i / iterations
        x = int((1 - progress) * start[0] + progress * end[0])
        y = int((1 - progress) * start[1] + progress * end[1])
        pygame.draw.circle(surface, color, (x, y), width)

# Get the RGB color based on the selected mode
def getColor(mode):
    if mode == 'blue':
        return (0, 0, 255)
    elif mode == 'red':
        return (255, 0, 0)
    elif mode == 'green':
        return (0, 255, 0)
    return (255, 255, 255)  # Default color is white

main()