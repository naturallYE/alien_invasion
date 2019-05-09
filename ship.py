import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中储存小数值
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        # 移动标志
        self.moving_up = False  # 上
        self.moving_down = False  # 下
        self.moving_left = False  # 左
        self.moving_right = False  # 右

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center_x值, center_y值
        # 当按下up键时(moving_up为True(moving_up = 1))和飞船方块上部坐标>屏幕顶边缘(顶边缘坐标为y=0)时,
        # 才可向上移动
        if self.moving_up and self.rect.top > 0:
            self.center_y -= self.ai_settings.ship_speed_factor
        # 当按下down键时(moving_down为True(moving_down = 1))和飞船方块下部坐标<屏幕底边缘
        # (底边缘为设置的窗口高度self.ai_settings.screen_height)时,才可向下移动
        if self.moving_down and self.rect.bottom < self.ai_settings.screen_height:
            self.center_y += self.ai_settings.ship_speed_factor
        # 当按下left键时(moving_left为True(moving_left = 1))和飞船方块左部坐标>屏幕左边缘(左边缘坐标为x=0)时,
        # 才可向左移动
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.ai_settings.ship_speed_factor
        # 当按下right键时(moving_right为True(moving_right = 1))和飞船方块右部坐标<屏幕右边缘
        # (底边缘为设置的窗口宽度self.ai_settings.screen_width)时,才可向下移动
        if self.moving_right and self.rect.right < self.ai_settings.screen_width:
            self.center_x += self.ai_settings.ship_speed_factor

        # 根据飞船的center_x值, center_y值更新rect对象
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def blitme(self):
        """在指定的位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
