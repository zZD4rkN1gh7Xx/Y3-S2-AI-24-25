import copy
import random
import pygame
import time
from ai_bot import playBot
from ai_bot import get_hint
from buttons import Button

def get_font(size):  
    return pygame.font.Font('utilities/Sigmar-Regular.ttf', size)

# Define the play function here without immediately running it

def play(playerType,bot_algorithm=0):
    pygame.init()  # Initialize pygame only when starting the game loop
    
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)  # Reduce buffer size to lower latency
    pygame.mixer.music.load("utilities/why-did-the-chicken-cross-the-road-official-instrumental.mp3")  
    pygame.mixer.music.set_volume(0.5)  
    pygame.mixer.music.play(-1)

    winning_sound = pygame.mixer.Sound("utilities/angry-birds-victory-sound.mp3")
    winning_sound.set_volume(0.5) 
    
    win_channel = pygame.mixer.Channel(1)
    
    #------- variables ------------
    WIDTH = 800
    HEIGHT = 550
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    font = pygame.font.Font('utilities/Sigmar-Regular.ttf', 24)
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
    botMoves = []

    hint_move = None


    tree_image = pygame.image.load("utilities/arvore-removebg-preview.png")  
    tree_width = 500  
    tree_height = 700
    tree_image = pygame.transform.scale(tree_image, (tree_width, tree_height))  

    cloud_image = pygame.image.load("utilities/cartoon-cloud-png.png") 
    cloud_width = 1000
    cloud_height = 300
    cloud_image = pygame.transform.scale(cloud_image, (cloud_width, cloud_height))

    button_image = pygame.image.load("utilities/menu-buttom.png")
    button_image = pygame.transform.scale(button_image,(125, 90))
    BACK_BUTTON = Button(image=button_image, pos=(50,510),
                         text_input="<-", font=get_font(20),
                         base_color="#d7fcd4", hovering_color="orange")

    HINT_BUTTON = Button(image=button_image, pos=(180, 510),  
                     text_input="Hint", font=get_font(20),  
                     base_color="#d7fcd4", hovering_color="orange")
  

    #---------- start ------------
    def generate_start():
        branch_number = random.randint(6,8)
        branch_birds = []
        available_birds = []

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

        # **Cloud Positioning**
        cloud_x = -50  # Move the cloud towards the left
        cloud_y = top_padding - 200  # Adjust height to appear behind the tree
        screen.blit(cloud_image, (cloud_x, cloud_y))  # **Draw the cloud FIRST**

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


        tree_left_x = -105  # Position for the left tree
        tree_right_x = WIDTH - 350  # Position for the right tree
        tree_y = top_padding - 180  # Adjust the vertical position of trees

        screen.blit(tree_image, (tree_left_x, tree_y))  # Draw the left tree
        screen.blit(tree_image, (tree_right_x, tree_y))  # Draw the right tree






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
    
    def play_winning_sound():
        if not win_channel.get_busy():  # Prevents overlapping
            win_channel.play(winning_sound)
            

    #--------- game_loop ---------- 





    run = True
    while run:
        screen.fill('light blue')
        timer.tick(fps)

        MOUSE_POS = pygame.mouse.get_pos()

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
                if BACK_BUTTON.checkForInput(MOUSE_POS):
                    return 
                if HINT_BUTTON.checkForInput(MOUSE_POS) and playerType == "PLAYER":
                    hint_move = get_hint(bird_colors)

            if(playerType == "PLAYER"):
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
                                hint_move = None
           
        if playerType == "BOT" and not win:
            bird_colors, botMoves = playBot(bird_colors, botMoves, bot_algorithm)

        BACK_BUTTON.changeColor(MOUSE_POS)
        BACK_BUTTON.update(screen)
        
        if playerType == "PLAYER":
            HINT_BUTTON.changeColor(MOUSE_POS)
            HINT_BUTTON.update(screen)


        if hint_move and playerType == "PLAYER":
            hint_text = font.render(f"Hint: Move {hint_move[0]} -> {hint_move[1]}", True, "yellow")
            screen.blit(hint_text, (300, 520))

        if hint_move and playerType == "PLAYER":
            hint_source, hint_dest = hint_move
            pygame.draw.line(screen, "red", (selected_branches[hint_source].x, selected_branches[hint_source].y),
                            (selected_branches[hint_source].x + 200, selected_branches[hint_source].y), 8)
            pygame.draw.line(screen, "red", (selected_branches[hint_dest].x, selected_branches[hint_dest].y),
                            (selected_branches[hint_dest].x + 200, selected_branches[hint_dest].y), 8)


        if win:
            victory_text = font.render('You Won! Press Enter for a new board!', True, 'white')
            screen.blit(victory_text, (300, 475))
            play_winning_sound()

        restart_text = font.render('Stuck? Space-Restart, Enter-New Board!', True, 'orange')
        screen.blit(restart_text, (10, 10))

        pygame.display.flip()

    pygame.quit()

