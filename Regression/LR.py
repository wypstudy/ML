# -*- coding: utf-8 -*-
import numpy
import math

def f(TrainingMatrix, TrainingResult, TestMatrix, TrainTime, TrainRate):
  RowSize = len(TrainingMatrix)
  ColSize = len(TrainingMatrix[0])
  TrainingMatrix = numpy.array(TrainingMatrix)
  TrainingResult = numpy.array(TrainingResult)
  theta = []
  for i in range(ColSize):
    theta.append(0.0)
  oldTheta = numpy.array(theta)
  theta = numpy.array(theta)
  rate = TrainRate
  loss = []

  for k in range(TrainTime):
    err = TrainingMatrix.dot(theta) - TrainingResult

    loss.append(reduce(lambda x, y: x + y, map(lambda x: abs(x), err)))
    if k > 0:
      if loss[k] < loss[k-1]:
        oldTheta = theta
      if loss[k] >= loss[k-1]:
        print k
        break
    print "iterative " + str(k) + " loss = " + str(loss[k])

    for i in range(ColSize):
      jTheta = err.dot(TrainingMatrix[0:RowSize, i])
      theta[i] = theta[i] - rate * jTheta


  rs = ColSize
  result = []
  for line in TestMatrix:
    h = 0
    for k in range(rs):
      h += oldTheta[k] * line[k]
    result.append(h)

  return result
