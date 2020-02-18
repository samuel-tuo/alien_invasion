#encoding: utf-8
""" 
@project = alien_invsion
@file = settings
@author = xiaotuo
@create_time = 2020/2/17 10:05 PM
"""
class Settings():
	"""储存《外星人入侵》的所有设置的类"""

	def __init__(self):
		"""初始化游戏的设置"""
		# 屏幕设置
		self.screen_width = 800
		self.screen_height = 400
		self.bg_color = (230, 230, 230)

		# setting for ship
		self.ship_speed_factor = 1.5

		# setting for bullet
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60