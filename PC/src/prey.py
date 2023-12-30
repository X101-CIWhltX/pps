import numpy as np
import math
import random

trigonometry_const = math.sqrt(3)/2

X0_vector = (1, 0)                               # 0   grade`s
X1_vector = (trigonometry_const, 0.5)            # 30  grade`s
X2_vector = (0.5, trigonometry_const)            # 60  grade`s
X3_vector = (0, 1)                               # 90  grade`s
X4_vector = (-0.5, trigonometry_const)           # 120 grade`s
X5_vector = (-1*trigonometry_const, 0.5)         # 150 grade`s
X6_vector = (-1, 0)                              # 180 grade`s
X7_vector = (-1*trigonometry_const, -0.5)        # 210 grade`s
X8_vector = (-0.5, -1*trigonometry_const)        # 240 grade`s
X9_vector = (0, -1)                              # 270 grade`s
X10_vector = (0.5, -1*trigonometry_const)        # 300 grade`s
X11_vector = (trigonometry_const, -0.5)          # 330 grade`s

X_vectors = (X0_vector, X1_vector, X2_vector, X3_vector,
	X4_vector, X5_vector, X6_vector, X7_vector, X8_vector,
	X9_vector, X10_vector, X11_vector)

VECTORS_MODULO = len(X_vectors)  # 12 vector`s from 0 to 11
VELOCITY_NORM = 2
MAX_PREYS = 150
BOUND_SIZE = 5

# 0.95 - the probability of maintaining the direction, 0.03/6 - the probability of a change of direction
velocity_probabilities = [0.97, 0.03/6, 0.03/6, 0.03/6, 0.03/6, 0.03/6, 0.03/6]

class Prey:
	def __init__(self, x_max, y_max):
		self.x_max = x_max
		self.y_max = y_max

		# The starting position is set according to a uniform distribution
		x_position = np.random.uniform(0, x_max, size=(1,))[0]
		y_position = np.random.uniform(0, y_max, size=(1,))[0]
		self.position = [x_position, y_position]

		self.cycle = random.randint(150, 250)  # The number of life iterations (life cycle) when prey can split into 2 preys
		self.part_cycle = 0

		# The starting velocity is set with random direction
		self.current_X = random.randint(0, VECTORS_MODULO-1)
		self.velocity = X_vectors[self.current_X]

		self.position[0] += VELOCITY_NORM * self.velocity[0]
		self.position[1] += VELOCITY_NORM * self.velocity[1]

	def next_iteration(self):
		# If the prey reaches one of the edges of the map, then we change its direction of movement from the edge of the map
		if (self.position[0] < BOUND_SIZE):
			self.current_X = random.randint(-2, 2)
			self.velocity = X_vectors[self.current_X]
		elif (self.x_max - self.position[0] < BOUND_SIZE):
			self.current_X = random.randint(4, 8)
			self.velocity = X_vectors[self.current_X]
		elif (self.position[1] < BOUND_SIZE):
			self.current_X = random.randint(1, 5)
			self.velocity = X_vectors[self.current_X]
		elif (self.y_max - self.position[1] < BOUND_SIZE):
			self.current_X = random.randint(7, 11)
			self.velocity = X_vectors[self.current_X]
		else:
			# With a probability of 0.95, the prey will not change its direction of movement,
			# and with a probability of 0.05, the prey may change its direction of movement by 30 or 60 degrees
			vector_offset = np.random.choice(list(range(0, 7)), 1, p=velocity_probabilities)[0]

			# 0 - turn by 0 degrees 
			# 1 - turn by 30 degrees counterclockwise
			# 2 - turn by 60 degrees counterclockwise
			# 3 - turn by 90 degrees counterclockwise
			# 4 (= -3) - turn by 30 degrees clockwise
			# 5 (= -2) - turn by 60 degrees clockwise
			# 6 (= -1) - turn by 90 degrees clockwise
			if(vector_offset > 3):
				vector_offset -= 7

			self.current_X = (self.current_X + vector_offset) % VECTORS_MODULO
			self.velocity = X_vectors[self.current_X]

		self.position[0] += VELOCITY_NORM * self.velocity[0]
		self.position[1] += VELOCITY_NORM * self.velocity[1]

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
			return np.random.choice([True, False], 1, [0.15, 0.85])[0]

		return False
