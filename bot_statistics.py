import pygame
import pygame.locals
import matplotlib.pyplot as plt
import csv
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import sys
from collections import defaultdict

WIDTH = 800
HEIGHT = 550

def compute_averages(data):
    averages = {}
    for key, values in data.items():
        avg_time = sum(values['times']) / len(values['times'])
        avg_memory = sum(values['memory_usage']) / len(values['memory_usage'])
        avg_moves = sum(values['num_moves']) / len(values['num_moves'])
        averages[key] = (avg_time, avg_memory, avg_moves)
    return averages

def show_bot_statistics(screen):
    data = defaultdict(lambda: {'times': [], 'memory_usage': [], 'num_moves': []})
    
    with open("bot_performance.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                board_size = int(row[0])
                algorithm = row[1]
                time = float(row[2])
                memory = float(row[3])
                
                moves_str = row[4] if len(row) > 4 else ""
                num_moves = 0 if moves_str == "No solution" else len(moves_str.split("; "))
                
                data[(algorithm, board_size)]['times'].append(time)
                data[(algorithm, board_size)]['memory_usage'].append(memory)
                data[(algorithm, board_size)]['num_moves'].append(num_moves)
            except ValueError:
                print(f"Skipping invalid row: {row}")
    
    averages = compute_averages(data)
    
    plt.switch_backend('Agg')
    
    unique_algorithms = set(algorithm for algorithm, _ in averages.keys())
    colors = plt.cm.get_cmap("tab10", len(unique_algorithms))
    
    # Create the first plot (Time)
    fig1, ax1 = plt.subplots(figsize=(WIDTH / 100, HEIGHT / 100))
    for i, algo in enumerate(unique_algorithms):
        x, y = zip(*[(bs, avg[0]) for (alg, bs), avg in averages.items() if alg == algo])
        ax1.scatter(x, y, label=algo, color=colors(i))
    ax1.set_xlabel("Board Size")
    ax1.set_ylabel("Average Time (seconds)")
    ax1.set_title("Algorithm Performance by Board Size (Time)")
    ax1.legend()
    
    # Create the second plot (Memory Usage)
    fig2, ax2 = plt.subplots(figsize=(WIDTH / 100, HEIGHT / 100))
    for i, algo in enumerate(unique_algorithms):
        x, y = zip(*[(bs, avg[1]) for (alg, bs), avg in averages.items() if alg == algo])
        ax2.scatter(x, y, label=algo, color=colors(i))
    ax2.set_xlabel("Board Size")
    ax2.set_ylabel("Average Memory Usage (MB)")
    ax2.set_title("Algorithm Performance by Board Size (Memory Usage)")
    ax2.legend()
    
    # Create the third plot (Number of Moves)
    fig3, ax3 = plt.subplots(figsize=(WIDTH / 100, HEIGHT / 100))
    for i, algo in enumerate(unique_algorithms):
        x, y = zip(*[(bs, avg[2]) for (alg, bs), avg in averages.items() if alg == algo])
        ax3.scatter(x, y, label=algo, color=colors(i))
    ax3.set_xlabel("Board Size")
    ax3.set_ylabel("Average Number of Moves")
    ax3.set_title("Algorithm Performance by Board Size (Number of Moves)")
    ax3.legend()
    
   
    def plot_to_surface(fig):
        canvas = FigureCanvas(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_argb()
        size = canvas.get_width_height()
        surface = pygame.image.fromstring(raw_data, size, "ARGB")
        return pygame.transform.scale(surface, (WIDTH, HEIGHT))
    
    surf1, surf2, surf3 = plot_to_surface(fig1), plot_to_surface(fig2), plot_to_surface(fig3)
    
    for surf in [surf1, surf2, surf3]:
        screen.fill((0, 0, 0))
        screen.blit(surf, (0, 0))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    break
            else:
                continue
            break
    
    plt.close(fig1)
    plt.close(fig2)
    plt.close(fig3)