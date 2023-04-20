"""
@FileName：scoreboard.py
@Author：stone
@Time：2023/4/19 15:28
@Description:记分牌
"""
import pygame.font
from pygame.sprite import Group

from cainiaojiaocheng.alian_game.ship import Ship


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

        #  准备包含最高分的图像

        self.prep_high_score()
        # 等级
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """将得分选人成一副图像"""
        round_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分显示到屏幕上面来
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.score_high_image, self.score_high_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """将最高得分转化为图像"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.score_high_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        # 将得分显示到屏幕上面来
        self.score_high_rect = self.score_high_image.get_rect()
        self.score_high_rect.centerx = self.screen_rect.centerx
        self.score_high_rect.top = self.screen_rect.top

    def prep_level(self):
        """将等级化为渲染的图像"""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color,
                                            self.ai_settings.bg_color)
        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """将等级化为渲染的图像"""
        self.ships = Group()
        for ship_number in range(self.stats.ship_limit):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
