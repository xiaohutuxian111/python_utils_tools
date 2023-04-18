"""
@FileName：bullet.py
@Author：stone
@Time：2023/4/18 21:32
@Description:子弹类
"""
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        """在飞船所在的位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen
        # 在（0，0）处创建一个表示子弹的矩形,在设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_with, ai_settings.bullet_height)
        self.rect = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储小数表示子弹的位置
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.spped_factor = ai_settings.bullet_speed_factor

    def draw_bullet(self):
        #  在屏幕上绘制子弹
        pygame.draw.rect(self.screen, self.colo, self.rect)
