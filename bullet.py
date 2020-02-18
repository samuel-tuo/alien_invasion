#encoding: utf-8
""" 
@project = alien_invasion
@file = bullet
@author = xiaotuo
@create_time = 2020/2/18 11:45 AM
"""
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""一个对飞船发射的子弹进行管理的类"""
	def __init__(self, ai_setting, screen, ship):
		"""在飞船所在的位置创建一个子弹"""
		super().__init__()
		self.screen = screen

		# 在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
		self.rect = pygame.Rect(0, 0, ai_setting.bullet_width,
		                        ai_setting.bullet_height)
		self.rect.bottom = ship.rect.bottom
		self.rect.center = ship.rect.center

		# 储存小数表示子弹的位置
		self.x = float(self.rect.x)
		self.color = ai_setting.bullet_color
		self.speed_factor = ai_setting.bullet_speed_factor

	def update(self):
		"""向上移动子弹"""
		# 更新表示子弹的小数值
		self.x += self.speed_factor
		# 更新表示子弹的rect的位置
		self.rect.x = self.x

	def draw_bullet(self):
		"""在屏幕上绘制子弹"""
		pygame.draw.rect(self.screen, self.color, self.rect)