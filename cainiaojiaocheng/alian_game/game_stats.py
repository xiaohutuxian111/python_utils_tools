"""
@FileName：game_stats.py
@Author：stone
@Time：2023/4/19 13:27
@Description:游戏统计信息
"""


class GameStats(object):
    """跟踪游戏过程中的统计信息"""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """初始化游戏运行过程中可能变化的信息"""
        self.ship_limit = self.ai_settings.ship_limit
