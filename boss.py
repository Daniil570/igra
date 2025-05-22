import pygame
from alien import Alien

class Boss(Alien):
    def __init__(self, ai_settings, screen):
        super().__init__(ai_settings, screen)
        self.image = pygame.image.load('boss.png')
        self.rect = self.image.get_rect()
        self.health = 50  # Теперь нужно 20 попаданий для победы
        self.max_health = 50
        self.hit_count = 0  # Счётчик попаданий
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        # Отрисовка индикатора здоровья
        health_bar_width = 100
        health_bar_height = 10
        current_health_width = (self.hit_count / self.max_health) * health_bar_width
        
        pygame.draw.rect(self.screen, (255, 0, 0), 
                        (self.rect.x, self.rect.y - 15, 
                         health_bar_width, health_bar_height))
        pygame.draw.rect(self.screen, (0, 255, 0), 
                        (self.rect.x, self.rect.y - 15, 
                         current_health_width, health_bar_height))
        
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * 1.5 * self.ai_settings.fleet_direction)
        self.rect.x = self.x
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
            
    def hit(self):
        self.hit_count += 1
        return self.hit_count >= self.max_health