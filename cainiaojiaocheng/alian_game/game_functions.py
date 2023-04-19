"""
@FileName：game_functions.py
@Author：stone
@Time：2023/4/18 17:55
@Description:事件检查
"""
import sys
import time

import pygame
from bullet import Bullets
from alien import Alien


def check_play_button(ai_settings, stats, screen, play_button, mouse_x, mouse_y, ship, aliens, bullets):
    """点击开始按钮事件"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:

        # 重置游戏统计信息
        stats.reset_stats()
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()
        stats.game_active = True
        # 清空外星人和子弹
        bullets.empty()
        aliens.empty()

        # 新建一批外星人，飞船在中央
        create_fleet(ai_settings, screen, ship, aliens)

        ship.center_ship()
        # 隐藏光标
        pygame.mouse.set_visible(False)


def check_events(ai_settings, screen, ship, aliens, bullets, play_button, stats):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, stats, screen, play_button, mouse_x, mouse_y, ship, aliens, bullets)


def check_keyup_events(event, ship):
    """键盘抬起事件"""
    if event.key == pygame.K_RIGHT:
        # x向右移动飞船
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_keydown_events(event, ship, ai_settings, screen, bullets):
    """键盘按下事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_F2:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """没有达到子弹限制，发射一个子弹"""
    if len(bullets) < ai_settings.bullet_allowed:
        #  创建一个子弹将子弹放到编组中
        new_bullet = Bullets(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, stats, ship, bullets, aliens, play_button,sb):
    """绘制屏幕操作"""
    # 设置背景色
    bg_color = ai_settings.bg_color
    screen.fill(bg_color)
    # 绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 绘制飞船
    ship.blitme()
    # 绘制外星人
    aliens.draw(screen)

    #  如果游戏处于非活动的状态，则绘制按钮
    if not stats.game_active:
        play_button.draw_button()
    #  显示得分
    sb.show_score()
    #  让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, bullets, aliens):
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets)
    bullets.update()


def check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets):
    """检测子弹与飞船的碰撞"""
    # 检查是否有子弹击中了外星人
    # 存在直接删除子弹和外新人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # 删除所有的子弹新建一群外星人
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)


def check_alien_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人到达屏幕的低端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """跟新外星人位置"""
    # 检查是否有外星人在边缘
    check_feet_edges(ai_settings, aliens)
    aliens.update()
    # 检测飞船和外星人碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        print("ship hit!")
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    # 检查外星人是否有到达底端
    check_alien_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """相应外星人碰飞穿"""
    if stats.ship_limit > 0:
        stats.ship_limit -= 1

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 新建外星人，并将飞船放在屏幕中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        time.sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def change_fleet_direction(ai_settings, aliens):
    """将外星人下移，并改变方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_drop_speed
    ai_settings.alien_direction *= -1


def check_feet_edges(ai_settings, aliens):
    """有外星人到达边缘时执行相应措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人组"""
    alien = Alien(ai_settings, screen)

    alien_number_x = get_number_aliens_x(ai_settings, alien.rect.width)
    alien_number_y = get_number_aliens_y(ai_settings, alien.rect.height, ship.rect.height)

    # 创建一行外星人
    for number_x in range(alien_number_x):
        for number_y in range(alien_number_y):
            create_alien(ai_settings, screen, aliens, number_x, number_y)


def create_alien(ai_settings, screen, aliens, alien_number_x, alien_number_y):
    """创建一个外星人"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + alien_width * 2 * alien_number_x
    alien.y = alien_height + alien_height * 2 * alien_number_y
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def get_number_aliens_y(ai_settings, alien_height, ship_height):
    """计算外星人有多少行"""
    available_space = ai_settings.screen_height - 3 * alien_height - ship_height
    number_aliens_y = int(available_space / (2 * alien_height))
    return number_aliens_y


def get_number_aliens_x(ai_settings, alien_width):
    """计算每一行有多少外杏仁"""
    available_space = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space / (2 * alien_width))
    return number_aliens_x
