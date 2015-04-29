# -*- coding: utf-8 -*-
from numpy import *
import math

def f(TrainingMatrix, TrainingResult, TestMatrix):
  RowSize = len(TrainingMatrix)
  ColSize = len(TrainingMatrix[0])
  oldTheta = []
  theta = []
  for i in range(ColSize):
    theta.append(0)
  rate = 0.000001
  loss = []

  for k in range(10000):
    err = []
    jTheta = []
    hs = 0
    for j in range(RowSize):
      err.append(0.0)
      for i in range(ColSize):
        err[hs] += TrainingMatrix[j][i] * theta[i]
      err[hs] -= TrainingResult[j]
      hs += 1

    loss.append(reduce(lambda x, y: x + y, map(lambda x: abs(x), err)))
    if k > 0:
      if loss[k] < loss[k-1]:
        oldTheta = theta
      if loss[k] >= loss[k -1]:
        print k
        break
    print "iterative " + str(k) + " loss = " + str(loss[k])

    for i in range(ColSize):
      jTheta = 0.0
      for j in range(RowSize):
        jTheta += err[j] * TrainingMatrix[j][i]
      theta[i] = theta[i] - rate * jTheta


  rs = ColSize
  result = []
  for line in TestMatrix:
    h = 0
    for k in range(rs):
      h += oldTheta[k] * line[k]
    result.append(h)

  return result
