from prey import Prey

class Life:
	def __init__(self, field_size, starting_count_preys = 5):
		self.width_screen = field_size[0]
		self.height_screen = field_size[1]
		self.count_preys = starting_count_preys
		self.preys = []

		for i in range(self.count_preys):
			prey = Prey(self.width_screen, self.height_screen)
			self.preys.append(prey)

	def next_life_iteration(self):
		for prey in self.preys:
			prey.next_iteration()

			# We limit the amount of preys to the value MAX_PREYS
			if(prey.time_to_div() and len(self.preys) <= Prey.MAX_PREYS):
				new_prey = Prey(self.width_screen, self.height_screen)
				new_prey.set_pos(prey.get_pos())
				self.preys.append(new_prey)

	def get_preys_position(self):
		return [prey.get_pos() for prey in self.preys]