"""
@FileName：alien_invasion.py
@Author：stone
@Time：2023/4/18 14:55
@Description:主窗口的创建
"""

import pygame
from pygame.sprite import Group
from setting import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import  Scoreboard
import game_functions as gf


def run_game():
    """初始化一个屏幕对象"""
    # 设置类初始化
    pygame.display.set_caption("Alien  Invation")
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    # 创建一个用于子弹的编组
    bullets = Group()
    # 创建外星人人人群
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    stats = GameStats(ai_settings)
    # 创建记分牌
    sb= Scoreboard(ai_settings, screen,stats)
    play_button = Button(ai_settings, screen, "play")
    # 开始游戏的主循环
    while True:
        # 实时监控鼠标键盘事件
        gf. check_events(ai_settings, screen, ship, aliens, bullets, play_button, stats,sb)
        ship.update()
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_bullets(ai_settings, screen, ship, bullets, aliens,stats,sb)
        gf.update_screen(ai_settings, screen, stats, ship, bullets, aliens, play_button,sb)


run_game()
