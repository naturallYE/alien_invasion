import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group



def run_game():
    # 创建一个clock对象以便控制游戏运行速度
    clock = pygame.time.Clock()
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien_Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于储存子弹的编组
    bullets = Group()

    # 创建一个用于储存外星人的编组
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)
        # 限制为120帧
        clock.tick(120)


run_game()
