import numpy as np


class Data:

	def __init__(self, numInstance, numDataSize):
		self.X = np.zeros((numDataSize, numInstance))
		self.label = np.zeros(numDataSize)

