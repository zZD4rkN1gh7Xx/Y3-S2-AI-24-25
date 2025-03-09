import time
import ai_logic

def playBot(board,moves):
    print("BOT IS PLAYING")
    
    if(moves == []): #get moves during the first time
        moves = ai_logic.solve_bfs(board)
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

