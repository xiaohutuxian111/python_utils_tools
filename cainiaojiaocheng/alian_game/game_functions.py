"""
@FileName：game_functions.py
@Author：stone
@Time：2023/4/18 17:55
@Description:事件检查
"""
import sys
import pygame
from bullet import Bullets
from alien import Alien


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets)


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
    elif event.key == pygame.K_Q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """没有达到子弹限制，发射一个子弹"""
    if len(bullets) < ai_settings.bullet_allowed:
        #  创建一个子弹将子弹放到编组中
        new_bullet = Bullets(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, ship, bullets, aliens):
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
    #  让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_fleet(ai_settings, screen, aliens):
    """创建外星人"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space = ai_settings.screen_width - 2 * alien_width
    print(available_space)
    number_aliens_x = int(available_space / (2 * alien_width))
    print(number_aliens_x)
    # 创建一行外星人
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + alien_width * 2 * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
