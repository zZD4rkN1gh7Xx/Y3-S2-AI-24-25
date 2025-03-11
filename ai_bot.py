import time
import ai_logic

def playBot(board,moves,bot_algorithm):
    print("BOT IS PLAYING")
    
    if(moves == []): #get moves during the first time
        match bot_algorithm:
            case 1:
                moves = ai_logic.solve_dfs(board)
            case 2:
                moves = ai_logic.solve_bfs(board)
            case 6:
                moves = ai_logic.solve_Astar(board)
            case 7:
                w = input("please state the weight for weighted A*")
                moves = ai_logic.solve_Astar(board, w)
            case _:
                print("Invalid algorithm option")
                

    else:    #run 1 move at a time
        new_move = moves[0]
        moves.pop(0)
        print(new_move)
        board = new_move
        time.sleep(0.5)

    print(board)
    print(moves)

    return board,moves


import copy

