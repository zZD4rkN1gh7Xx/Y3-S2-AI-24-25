import pygame
import pygame.locals
import matplotlib.pyplot as plt
import csv


WIDTH = 800
HEIGHT = 550

def show_bot_statistics():
    board_sizes = []
    algorithms = []
    times = []

    with open("bot_performance.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            try:
                board_sizes.append(int(row[0])) 
                algorithms.append(row[1])       
                times.append(float(row[2]))     
            except ValueError:
                print(f"Skipping invalid row: {row}")  


    plt.figure(figsize=(10, 5))

   
    unique_algorithms = list(set(algorithms))
    colors = plt.cm.get_cmap("tab10", len(unique_algorithms)) 

    for i, algo in enumerate(unique_algorithms):
        x = [board_sizes[j] for j in range(len(algorithms)) if algorithms[j] == algo]
        y = [times[j] for j in range(len(algorithms)) if algorithms[j] == algo]
        plt.scatter(x, y, label=algo, color=colors(i))  
    plt.xlabel("Board Size")
    plt.ylabel("Time (seconds)")
    plt.title("Algorithm Performance by Board Size")
    plt.legend()
    plt.show()

    pygame.display.set_mode([WIDTH, HEIGHT]) 
