"""
@FileName：ship.py
@Author：stone
@Time：2023/4/18 15:51
@Description:飞船类
"""
import pygame.image


class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置初始位置"""
        self.screen = screen

        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新的飞船放在屏幕的中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.moving_right = False
        self.moving_left = False

        self.ai_settings = ai_settings
        # 在飞船的属性center中存储最小的数值
        self.center = float(self.rect.centerx)

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.center < self.screen_rect.right - 0.5 * self.image.get_width():
            # 更新飞船的center值，而不是rect
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.center > 0.5 * self.image.get_width():
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center 的位置更新 rect对象
        self.rect.centerx = self.center

    def center_ship(self):
        """让飞船在屏幕居中"""
        self.center = self.screen_rect.centerx

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
