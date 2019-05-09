class Settings():
    """储存《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 600
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5  # 飞船速度

        # 子弹的设置
        self.bullet_speed_factor = 1  # 子弹速度
        self.bullet_width = 3  # 子弹宽度
        self.bullet_height = 15  # 子弹高度
        self.bullet_color = 60, 60, 60  # 子弹颜色
        self.bullets_allowed = 30  # 屏幕中的子弹数量限制
