"""
@FileName：alien_invasion.py
@Author：stone
@Time：2023/4/18 14:55
@Description:主窗口的创建
"""

import pygame
from setting import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """初始化一个屏幕对象"""
    # 设置类初始化
    ai_settings = Settings()

    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_height, ai_settings.screen_width))

    ship = Ship(screen)
    pygame.display.set_caption("Alien  Invation")

    # 开始游戏的主循环
    while True:
        # 实时监控鼠标键盘事件
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)


run_game()
