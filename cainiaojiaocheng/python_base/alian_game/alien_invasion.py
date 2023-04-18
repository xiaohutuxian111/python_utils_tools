"""
@FileName：alien_invasion.py
@Author：stone
@Time：2023/4/18 14:55
@Description:主窗口的创建
"""
import sys

import pygame


def run_game():
    """初始化一个屏幕对象"""
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien  Invation")


    # 设置背景色
    bg_color =  (230,230,230)

    # 开始游戏的主循环
    while True:
        # 实时监控鼠标键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #  每次循环重新绘制屏幕
        screen.fill(bg_color)
        #  让最近绘制的屏幕可见
        pygame.display.flip()



run_game()