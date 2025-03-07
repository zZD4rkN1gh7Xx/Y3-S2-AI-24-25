import copy

class BoardState:
    def __init__(self, board):
        self.board = tuple(tuple(row) for row in board)  

    def __hash__(self):
        return hash(self.board)

    def __eq__(self, other):
        return isinstance(other, BoardState) and self.board == other.board

    def to_list(self):
        """Convert back to a list (for processing)"""
        return [list(row) for row in self.board]


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


def get_new_boards(branch_birds, new_moves):
    new_boards = []

    for move in new_moves:
        source, destination = move

        new_board = copy.deepcopy(branch_birds)

        # If the branch is empty
        if len(new_board[source]) == 0:
            continue
        
        # If the new branch is full
        if len(new_board[destination]) >= 4:
            continue

        color_birds_to_move = new_board[source][-1]

        birds_to_move = []
        for i in range(len(new_board[source]) - 1, -1, -1):
            if new_board[source][i] == color_birds_to_move:
                birds_to_move.append(new_board[source][i])
            else:
                break 

        num_birds_moving = len(birds_to_move)

        if len(new_board[destination]) == 0 or new_board[destination][-1] == color_birds_to_move:
            while birds_to_move and len(new_board[destination]) < 4:
                new_board[destination].append(birds_to_move.pop())

            new_board[source] = new_board[source][:len(new_board[source]) - num_birds_moving]

            new_boards.append(BoardState(new_board))  # Convert to BoardState

    return new_boards


def check_victory(branch_birds):
    for i in range(len(branch_birds)):
        if len(branch_birds[i]) > 0:
            if len(branch_birds[i]) != 4:
                return False
            else:
                main_color = branch_birds[i][-1]
                if any(bird != main_color for bird in branch_birds[i]):
                    return False
    return True


def reconstruct_path(start_branch, current_branch, parent_map):
    path = []

    while current_branch in parent_map:
        path.append(current_branch.to_list())  # Convert BoardState to list
        current_branch = parent_map[current_branch]

    path.append(start_branch.to_list())
    return list(reversed(path))


def solve_bfs(initial_board):
    start_state = BoardState(initial_board)
    
    visited = set()
    parent_map = {}

    queue = [start_state]

    while queue:
        current_state = queue.pop(0)

        if check_victory(current_state.to_list()):
            return reconstruct_path(start_state, current_state, parent_map)

        if current_state in visited:
            continue 

        visited.add(current_state)
        possible_moves = get_possible_moves(current_state.to_list())

        for board in get_new_boards(current_state.to_list(), possible_moves):
            if board not in visited:
                parent_map[board] = current_state
                queue.append(board)

    return None

def extract_moves(solution_path):
    moves = []
    
    for i in range(len(solution_path) - 1):
        prev_state = solution_path[i]
        next_state = solution_path[i + 1]
        
        source, destination = None, None
        
        for j in range(len(prev_state)):
            if len(prev_state[j]) > len(next_state[j]):
                source = j
            elif len(prev_state[j]) < len(next_state[j]):
                destination = j
        
        if source is not None and destination is not None:
            moves.append(f"{source} -> {destination}")
    
    return moves


board = [[2, 0, 1, 2], [3, 1, 3, 1], [0, 2, 2, 1], [3, 0, 3, 0], [], []]
print(extract_moves(solve_bfs(board)))
