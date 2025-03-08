import pygame
import pygame.locals
import sys  
from buttons import Button
from game import play

pygame.init()

WIDTH = 800
HEIGHT = 550
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Bird Sort PyGame')
font = pygame.font.Font('utilities/Sigmar-Regular.ttf', 24)

BG = pygame.image.load("utilities/sky-BG.jpg")
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT)) 

pygame.mixer.init()
pygame.mixer.music.load("utilities/why-did-the-chicken-cross-the-road-official-instrumental.mp3")  
pygame.mixer.music.set_volume(0.5)  
pygame.mixer.music.play(-1)




def get_font(size):  
    return pygame.font.Font('utilities/Sigmar-Regular.ttf', size)


def main_menu():
    pygame.display.set_caption("MAIN MENU BRID SROT")

    while True:
        screen.blit(BG, (0, 0))  

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("BRID SROT", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH // 2, 110))
        screen.blit(MENU_TEXT, MENU_RECT)

        button_image = pygame.image.load("utilities/menu-buttom.png")
        button_image = pygame.transform.scale(button_image, (400, 200))

        button_image2 = pygame.transform.scale(button_image, (300, 150))

        PLAY_BUTTON = Button(image=button_image, pos=(WIDTH // 2, 310), 
                             text_input="PLAY!", font=get_font(50), 
                             base_color="#d7fcd4", hovering_color="orange")
        
        OPTIONS_BUTTON = Button(image=button_image2, pos=(WIDTH // 2, 410), 
                             text_input="OPTIONS", font=get_font(30), 
                             base_color="#d7fcd4", hovering_color="orange")

        for button in [PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for button in [OPTIONS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play("PLAYER")
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play("BOT")

        pygame.display.update()


main_menu()

