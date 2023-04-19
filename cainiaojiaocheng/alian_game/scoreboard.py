"""
@FileName：scoreboard.py
@Author：stone
@Time：2023/4/19 15:28
@Description:记分牌
"""
import pygame.font


class Scoreboard():
    """显示的非信息类"""

    def __init__(self, ai_settings, screen, stats):
        """显示得分信息的类"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息使用字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #  准备初始化得分
        self.prep_score()

    def prep_score(self):
        """将得分选人成一副图像"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分显示到屏幕上面来
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
