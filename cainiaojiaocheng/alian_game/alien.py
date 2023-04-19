"""
@FileName：alien.py
@Author：stone
@Time：2023/4/19 9:27
@Description:外星人
"""
import pygame.image
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        """初始化外星人并初始化位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像,并设置rect属性
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # 每个外星人都初始化在屏幕左上方附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)
        self.y =  float(self.rect.y)

    def blitme(self):
        """在指定的位置绘制外星人"""
        self.screen.blit(self.image, self.rect)
