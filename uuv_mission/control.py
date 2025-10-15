import numpy as np

class Controller:
	def __init__(self, KP=0.15, KD=0.6):
		self.KP = KP
		self.KD = KD
		self.prev_error = 0.0

	def reset(self):
		self.prev_error = 0.0

	def get_action(self, reference, output):
		error = reference - output
		derivative = error - self.prev_error
		action = self.KP * error + self.KD * derivative
		self.prev_error = error
		return action
