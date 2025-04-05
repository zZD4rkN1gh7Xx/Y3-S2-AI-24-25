import pygame
import matplotlib.pyplot as plt
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
    
    heuristic_time_data = defaultdict(list)
    
    #target algorithmsfor heuristics
    target_algorithms = ["A*", "Greedy", "Weighted A*"]
    
    with open("bot_performance.csv", "r") as file:
        file_contents = file.read()
    
    lines = file_contents.strip().split('\n')
    for line in lines:
        parts = line.split(',')
        
        if len(parts) >= 5:
            try:
                board_size = int(parts[0])
                algorithm = parts[1]
                time = float(parts[2])
                memory = float(parts[3])
                
                # Try to get the heuristic (last value)
                last_part = parts[-1].strip()
                if last_part.isdigit():
                    heuristic = int(last_part)
                    
                    moves_str = ','.join(parts[4:-1])
                    num_moves = 0 if moves_str == "No solution" else len(moves_str.split("; "))
                    
                    data[(algorithm, board_size)]['times'].append(time)
                    data[(algorithm, board_size)]['memory_usage'].append(memory)
                    data[(algorithm, board_size)]['num_moves'].append(num_moves)
                    
                    if algorithm in target_algorithms:
                        heuristic_time_data[(algorithm, heuristic)].append(time)
                        print(f"Added: Algorithm: {algorithm}, Heuristic: {heuristic}, Time: {time}")
                else:
                    # No heuristic, just process for regular plots
                    num_moves = 0 if parts[4] == "No solution" else len(parts[4].split("; "))
                    data[(algorithm, board_size)]['times'].append(time)
                    data[(algorithm, board_size)]['memory_usage'].append(memory)
                    data[(algorithm, board_size)]['num_moves'].append(num_moves)
                    
            except (ValueError, IndexError) as e:
                print(f"Skipping invalid line: {line}, error: {e}")
    
    averages = compute_averages(data)
    
    heuristic_averages = {}
    for (algo, heur), times in heuristic_time_data.items():
        if times:  # Ensure we have data
            heuristic_averages[(algo, heur)] = sum(times) / len(times)
    
    print(f"Total heuristic data points: {len(heuristic_averages)}")
    
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
    
    # Create the new plot (Heuristic vs Time by Algorithm)
    heuristic_names = {1: "Misplaced", 2: "Advanced", 3: "Combined"}
    
    fig4, ax4 = plt.subplots(figsize=(WIDTH / 100, HEIGHT / 100))
    
    if heuristic_averages:
        unique_heuristic_algorithms = set(algo for (algo, _) in heuristic_averages.keys())
        
        algo_to_color_idx = {algo: i for i, algo in enumerate(unique_algorithms)}
    
        for algo in target_algorithms:
            if algo in unique_heuristic_algorithms:
                algo_data = [(h, avg_time) for (alg, h), avg_time in heuristic_averages.items() if alg == algo]
                
                if algo_data:
                    x, y = zip(*sorted(algo_data))  # Sort by heuristic number
                    color_idx = algo_to_color_idx.get(algo, 0)
                    ax4.scatter(x, y, label=algo, color=colors(color_idx % len(unique_algorithms)))

        
        ax4.set_xlabel("Heuristic Type")
        ax4.set_ylabel("Average Time (seconds)")
        ax4.set_title("Algorithm Performance by Heuristic Type (Time)")
        ax4.set_xticks(range(1, 4))
        ax4.set_xticklabels([heuristic_names.get(i, str(i)) for i in range(1, 4)])
        ax4.legend()
    else:
        plt.text(0.5, 0.5, "No heuristic data available", 
                horizontalization='center', verticalalignment='center')
    
    def plot_to_surface(fig):
        canvas = FigureCanvas(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_argb()
        size = canvas.get_width_height()
        surface = pygame.image.fromstring(raw_data, size, "ARGB")
        return pygame.transform.scale(surface, (WIDTH, HEIGHT))
    
    surf1, surf2, surf3, surf4 = plot_to_surface(fig1), plot_to_surface(fig2), plot_to_surface(fig3), plot_to_surface(fig4)
    
    for surf in [surf1, surf2, surf3, surf4]:
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
    plt.close(fig4)