import pygame
from buttons import Button

def get_font(size):  
    return pygame.font.Font('utilities/Sigmar-Regular.ttf', size)

def get_top_scores():
    scores = []
    try:
        with open("leaderboard.txt", "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                if len(parts) < 4:
                    continue 
                
                name = parts[0].split(": ")[1]
                moves = int(parts[1].split(": ")[1])
                time = float(parts[2].split(": ")[1][:-1]) 
                wer = float(parts[3].split(": ")[1])

                scores.append((name, moves, time, wer))

        scores.sort(key=lambda x: x[3]) 

        return reversed(scores[:5])  # Return top 5
    except FileNotFoundError:
        return []  

def draw_leaderboard(screen):
    # Load Background Assets
    cloud_image = pygame.image.load("utilities/cartoon-cloud-png.png")
    cloud_image = pygame.transform.scale(cloud_image, (900, 250))  

    tree_image = pygame.image.load("utilities/arvore-removebg-preview.png")
    tree_image = pygame.transform.scale(tree_image, (450, 600)) 

    button_image = pygame.image.load("utilities/menu-buttom.png")
    button_image = pygame.transform.scale(button_image, (125, 90))

    BACK_BUTTON = Button(image=button_image, pos=(50, 510),
                         text_input="<-", font=get_font(20),
                         base_color="#d7fcd4", hovering_color="orange")

    running = True
    while running:
        screen.fill("light blue")

        # Draw Background First
        screen.blit(cloud_image, (-50, -120)) 

        screen.blit(tree_image, (-100, screen.get_height() - 550))  
        screen.blit(tree_image, (screen.get_width() - 350, screen.get_height() - 550))  

        font = pygame.font.Font('utilities/Sigmar-Regular.ttf', 35)
        title = font.render("Top 5 Scores", True, "blue")
        screen.blit(title, (screen.get_width() // 2 - 100, 50))

        top_scores = get_top_scores()
        if not top_scores:
            no_scores_text = font.render("No scores available", True, "orange")
            screen.blit(no_scores_text, (screen.get_width() // 2 - 100, 100))
        else:
            # Table Headers
            header_font = pygame.font.Font('utilities/Sigmar-Regular.ttf', 26)
            headers = ["#", "Name", "SCORE"]
            header_x_positions = [150, 300, 500]
            
            for i, header in enumerate(headers):
                header_text = header_font.render(header, True, "orange")
                screen.blit(header_text, (header_x_positions[i], 140))

            row_font = pygame.font.Font('utilities/Sigmar-Regular.ttf', 24)
            y_offset = 180

            for i, (name, _, _, wer) in enumerate(top_scores):  
                row_values = [str(i+1), name, f"{wer:.2f}"]
                
                for j, value in enumerate(row_values):
                    row_text = row_font.render(value, True, "orange")
                    screen.blit(row_text, (header_x_positions[j], y_offset))
                
                y_offset += 40  

        BACK_BUTTON.changeColor(pygame.mouse.get_pos())
        BACK_BUTTON.update(screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
               
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(pygame.mouse.get_pos()):
                    running = False  
