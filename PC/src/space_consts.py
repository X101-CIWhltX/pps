import math

class Space_consts:
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
	BOUND_SIZE = 5

	# 0.95 - the probability of maintaining the direction, 0.03/6 - the probability of a change of direction
	velocity_probabilities = [0.97, 0.03/6, 0.03/6, 0.03/6, 0.03/6, 0.03/6, 0.03/6]