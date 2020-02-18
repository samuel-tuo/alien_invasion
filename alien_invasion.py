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

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,
		 ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(screen) # 创建一首飞船

	# 开始游戏的主循环
	while True:
		# 监视鼠标和键盘事件
		gf.check_events(ship)
		# 更新飞船位置信息
		ship.update()
		# 更新屏幕显示
		gf.update_screen(ai_settings,screen,ship)
run_game()

