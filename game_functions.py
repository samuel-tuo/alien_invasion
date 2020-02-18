#encoding: utf-8
""" 
@project = alien_invasion
@file = game_functions
@author = xiaotuo
@create_time = 2020/2/18 8:53 AM
"""
import sys
import pygame
from bullet import Bullet

def check_events(ai_setting, screen, ship, bullets):
	"""响应按键和鼠标"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_setting, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

def check_keydown_events(event, ai_setting, screen, ship, bullets):
	"""响应按下按键"""
	if event.key == pygame.K_RIGHT:
		# 向右移动飞船
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		# 向左移动飞船
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		# 飞船向前移动
		ship.moving_forward = True
	elif event.key == pygame.K_DOWN:
		# 飞船向后移动
		ship.moving_back = True
	elif event.key == pygame.K_SPACE:
		fire_bullets(ai_setting, screen, ship, bullets)


def fire_bullets(ai_setting, screen, ship, bullets):
	"""如果子弹数量没达到限制，就发射一颗"""
	# 创建一颗子弹，并将其加入到bullets编组中
	if len(bullets) < ai_setting.bullets_allowed:
		new_bullet = Bullet(ai_setting, screen, ship)
		bullets.add(new_bullet)

def check_keyup_events(event, ship):
	"""响应松开按键"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		# 飞船向前移动
		ship.moving_forward = False
	elif event.key == pygame.K_DOWN:
		# 飞船向后移动
		ship.moving_back = False

def update_screen(ai_settings,screen,ship, bullets):
	"""更新屏幕上的图像，并切换到新屏幕"""
	# 每次循环重绘屏幕
	screen.fill(ai_settings.bg_color)
	ship.blitme()  # 绘制飞船
	# 绘制子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	# 让最近绘制的屏幕可见
	pygame.display.flip()


def update_bullets(bullets):
	"""更新子弹的位置，并删除超出屏幕的子弹"""
	# 更新子弹的位置
	bullets.update()
	# 删除已经消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)