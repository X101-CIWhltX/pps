import pygame

from prey import Prey
import prey as p

class Screen:
	def __init__(self, width_screen=500, height_screen=500):
		self.width_screen = width_screen
		self.height_screen = height_screen

		self.clock = pygame.time.Clock()

		pygame.init()
		self.screen = pygame.display.set_mode((width_screen, height_screen))

		self.running = True

		self.preys = []
		self.count_preys = 5

		for i in range(self.count_preys):
			prey = Prey(width_screen, height_screen)
			self.preys.append(prey)

		self.circles_r = 3

		self.main_loop()

		pygame.quit()

	def main_loop(self):
		while self.running:
			self.event_handler()

			# white screen
			self.screen.fill((255, 255, 255))

			# Drawing all preys
			for prey in self.preys:
				pygame.draw.circle(self.screen, (0, 255, 0), prey.get_pos(), self.circles_r)

			for prey in self.preys:	
				prey.next_iteration()

				# We limit the amount of preys to the value MAX_PREYS
				if(prey.time_to_div() and len(self.preys) <= p.MAX_PREYS):
					new_prey = Prey(self.width_screen, self.height_screen)
					new_prey.set_pos(prey.get_pos())
					self.preys.append(new_prey)

			pygame.display.flip()

			# set 60 fps
			self.clock.tick(60)

	def event_handler(self):
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

sc = Screen(500, 500)