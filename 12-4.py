import pygame
def run_game():
    # 创建一个clock对象以便控制游戏运行速度
    clock = pygame.time.Clock()
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen_width = 600
    screen_height = 800
    bg_color = (230, 230, 230)
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("12-4")


    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(event)
            if event.type == pygame.KEYUP:
                print(event)
        # 更新屏幕
        # 每次循环时都重绘屏幕
        screen.fill(bg_color)

        # 让最近绘制的屏幕可见
        pygame.display.flip()
        # 限制为120帧
        clock.tick(120)



run_game()