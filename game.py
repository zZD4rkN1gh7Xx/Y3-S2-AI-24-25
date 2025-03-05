import copy
import random
import pygame


pygame.init()

#------- variables ------------
WIDTH = 800
HEIGHT = 550

screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font('freesansbold.ttf', 24)
fps = 60
timer = pygame.time.Clock()
color_choices = ['red', 'orange', 'BLACK', 'dark blue', 'dark green', 'pink', 'purple', 'dark gray',
                'violet', 'light green', 'yellow', 'white']
bird_colors = []
initial_colors = []

branches = 8 
new_game = True
selected = False
selected_branches = []
select_branch = 100
win = False

#---------- start ------------
def generate_start():
    branch_number = random.randint(6,12)
    branch_birds = []
    available_birds =[]

    for i in range(branch_number):
        branch_birds.append([])
        if i < branch_number - 2:
            for j in range(4):
                available_birds.append(i)
    for i in range(branch_number - 2):
        for j in range(4):
            color = random.choice(available_birds)
            branch_birds[i].append(color)
            available_birds.remove(color)
    print(branch_birds)
    print(branch_number)

    return branch_number, branch_birds

#--------- draw --------------
# determine the rightmost bird of the selected branch and destination branch,
def draw(branch_num, branch_birds):
    selected_branches = []
    half_screen = WIDTH / 2
    square_size = 40
    square_padding = 5
    branch_width = 200
    branch_thickness = 5
    spacing_between_branches = 20
    branches_per_column = (branch_num + 1) // 2
    top_padding = 180

    left_x = 150
    right_x = half_screen + 50

    row_spacing = square_size + spacing_between_branches

    for i in range(branch_num):
        column = 0 if i % 2 == 0 else 1
        row = i // 2

        x_pos = left_x if column == 0 else right_x
        y_pos = top_padding + row * row_spacing

        total_width = len(branch_birds[i]) * (square_size + square_padding) - square_padding
        start_x = x_pos + (branch_width - total_width) / 2

        # Reverse bird order for second column
        birds_to_draw = branch_birds[i] if column == 0 else list(reversed(branch_birds[i]))

        for j in range(len(birds_to_draw)):
            pygame.draw.rect(screen, color_choices[birds_to_draw[j]], 
                            [start_x + j * (square_size + square_padding), y_pos - square_size, 
                            square_size, square_size], 0, 3)

        branch_color = 'green' if select_branch == i else 'brown'
        pygame.draw.line(screen, branch_color, (x_pos, y_pos), (x_pos + branch_width, y_pos), branch_thickness)

        branch_rect = pygame.Rect(x_pos, y_pos - square_size, branch_width, square_size)
        selected_branches.append(branch_rect)


    return selected_branches


#--------- calculate move-------------
def calc_move(colors, selected_branch, destination):
    chain = True
    color_on_top = 100
    length = 1
    color_to_move = 100
    if len(colors[selected_branch]) > 0:
        color_to_move = colors[selected_branch][-1]
        for i in range(1, len(colors[selected_branch])):
            if chain:
                if colors[selected_branch][-1 - i] == color_to_move:
                    length += 1
                else:
                    chain = False
    if 4 > len(colors[destination]):
        if len(colors[destination]) == 0:
            color_on_top = color_to_move
        else:
            color_on_top = colors[destination][-1]
    if color_on_top == color_to_move:
        for i in range(length):
            if len(colors[destination]) < 4:
                if len(colors[selected_branch]) > 0:
                    colors[destination].append(color_on_top)
                    colors[selected_branch].pop(-1)
    print(colors, length)
    return colors

def check_victory(colors):
    won = True
    for i in range(len(colors)):
        if len(colors[i]) > 0:
            if len(colors[i]) != 4:
                won = False
            else:
                main_color = colors[i][-1]
                for j in range(len(colors[i])):
                    if colors[i][j] != main_color:
                        won = False
    return won

#--------- game_loop ---------- 

def play():
    global branches, bird_colors, initial_colors, new_game, selected, select_branch, win 
    run = True
    while run:
        screen.fill('light blue')
        timer.tick(fps)

        #game states
        if new_game:
            branches, bird_colors = generate_start()
            initial_colors = copy.deepcopy(bird_colors)
            new_game = False
        else:
            selected_branches = draw(branches, bird_colors)
            win = check_victory(bird_colors)

        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    bird_colors = copy.deepcopy(initial_colors)
                elif event.key == pygame.K_RETURN:
                    new_game = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not selected:
                    for item in range(len(selected_branches)):
                        if selected_branches[item].collidepoint(event.pos):
                            selected = True
                            select_branch = item
                else:
                    for item in range(len(selected_branches)):
                        if selected_branches[item].collidepoint(event.pos):
                            dest_branch = item
                            bird_colors = calc_move(bird_colors, select_branch, dest_branch)
                            selected = False
                            select_branch = 100
        # draw 'victory' text when winning in middle, always show restart and new board text at top
        if win:
            victory_text = font.render('You Won! Press Enter for a new board!', True, 'white')
            screen.blit(victory_text, (300, 475))
        restart_text = font.render('Stuck? Space-Restart, Enter-New Board!', True, 'white')
        screen.blit(restart_text, (10, 10))

        pygame.display.flip()


play()
pygame.quit()
