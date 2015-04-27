# -*- coding: utf-8 -*-

def f(TrainingMatrix, TrainingResult, TestMatrix):
  theta = []
  for i in range(Size):
    theta.append(0)
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
        h += TrainingMatrix[j][k] * theta[k]
      error_sum = TrainingResult[j] - h
      for k in range(ColSize):
        theta[k] += rate * error_sum * TrainingMatrix[j][k]

  ans = []

  return ans

