import pygame

from life_simulation import Life

class Screen:
	def __init__(self, width_screen=500, height_screen=500):
		self.width_screen = width_screen
		self.height_screen = height_screen

		self.life = Life((width_screen, height_screen))

		self.clock = pygame.time.Clock()

		pygame.init()
		self.screen = pygame.display.set_mode((width_screen, height_screen))

		self.running = True

		self.circles_r = 3

		self.main_loop()

		pygame.quit()

	def main_loop(self):
		while self.running:
			self.event_handler()

			# white screen
			self.screen.fill((255, 255, 255))

			preys_coordinates = self.life.get_preys_position()
			# Drawing all preys
			for coordinates in preys_coordinates:
				pygame.draw.circle(self.screen, (0, 255, 0), coordinates, self.circles_r)

			self.life.next_life_iteration()

			pygame.display.flip()

			# set 60 fps
			self.clock.tick(60)

	def event_handler(self):
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

sc = Screen(500, 500)