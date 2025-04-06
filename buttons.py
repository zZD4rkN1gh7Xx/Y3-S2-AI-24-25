import pygame
class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos, self.y_pos = pos
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color

        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))  
        self.mask = pygame.mask.from_surface(self.image)  

        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos - 8))

    def update(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if self.is_hovered(position): 
            print("Button pressed!")
            return True 
        return False

    def changeColor(self, position):
        if self.is_hovered(position):  
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    def is_hovered(self, position):
        x, y = position
        if self.rect.collidepoint(position):  
            rel_x, rel_y = x - self.rect.left, y - self.rect.top  
            return self.mask.get_at((rel_x, rel_y)) 
        return False  
