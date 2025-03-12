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
    num_moves = []  

    with open("bot_performance.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                board_sizes.append(int(row[0]))  
                algorithms.append(row[1])       
                times.append(float(row[2]))     
                memory_usage.append(float(row[3]))  
                
                moves_str = row[4] if len(row) > 4 else ""
                if moves_str == "No solution":
                    num_moves.append(0)  
                else:
                    num_moves.append(len(moves_str.split("; ")))  
            except ValueError:
                print(f"Skipping invalid row: {row}")

    plt.switch_backend('Agg')

    # Create the first plot (Time)
    fig1, ax1 = plt.subplots(figsize=(WIDTH / 100, HEIGHT / 100)) 
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

    canvas1 = FigureCanvas(fig1)
    canvas1.draw()
    renderer1 = canvas1.get_renderer()
    raw_data1 = renderer1.tostring_argb()  
    size1 = canvas1.get_width_height()
    surf1 = pygame.image.fromstring(raw_data1, size1, "ARGB") 

    surf1 = pygame.transform.scale(surf1, (WIDTH, HEIGHT))

    # Create the second plot (Memory Usage)
    fig2, ax2 = plt.subplots(figsize=(WIDTH / 100, HEIGHT / 100))  
    for i, algo in enumerate(unique_algorithms):
        x = [board_sizes[j] for j in range(len(algorithms)) if algorithms[j] == algo]
        y = [memory_usage[j] for j in range(len(algorithms)) if algorithms[j] == algo]
        ax2.scatter(x, y, label=algo, color=colors(i))
    ax2.set_xlabel("Board Size")
    ax2.set_ylabel("Memory Usage (MB)")
    ax2.set_title("Algorithm Performance by Board Size (Memory Usage)")
    ax2.legend()

    canvas2 = FigureCanvas(fig2)
    canvas2.draw()
    renderer2 = canvas2.get_renderer()
    raw_data2 = renderer2.tostring_argb() 
    size2 = canvas2.get_width_height()
    surf2 = pygame.image.fromstring(raw_data2, size2, "ARGB")  

    surf2 = pygame.transform.scale(surf2, (WIDTH, HEIGHT))

    # Create the third plot (Number of Moves)
    fig3, ax3 = plt.subplots(figsize=(WIDTH / 100, HEIGHT / 100)) 
    for i, algo in enumerate(unique_algorithms):
        x = [board_sizes[j] for j in range(len(algorithms)) if algorithms[j] == algo]
        y = [num_moves[j] for j in range(len(algorithms)) if algorithms[j] == algo]
        ax3.scatter(x, y, label=algo, color=colors(i))
    ax3.set_xlabel("Board Size")
    ax3.set_ylabel("Number of Moves")
    ax3.set_title("Algorithm Performance by Board Size (Number of Moves)")
    ax3.legend()

    canvas3 = FigureCanvas(fig3)
    canvas3.draw()
    renderer3 = canvas3.get_renderer()
    raw_data3 = renderer3.tostring_argb()
    size3 = canvas3.get_width_height()
    surf3 = pygame.image.fromstring(raw_data3, size3, "ARGB") 

    surf3 = pygame.transform.scale(surf3, (WIDTH, HEIGHT))

    # Display the first plot
    screen.fill((0, 0, 0))  
    screen.blit(surf1, (0, 0))  
    pygame.display.update()

    # Wait for a mouse click to switch to the second plot
    waiting_for_click = True
    while waiting_for_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  
                waiting_for_click = False

    # Display the second plot
    screen.fill((0, 0, 0))  
    screen.blit(surf2, (0, 0)) 
    pygame.display.update()

    # Wait for a mouse click to switch to the third plot
    waiting_for_click = True
    while waiting_for_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  
                waiting_for_click = False

    # Display the third plot
    screen.fill((0, 0, 0))  
    screen.blit(surf3, (0, 0)) 
    pygame.display.update()

    # Wait for a mouse click to exit the statistics screen
    waiting_for_click = True
    while waiting_for_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  
                waiting_for_click = False

    plt.close(fig1)
    plt.close(fig2)
    plt.close(fig3)