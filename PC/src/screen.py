import pygame

from prey import Prey

class Screen:
	def __init__(self, width_screen=500, height_screen=500):
		self.width_screen = width_screen
		self.height_screen = height_screen

		self.clock = pygame.time.Clock()

		pygame.init()

		self.screen = pygame.display.set_mode((width_screen, height_screen))

		self.running = True

		self.preys = []

		for i in range(100):
			prey = Prey(width_screen, height_screen)
			self.preys.append(prey)


		self.circles_r = 3
		self.count = 0

		self.main_loop()

		pygame.quit()

	def main_loop(self):
		while self.running:

			self.event_handler()

			self.screen.fill((255, 255, 255))

			for prey in self.preys:
				pygame.draw.circle(self.screen, (0, 255, 0),prey.get_pos(), self.circles_r)

			for prey in self.preys:	
				prey.next_iteration()


			pygame.display.flip()
			self.clock.tick(60)

	def event_handler(self):
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

sc = Screen(500, 500)