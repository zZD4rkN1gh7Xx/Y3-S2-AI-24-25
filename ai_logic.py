import copy

def get_possible_moves(branch_birds):
    possible_moves = []
    
    for src in range(len(branch_birds)):  
        if len(branch_birds[src]) == 0:
            continue  

        top_bird = branch_birds[src][-1]  

        for dest in range(len(branch_birds)):  
            if src == dest:
                continue  
            
            if len(branch_birds[dest]) < 4:  
                if len(branch_birds[dest]) == 0 or branch_birds[dest][-1] == top_bird:
                    possible_moves.append((src, dest))  

    return possible_moves



def get_new_board(branch_birds, new_move):
    source, destination = new_move

    new_board = copy.deepcopy(branch_birds)

    #if the branch is empty
    if len(new_board[source]) == 0:
        return new_board
    
    #if the enew branch is full
    if len(new_board[destination]) >= 4:
        return new_board

    # ir buscar a cor do passaro que esta no topo para ver movido
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

        #moves os passaros de uma branch para outra
        new_board[source] = new_board[source][:len(new_board[source]) - len(birds_to_move)]

    return new_board

board = [[4, 1, 4, 2], [3, 2, 0], [2, 3], [4, 4], [3, 1, 3, 2], [0, 0, 0], [1, 1]]

move = get_possible_moves(board)[1]


print(move)
print(get_new_board(board, move))