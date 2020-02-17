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

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,
		 ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	bg_color = ai_settings.bg_color # 设置背景色

	# 开始游戏的主循环
	while True:
		# 监视鼠标和键盘事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		# 每次循环时都重绘屏幕
		screen.fill(bg_color)
		# 让最近绘制的屏幕可见
		pygame.display.flip()

run_game()

