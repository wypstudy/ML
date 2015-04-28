# -*- coding: utf-8 -*-
from numpy import *

def f(TrainingMatrix, TrainingResult, TestMatrix):
  theta = [[]]
  for i in range(Size):
    theta[0].append(0)
  loss = 1000.0
  rate = 0.01
  RowSize = len(TrainingMatrix)
  ColSize = len(TrainingMatrix[0])

  for i in range(100):
    if loss < 0.0001:
      break
    error_sum = 0.0
    for j in range(RowSize):
      h = 0.0
      for k in range(ColSize):
        h += TrainingMatrix[j][k] * theta[0][k]
      error_sum = TrainingResult[j] - h
      for k in range(ColSize):
        theta[0][k] += rate * error_sum * TrainingMatrix[j][k]

  return matrix(TestMatrix) * matrix(theta)

