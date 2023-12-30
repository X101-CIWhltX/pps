import numpy as np
import math
import random

trigonometry_const = math.sqrt(3)/2

X0_vector = (1, 0)
X1_vector = (trigonometry_const, 0.5)
X2_vector = (0.5, trigonometry_const)
X3_vector = (0, 1)
X4_vector = (-0.5, trigonometry_const)
X5_vector = (-1*trigonometry_const, 0.5)
X6_vector = (-1, 0)
X7_vector = (-1*trigonometry_const, -0.5)
X8_vector = (-0.5, -1*trigonometry_const)
X9_vector = (0, -1)
X10_vector = (0.5, -1*trigonometry_const)
X11_vector = (trigonometry_const, -0.5)

X_vectors = (X0_vector, X1_vector, X2_vector, X3_vector,
	X4_vector, X5_vector, X6_vector, X7_vector, X8_vector,
	X9_vector, X10_vector, X11_vector)

vectors_modulo = len(X_vectors)

velocity_norm = 2


class Prey:
	def __init__(self, x_max, y_max):
		self.x_max = x_max
		self.y_max = y_max

		self.velocity_probabilities = [0.97, 0.03/6, 0.03/6, 0.03/6, 0.03/6, 0.03/6, 0.03/6]

		self.x_position = np.random.uniform(0, x_max, size=(1,))[0]
		self.y_position = np.random.uniform(0, y_max, size=(1,))[0]

		vector_offset = random.randint(0, vectors_modulo-1)

		self.bound = 5

		self.velocity = X_vectors[vector_offset]

		self.x_position += velocity_norm*self.velocity[0]
		self.y_position += velocity_norm*self.velocity[1]

	def next_iteration(self):
		index_X = 0

		if (self.x_position < self.bound):
			index_X = random.randint(-2, 2)
			self.velocity = X_vectors[index_X]
		elif (self.x_max - self.x_position < self.bound):
			index_X = random.randint(4, 8)
			self.velocity = X_vectors[index_X]
		elif (self.y_position < self.bound):
			index_X = random.randint(1, 5)
			self.velocity = X_vectors[index_X]
		elif (self.y_max - self.y_position < self.bound):
			index_X = random.randint(7, 11)
			self.velocity = X_vectors[index_X]
		else:
			vector_offset = np.random.choice(list(range(0, 7)), 1, p=self.velocity_probabilities)[0]
			if(vector_offset > 3):
				vector_offset -= 7
			self.velocity = X_vectors[(X_vectors.index(self.velocity) + vector_offset) % vectors_modulo]

		self.x_position += velocity_norm*self.velocity[0]
		self.y_position += velocity_norm*self.velocity[1]


	def get_pos(self):
		return (self.x_position, self.y_position)

