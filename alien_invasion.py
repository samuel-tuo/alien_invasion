#encoding: utf-8
""" 
@project = alien_invsion
@file = alien_invasion
@author = xiaotuo
@create_time = 2020/2/17 9:43 PM
"""
import  sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,
		 ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(ai_settings, screen) # 创建一首飞船
	bullets = Group()                # 创建一个用于储存子弹的编组

	# 开始游戏的主循环
	while True:
		# 监视鼠标和键盘事件
		gf.check_events(ai_settings, screen, ship, bullets)
		# 更新飞船位置信息
		ship.update()
		bullets.update()
		# 删除已经消失的子弹
		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
		print(len(bullets))
		# 更新屏幕显示
		gf.update_screen(ai_settings, screen, ship, bullets)
run_game()

