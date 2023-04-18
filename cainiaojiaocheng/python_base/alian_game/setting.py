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
        self.screen_width = 800
        self.screen_height = 1200
        self.bg_color = (233, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height =15
        self.bullet_color = 60,60,60


