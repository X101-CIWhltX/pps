import numpy as np
import math
import random

from space_consts import Space_consts

class Prey:
	MAX_PREYS = 70
	VELOCITY_NORM = 2
	def __init__(self, x_max, y_max):
		self.x_max = x_max
		self.y_max = y_max

		# The starting position is set according to a uniform distribution
		x_position = np.random.uniform(0, x_max, size=(1,))[0]
		y_position = np.random.uniform(0, y_max, size=(1,))[0]
		self.position = [x_position, y_position]

		self.cycle = random.randint(50, 150)  # The number of life iterations (life cycle) when prey can split into 2 preys
		self.part_cycle = 0

		# The starting velocity is set with random direction
		self.current_X = random.randint(0, Space_consts.VECTORS_MODULO-1)
		self.velocity = Space_consts.X_vectors[self.current_X]

		self.position[0] += Prey.VELOCITY_NORM * self.velocity[0]
		self.position[1] += Prey.VELOCITY_NORM * self.velocity[1]

	def next_iteration(self):
		# If the prey reaches one of the edges of the map, then we change its direction of movement from the edge of the map
		if (self.position[0] < Space_consts.BOUND_SIZE):
			self.current_X = random.randint(-2, 2)
			self.velocity = Space_consts.X_vectors[self.current_X]
		elif (self.x_max - self.position[0] < Space_consts.BOUND_SIZE):
			self.current_X = random.randint(4, 8)
			self.velocity = Space_consts.X_vectors[self.current_X]
		elif (self.position[1] < Space_consts.BOUND_SIZE):
			self.current_X = random.randint(1, 5)
			self.velocity = Space_consts.X_vectors[self.current_X]
		elif (self.y_max - self.position[1] < Space_consts.BOUND_SIZE):
			self.current_X = random.randint(7, 11)
			self.velocity = Space_consts.X_vectors[self.current_X]
		else:
			# With a probability of 0.95, the prey will not change its direction of movement,
			# and with a probability of 0.05, the prey may change its direction of movement by 30 or 60 degrees
			vector_offset = np.random.choice(list(range(0, 7)), 1, p=Space_consts.velocity_probabilities)[0]

			# 0 - turn by 0 degrees 
			# 1 - turn by 30 degrees counterclockwise
			# 2 - turn by 60 degrees counterclockwise
			# 3 - turn by 90 degrees counterclockwise
			# 4 (= -3) - turn by 30 degrees clockwise
			# 5 (= -2) - turn by 60 degrees clockwise
			# 6 (= -1) - turn by 90 degrees clockwise
			if(vector_offset > 3):
				vector_offset -= 7

			self.current_X = (self.current_X + vector_offset) % Space_consts.VECTORS_MODULO
			self.velocity = Space_consts.X_vectors[self.current_X]

		self.position[0] += Prey.VELOCITY_NORM * self.velocity[0]
		self.position[1] += Prey.VELOCITY_NORM * self.velocity[1]

		# With every iteration increment part_cycle
		self.part_cycle += 1


	def get_pos(self):
		return (self.position[0], self.position[1])

	def set_pos(self, new_position):
		self.position[0] = new_position[0]
		self.position[1] = new_position[1]

	# 
	def time_to_div(self):
		# When the prey life cycle ends, the production with a probability of 0.005 can be divided into 2 preys, then
		# reset part_cycle
		if(self.part_cycle >= self.cycle):
			self.part_cycle = 0
			return np.random.choice([True, False], 1, [0.5, 0.5])[0]

		return False
