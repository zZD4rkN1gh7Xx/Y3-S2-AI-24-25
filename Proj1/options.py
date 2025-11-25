import pygame
import sys
from buttons import Button
from game import play


def options(BG):
   
    WIDTH = 800
    HEIGHT = 550
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    
    pygame.display.set_caption('Bird Sort PyGame')
    font = pygame.font.Font('utilities/Sigmar-Regular.ttf', 24)
    pygame.display.set_caption("OPTIONS")

    
    def get_font(size):  
        return pygame.font.Font('utilities/Sigmar-Regular.ttf', size)

    selected_algorithm = None 

    while True:
        screen.blit(BG, (0, 0))

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        OPTIONS_TEXT = pygame.font.Font('utilities/Sigmar-Regular.ttf', 50).render("CHOOSE AN ALGORITHM", True, "#b68f40")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 65))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        button_image = pygame.image.load("utilities/menu-buttom.png")
            
        button_small = pygame.transform.scale(button_image,(125, 90))
        button_large = pygame.transform.scale(button_image, (400, 150))  

        BUTTON1 = Button(image=button_large, pos=(150, 150),  
                        text_input="DFS", font=get_font(30),
                        base_color="#d7fcd4", hovering_color="orange")

        BUTTON2 = Button(image=button_large, pos=(400, 150), 
                        text_input="BFS", font=get_font(30),
                        base_color="#d7fcd4", hovering_color="orange")

        BUTTON3 = Button(image=button_large, pos=(650, 150),  
                        text_input="ITERATIVE DEEPENING", font=get_font(15),
                        base_color="#d7fcd4", hovering_color="orange")
        
        BUTTON4 = Button(image=button_large, pos=(150, 300),  
                        text_input="UNIFORM COST", font=get_font(20),
                        base_color="#d7fcd4", hovering_color="orange")

        BUTTON5 = Button(image=button_large, pos=(400, 300),  
                        text_input="GREEDY SEARCH", font=get_font(20),
                        base_color="#d7fcd4", hovering_color="orange")

        BUTTON6 = Button(image=button_large, pos=(650, 300),  
                        text_input="A*", font=get_font(30),
                        base_color="#d7fcd4", hovering_color="orange")

        BUTTON7 = Button(image=button_large, pos=(400, 450),  
                        text_input="WEIGHTED A*", font=get_font(20),
                        base_color="#d7fcd4", hovering_color="orange")


        BACK_BUTTON = Button(image=button_small, pos=(50,510),
                            text_input="<-", font=get_font(20),
                            base_color="#d7fcd4", hovering_color="orange") 

        if selected_algorithm in [5, 6, 7]:  # Show heuristic options only for greddy, A* and Weighted A*
            HEURISTIC_TEXT = get_font(40).render("CHOOSE HEURISTIC", True, "orange")
            HEURISTIC_RECT = HEURISTIC_TEXT.get_rect(center=(400, 200))
            screen.blit(HEURISTIC_TEXT, HEURISTIC_RECT)


            scaled_button = pygame.transform.scale(button_image, (button_large.get_width() + 100, button_large.get_height()))

            HEURISTIC_BUTTON1 = Button(image=scaled_button, pos=(250, 350),  
                                    text_input="MISPLACED BIRDS", font=get_font(25),
                                    base_color="#d7fcd4", hovering_color="orange")

            HEURISTIC_BUTTON2 = Button(image=scaled_button, pos=(550, 350),  
                                    text_input="ADVANCED", font=get_font(25),
                                    base_color="#d7fcd4", hovering_color="orange")


            HEURISTIC_BUTTON3 = Button(image=scaled_button, pos=(400, 450),  
                                    text_input="COMBINED HEURISTIC", font=get_font(25),
                                    base_color="#d7fcd4", hovering_color="orange")

            for button in [HEURISTIC_BUTTON1, HEURISTIC_BUTTON2, HEURISTIC_BUTTON3]:
                button.changeColor(OPTIONS_MOUSE_POS)
                button.update(screen)
        else:
            for button in [BUTTON1, BUTTON2, BUTTON3, BUTTON4, BUTTON5, BUTTON6, BUTTON7]:
                button.changeColor(OPTIONS_MOUSE_POS)
                button.update(screen)

        BACK_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        BACK_BUTTON.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    return  

                if selected_algorithm in [5,6, 7]:  # Only Greedy, A* and Weighted A* require heuristic
                    if HEURISTIC_BUTTON1.checkForInput(OPTIONS_MOUSE_POS):
                        play("BOT", selected_algorithm, 1)  # Misplaced Birds heuristic
                    if HEURISTIC_BUTTON2.checkForInput(OPTIONS_MOUSE_POS):
                        play("BOT", selected_algorithm, 2)  # Advanced heuristic
                    if HEURISTIC_BUTTON3.checkForInput(OPTIONS_MOUSE_POS):
                        play("BOT", selected_algorithm, 3) #combined heuristic
                else:  
                    for i, button in enumerate([BUTTON1, BUTTON2, BUTTON3, BUTTON4, BUTTON5, BUTTON6, BUTTON7], start=1):
                        if button.checkForInput(OPTIONS_MOUSE_POS):
                            if i in [5, 6, 7]:  
                                selected_algorithm = i 
                            else:
                                play("BOT", i)  

        pygame.display.update()
