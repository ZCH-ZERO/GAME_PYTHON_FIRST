class Settings():
	"""存储《外星人入侵》 的所有设置的类"""

	def __init__(self):
		"""初始化游戏的设置"""
		# 屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)

		# 飞船的设置---设置飞船的速度----这里的改动是将ship_speed_factor的初始值设置为1.5
		# 							------需要飞船移动时，我们将移动1.5像素而不是 1 像素
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 1
		# 子弹设置
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullets_allowed = 3

