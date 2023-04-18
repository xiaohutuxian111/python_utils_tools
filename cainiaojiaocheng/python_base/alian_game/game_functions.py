"""
@FileName：game_functions.py
@Author：stone
@Time：2023/4/18 17:55
@Description:事件检查
"""
import sys

import pygame
from setting import Settings
from ship import Ship

def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings,screen,ship):
    # 设置背景色
    bg_color = ai_settings.bg_color
    screen.fill(bg_color)
    # 绘制飞船
    ship.blitme()
    #  让最近绘制的屏幕可见
    pygame.display.flip()
