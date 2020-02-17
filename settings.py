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
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)