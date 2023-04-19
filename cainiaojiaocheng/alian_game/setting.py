"""
@FileName：setting.py
@Author：stone
@Time：2023/4/18 15:03
@Description:
"""


class Settings():
    """存储配置的所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        self.screen_height = 800
        self.screen_width = 1200
        self.bg_color = (233, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1

        # 子弹设置
        self.bullet_speed_factor =  3
        self.bullet_width = 3
        self.bullet_height =15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3

        #  外星人设置
        self.alien_speed_factor = 1
        #  外星人下落速度
        self.alien_drop_speed = 5
        # 外星人移动方向  1 为向右 -1为向左
        self.alien_direction =1







