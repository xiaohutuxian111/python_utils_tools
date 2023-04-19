"""
@FileName：button.py
@Author：stone
@Time：2023/4/19 14:22
@Description:
"""
import pygame.font


class Button():
    """按钮类"""

    def __init__(self, ai_settings, screen, msg):
        """按钮初始化到屏幕"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # 设置按钮的尺寸和其他设置
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 0)
        self.font = pygame.font.SysFont(None, 48)

        # 创建按钮的rect对象，并将其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按键的标签只需创建一次
        self.grep_msg(msg)

    def grep_msg(self, msg):
        """将msg渲染成图像,并使在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制一个颜色填充的按钮，并填充文本"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
