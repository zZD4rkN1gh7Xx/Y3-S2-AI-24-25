import pygame
import pygame.locals
import matplotlib.pyplot as plt
import csv
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import sys

WIDTH = 800
HEIGHT = 550

def show_bot_statistics(screen):
    board_sizes = []
    algorithms = []
    times = []
    memory_usage = []  
    num_moves = []  # List to store the number of moves

    with open("bot_performance.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                board_sizes.append(int(row[0]))  
                algorithms.append(row[1])       
                times.append(float(row[2]))     
                memory_usage.append(float(row[3]))  
                # Extract the number of moves from the solution string
                moves_str = row[4] if len(row) > 4 else ""
                if moves_str == "No solution":
                    num_moves.append(0)  # No solution means 0 moves
                else:
                    num_moves.append(len(moves_str.split("; ")))  # Count the number of moves
            except ValueError:
                print(f"Skipping invalid row: {row}")

    # Use the Agg backend to render plots to a surface
    plt.switch_backend('Agg')

    # Create the first plot (Time)
    fig1, ax1 = plt.subplots(figsize=(WIDTH / 100, HEIGHT / 100))  # Adjust figure size to fit the Pygame window
    unique_algorithms = list(set(algorithms))
    colors = plt.cm.get_cmap("tab10", len(unique_algorithms))
    for i, algo in enumerate(unique_algorithms):
        x = [board_sizes[j] for j in range(len(algorithms)) if algorithms[j] == algo]
        y = [times[j] for j in range(len(algorithms)) if algorithms[j] == algo]
        ax1.scatter(x, y, label=algo, color=colors(i))
    ax1.set_xlabel("Board Size")
    ax1.set_ylabel("Time (seconds)")
    ax1.set_title("Algorithm Performance by Board Size (Time)")
    ax1.legend()

    # Render the first plot to a Pygame surface
    canvas1 = FigureCanvas(fig1)
    canvas1.draw()
    renderer1 = canvas1.get_renderer()
    raw_data1 = renderer1.tostring_argb()  # Use tostring_argb() instead of tostring_rgb()
    size1 = canvas1.get_width_height()
    surf1 = pygame.image.fromstring(raw_data1, size1, "ARGB")  # Use "ARGB" format

    # Resize the surface to fit the Pygame window
    surf1 = pygame.transform.scale(surf1, (WIDTH, HEIGHT))

    # Create the second plot (Memory Usage)
    fig2, ax2 = plt.subplots(figsize=(WIDTH / 100, HEIGHT / 100))  # Adjust figure size to fit the Pygame window
    for i, algo in enumerate(unique_algorithms):
        x = [board_sizes[j] for j in range(len(algorithms)) if algorithms[j] == algo]
        y = [memory_usage[j] for j in range(len(algorithms)) if algorithms[j] == algo]
        ax2.scatter(x, y, label=algo, color=colors(i))
    ax2.set_xlabel("Board Size")
    ax2.set_ylabel("Memory Usage (MB)")
    ax2.set_title("Algorithm Performance by Board Size (Memory Usage)")
    ax2.legend()

    # Render the second plot to a Pygame surface
    canvas2 = FigureCanvas(fig2)
    canvas2.draw()
    renderer2 = canvas2.get_renderer()
    raw_data2 = renderer2.tostring_argb()  # Use tostring_argb() instead of tostring_rgb()
    size2 = canvas2.get_width_height()
    surf2 = pygame.image.fromstring(raw_data2, size2, "ARGB")  # Use "ARGB" format

    # Resize the surface to fit the Pygame window
    surf2 = pygame.transform.scale(surf2, (WIDTH, HEIGHT))

    # Create the third plot (Number of Moves)
    fig3, ax3 = plt.subplots(figsize=(WIDTH / 100, HEIGHT / 100))  # Adjust figure size to fit the Pygame window
    for i, algo in enumerate(unique_algorithms):
        x = [board_sizes[j] for j in range(len(algorithms)) if algorithms[j] == algo]
        y = [num_moves[j] for j in range(len(algorithms)) if algorithms[j] == algo]
        ax3.scatter(x, y, label=algo, color=colors(i))
    ax3.set_xlabel("Board Size")
    ax3.set_ylabel("Number of Moves")
    ax3.set_title("Algorithm Performance by Board Size (Number of Moves)")
    ax3.legend()

    # Render the third plot to a Pygame surface
    canvas3 = FigureCanvas(fig3)
    canvas3.draw()
    renderer3 = canvas3.get_renderer()
    raw_data3 = renderer3.tostring_argb()  # Use tostring_argb() instead of tostring_rgb()
    size3 = canvas3.get_width_height()
    surf3 = pygame.image.fromstring(raw_data3, size3, "ARGB")  # Use "ARGB" format

    # Resize the surface to fit the Pygame window
    surf3 = pygame.transform.scale(surf3, (WIDTH, HEIGHT))

    # Display the first plot
    screen.fill((0, 0, 0))  # Clear the screen
    screen.blit(surf1, (0, 0))  # Display the first plot
    pygame.display.update()

    # Wait for a mouse click to switch to the second plot
    waiting_for_click = True
    while waiting_for_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click
                waiting_for_click = False

    # Display the second plot
    screen.fill((0, 0, 0))  # Clear the screen
    screen.blit(surf2, (0, 0))  # Display the second plot
    pygame.display.update()

    # Wait for a mouse click to switch to the third plot
    waiting_for_click = True
    while waiting_for_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click
                waiting_for_click = False

    # Display the third plot
    screen.fill((0, 0, 0))  # Clear the screen
    screen.blit(surf3, (0, 0))  # Display the third plot
    pygame.display.update()

    # Wait for a mouse click to exit the statistics screen
    waiting_for_click = True
    while waiting_for_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click
                waiting_for_click = False

    # Clean up
    plt.close(fig1)
    plt.close(fig2)
    plt.close(fig3)