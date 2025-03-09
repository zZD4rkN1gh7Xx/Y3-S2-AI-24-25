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
        board = getNewBoard(board,new_move)
        time.sleep(0.5)

    print(board)
    print(moves)

    return board,moves,


import copy

def getNewBoard(branch_birds, new_move):
    source, destination = new_move

    new_board = copy.deepcopy(branch_birds) 

    if len(new_board[source]) == 0 or len(new_board[destination]) >= 4:
        return new_board

    color_birds_to_move = new_board[source][-1]  

    birds_to_move = []
    for i in range(len(new_board[source]) - 1, -1, -1):
        if new_board[source][i] == color_birds_to_move:
            birds_to_move.append(new_board[source][i])
        else:
            break  

    
    if len(new_board[destination]) == 0 or new_board[destination][-1] == color_birds_to_move:
        while birds_to_move and len(new_board[destination]) < 4:
            new_board[destination].append(birds_to_move.pop())

        new_board[source] = new_board[source][:len(new_board[source]) - len(birds_to_move) - 1]

    return new_board

