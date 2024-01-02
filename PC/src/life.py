from prey import Prey
from predator import Predator
import math

class Life:
	def __init__(self, field_size, starting_count_preys = 5):
		self.width_screen = field_size[0]
		self.height_screen = field_size[1]

		self.count_preys = starting_count_preys
		self.preys = []

		self.count_predators = 0
		self.predators = []

		for i in range(self.count_preys):
			prey = Prey(self.width_screen, self.height_screen)
			self.preys.append(prey)

	def next_life_iteration(self):
		if(len(self.preys) == 0):
			prey = Prey(self.width_screen, self.height_screen)
			self.preys.append(prey)

		need_to_contain_preys_position = False
		preys_position = []

		if(len(self.predators) > 0):
			need_to_contain_preys_position = True

		for prey in self.preys:
			prey.next_iteration()

			if(need_to_contain_preys_position):
				preys_position.append(prey.get_pos())

			# We limit the amount of preys to the value MAX_PREYS
			if(prey.time_to_div() and len(self.preys) <= Prey.MAX_PREYS):
				new_prey = Prey(self.width_screen, self.height_screen)
				new_prey.set_pos(prey.get_pos())
				self.preys.append(new_prey)

		if(len(self.preys) > 40 and len(self.predators) == 0):
			predator = Predator(self.width_screen, self.height_screen)
			self.predators.append(predator)

			for prey in self.preys:
				preys_position.append(prey.get_pos())

		new_predators = []
		for predator in self.predators:
			if(predator.get_is_died()):
				self.predators.remove(predator)
				continue
			nearly_prey_coordinates = None
			nearly_distance = None

			for prey_pos in preys_position:
				predator_pos = predator.get_pos()
				distance = math.sqrt((prey_pos[0] - predator_pos[0])**2 + (prey_pos[1] - predator_pos[1])**2)

				if(distance <= Predator.RADIUS_DETECT):
					if(distance < 3.4):
						self.preys.pop(preys_position.index(prey_pos))
						preys_position.remove(prey_pos)
						if(predator.need_to_div()):
							new_predator = Predator(self.width_screen, self.height_screen)
							new_predator.set_pos(predator.get_pos())
							new_predators.append(new_predator)
					else:
						if(nearly_prey_coordinates == None):
							nearly_prey_coordinates = prey_pos
							nearly_distance = distance
						elif(distance < nearly_distance):
							nearly_distance = distance

			if(nearly_prey_coordinates != None):
				predator.set_nearly_prey_pos(nearly_prey_coordinates)

			predator.next_iteration()

		self.predators.extend(new_predators)



	def get_preys_position(self):
		return [prey.get_pos() for prey in self.preys]

	def get_predators_position(self):
		return [predator.get_pos() for predator in self.predators]
