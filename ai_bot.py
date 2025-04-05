import time
import ai_logic
import csv
import tracemalloc

def playBot(board, moves, bot_algorithm, bot_heuristic):
    print("BOT IS PLAYING")

    board_size = len(board)
    algorithm_name = ["DFS", "BFS", "IDDFS", "Uniform Cost", "Greedy", "A*", "Weighted A*"]

    if not moves:
        tracemalloc.start()
        start_time = time.time()

        try:
            match bot_algorithm:
                case 1:
                    print("\n SOLVING USING DFS \n")
                    moves = ai_logic.solve_dfs(board)
                case 2:
                    print("\n SOLVING USING BFS \n")
                    moves = ai_logic.solve_bfs(board)
                case 3:
                    print("\n SOLVING USING ITERATIVE DEEPENING DFS \n")
                    moves = ai_logic.solve_iddfs(board)
                case 4:
                    print("\n SOLVING USING UNIFORM COST \n")
                    moves = ai_logic.solve_uniform_cost(board)
                case 5:
                    print("\n SOLVING USING GREEDY \n")
                    moves = ai_logic.solve_greedy(board, choice=bot_heuristic)
                case 6:
                    print("\n SOLVING USING A* \n")
                    moves = ai_logic.solve_Astar(board, choice=bot_heuristic)
                case 7:
                    w = 1.2
                    print("\n SOLVING USING WEIGHTED A*, with w = ", w, "\n")
                    moves = ai_logic.solve_Astar(board, w, choice=bot_heuristic)
                case _:
                    print("Invalid algorithm option \n")
                    moves = []

        except RuntimeError as e:
            print(f"Search failed: {e}")
            return None, []

        end_time = time.time()
        bot_think_time = end_time - start_time
        current_mem, peak_mem = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        peak_mem_mb = peak_mem / (1024 * 1024)
        print(f"Bot took {bot_think_time:.4f} seconds to compute the solution.")
        print(f"Peak memory usage: {peak_mem_mb:.2f} MB")

        # Extract the move sequence
        moves_str = "; ".join(ai_logic.extract_moves(moves)) if moves else "No solution"

        # Writing performance to file
        with open("bot_performance.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            row = [board_size, algorithm_name[bot_algorithm - 1], bot_think_time, peak_mem_mb, moves_str]
            if bot_algorithm in [5, 6, 7]:
                row.append(f"{bot_heuristic}")
            writer.writerow(row)

        if not moves:
            print("No solution found by bot.")
            return None, []

    if moves:
        new_move = moves.pop(0)
        board = new_move
        time.sleep(0.5)
    else:
        print("No more moves to play.")
        return None, []

    return board, moves


# da-te uma hint based na euristica de defenida na miss_placed_birds
def get_hint(branch_birds):
    next_board = ai_logic.best_local_move(branch_birds, [])  

    if not next_board:
        return None 

    move = ai_logic.extract_moves([branch_birds, next_board])  

    if move:
        source, destination = map(int, move[0].split(" -> "))  
        return (source, destination)  

    return None

