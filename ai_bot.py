import time
import ai_logic

def playBot(board,moves):
    print("BOT IS PLAYING")
    
    if(moves == []): #get moves during the first time
        moves = ai_logic.solve_Astar(board,1.5)
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

