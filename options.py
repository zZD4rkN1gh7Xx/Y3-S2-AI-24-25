import pygame
import sys
from buttons import Button
from game import play;
def options(BG):
   
    WIDTH = 800
    HEIGHT = 550
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    
    pygame.display.set_caption('Bird Sort PyGame')
    font = pygame.font.Font('utilities/Sigmar-Regular.ttf', 24)
    pygame.display.set_caption("OPTIONS")

    
    def get_font(size):  
        return pygame.font.Font('utilities/Sigmar-Regular.ttf', size)

    while True:
        screen.blit(BG, (0, 0))

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        OPTIONS_TEXT = pygame.font.Font('utilities/Sigmar-Regular.ttf', 50).render("OPTIONS", True, "#b68f40")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 75))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        button_image = pygame.image.load("utilities/menu-buttom.png")
            
        button_small = pygame.transform.scale(button_image, (250, 100))  
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



        for button in [BUTTON1,BUTTON2,BUTTON3,BUTTON4,BUTTON5,BUTTON6,BUTTON7, BACK_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    return  # Exit the options menu and return to the main menu
                if BUTTON1.checkForInput(OPTIONS_MOUSE_POS):
                    play("BOT",1)
                if BUTTON2.checkForInput(OPTIONS_MOUSE_POS):
                    play("BOT",2)  
                if BUTTON3.checkForInput(OPTIONS_MOUSE_POS):
                    play("BOT",3)  
                if BUTTON4.checkForInput(OPTIONS_MOUSE_POS):
                    play("BOT",4)  
                if BUTTON5.checkForInput(OPTIONS_MOUSE_POS):
                    play("BOT",5)
                if BUTTON6.checkForInput(OPTIONS_MOUSE_POS):
                    play("BOT",6)  
                if BUTTON7.checkForInput(OPTIONS_MOUSE_POS):
                    play("BOT",7)     
          

        pygame.display.update()


