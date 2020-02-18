#encoding: utf-8
""" 
@project = alien_invasion
@file = ship
@author = xiaotuo
@create_time = 2020/2/18 12:03 AM
"""
import pygame

class Ship():
	def __init__(self, ai_settings, screen):
		"""初始化飞船并设定其初始位置"""
		self.screen = screen
		self.ai_settings = ai_settings

		# 加载飞船图像并获取其外接矩形
		ship_picture = pygame.image.load('images/ship.bmp')
		# 将图片旋转
		self.image = pygame.transform.rotate(ship_picture, -90)
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# 每艘新飞船放在屏幕中央
		self.rect.bottom= self.screen_rect.centery
		self.rect.left = self.screen_rect.left

		# 在飞船的属性center中储存小数值
		self.bottom = float(self.rect.bottom)
		self.left = float(self.rect.left)

		# 移动标志
		self.moving_right = False
		self.moving_left = False
		self.moving_forward = False
		self.moving_back = False

	def update(self):
		"""根据移动标志调整飞船的位置"""
		# 飞船的右侧坐标小于屏幕的右侧坐标
		if self.moving_right and self.rect.bottom < self.screen_rect.bottom:
			self.bottom += self.ai_settings.ship_speed_factor
		# 飞船的左侧坐标大于屏幕的左侧坐标
		if self.moving_left and self.rect.top > self.screen_rect.top:
			self.bottom -= self.ai_settings.ship_speed_factor
		# 飞船的顶部坐标大于屏幕的顶部坐标
		if self.moving_forward and self.rect.right < self.screen_rect.right:
			self.left += self.ai_settings.ship_speed_factor
		# 飞船的底部坐标小于屏幕的底部坐标
		if self.moving_back and self.rect.left > self.screen_rect.left:
			self.left -= self.ai_settings.ship_speed_factor

		# 根据self.center更新rect对象
		self.rect.bottom = self.bottom
		self.rect.left = self.left

	def blitme(self):
		"""在指定的位置绘制飞船"""
		self.screen.blit(self.image, self.rect)