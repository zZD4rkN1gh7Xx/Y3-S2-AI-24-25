import pygame
import sys
class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos, self.y_pos = pos
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color

        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))  # Rectangle hitbox
        self.mask = pygame.mask.from_surface(self.image)  # Create a mask for transparency

        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos - 8))

    def update(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if self.is_hovered(position):  # Pixel-perfect check
            return True  # Return True when the button is clicked
        return False

    def changeColor(self, position):
        if self.is_hovered(position):  # More precise hover check
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    def is_hovered(self, position):
        x, y = position
        if self.rect.collidepoint(position):  # First, check if it's in the general hitbox
            rel_x, rel_y = x - self.rect.left, y - self.rect.top  # Convert to local coordinates
            return self.mask.get_at((rel_x, rel_y))  # Check if that pixel is opaque
        return False  # Not inside the hitbox at all
