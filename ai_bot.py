import time
import ai_logic

def playBot(board,moves,bot_algorithm):
    print("BOT IS PLAYING")
    
    if(moves == []): #get moves during the first time
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
                moves = ai_logic.solve_greedy(board)
            case 6:
                print("\n SOLVING USING A* \n")
                moves = ai_logic.solve_Astar(board)
            case 7:
                w = 3.5
                print("\n SOLVING USING WEIGHTED A*, with w = ", w, "\n"), 
                moves = ai_logic.solve_Astar(board, w)
            case _:
                print("Invalid algorithm option \n")
                

    else:    #run 1 move at a time
        new_move = moves[0]
        moves.pop(0)
        print(new_move)
        board = new_move
        time.sleep(0.5)

    print(board)
    print(moves)

    return board,moves

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

