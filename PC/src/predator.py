import numpy as np
import math
import random

from space_consts import Space_consts

class Predator:
	MAX_PREDATORS = 50
	RADIUS_DETECT = 50
	LAST_LIFE_ITERATION = 400
	VELOCITY_NORM = 2.4

	def __init__(self, x_max, y_max):
		self.x_max = x_max
		self.y_max = y_max

		self.iterations = 0

		self.is_died = False

		self.is_nearly_prey_setting = False

		self.prey_pos = []

		# The starting position is set according to a uniform distribution
		x_position = np.random.uniform(0, x_max, size=(1,))[0]
		y_position = np.random.uniform(0, y_max, size=(1,))[0]
		self.position = [x_position, y_position]

		# The starting velocity is set with random direction
		self.current_X = random.randint(0, Space_consts.VECTORS_MODULO-1)
		self.velocity = Space_consts.X_vectors[self.current_X]

		self.position[0] += Predator.VELOCITY_NORM * self.velocity[0]
		self.position[1] += Predator.VELOCITY_NORM * self.velocity[1]

	def next_iteration(self):
		self.iterations += 1
		if(self.iterations == self.LAST_LIFE_ITERATION):
			self.is_died = True
			return

		if(self.iterations < 80 or not self.is_nearly_prey_setting):
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
		else:
			new_vector_v = np.array(self.prey_pos) - np.array(self.position)
			self.velocity = tuple(new_vector_v / np.linalg.norm(new_vector_v))

		self.position[0] += Predator.VELOCITY_NORM * self.velocity[0]
		self.position[1] += Predator.VELOCITY_NORM * self.velocity[1]

		self.is_nearly_prey_setting = False

	def get_pos(self):
		return (self.position[0], self.position[1])

	def set_pos(self, new_pos):
		self.position[0] = new_pos[0]
		self.position[1] = new_pos[1]

	def get_is_died(self):
		return self.is_died

	def need_to_div(self):
		return np.random.choice([True, False], 1, [0.3, 0.7])[0]

	def set_nearly_prey_pos(self, prey_pos):
		self.is_nearly_prey_setting = True
		self.prey_pos = prey_pos