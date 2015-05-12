# -*- coding: utf-8 -*-
# Author : banehallow
# Email  : 1140664142@qq.com

import numpy
import math

def f(TrainingMatrix, TrainingResult, TestMatrix, TrainTime, TrainRate):
  RowSize = len(TrainingMatrix)
  ColSize = len(TrainingMatrix[0])
  TrainingMatrix = numpy.array(TrainingMatrix)
  TrainingResult = numpy.array(TrainingResult)
  rate = TrainRate
  result = []
  TestSize = len(TestMatrix)
  for i in range(len(TestMatrix)):
    theta = []
    oldTheta = []
    weight = []
    for j in range(RowSize):
      dis = numpy.array(TestMatrix[i])-numpy.array(TrainingMatrix[j])
      nw = math.exp(-1*(dis.dot(dis))/2)
      weight.append(nw)
      
    for j in range(ColSize):
      theta.append(0.0)
    theta = numpy.array(theta)
    oldTheta = theta
    loss = 0.1
    oldloss = loss
    for j in range(TrainTime):
      err = TrainingMatrix.dot(theta) - TrainingResult
      for k in range(len(err)):
        err[k] *= weight[k] 
      newloss = reduce(lambda x, y: x + y, map(lambda x: abs(x), err))
      if j == 0:
        oldloss = newloss
      print "test " + str(i) + " iterative " + str(j) + " loss = " + str(newloss)
      if newloss < loss:
        oldTheta = theta
        break
      if newloss > oldloss:
        theta = oldTheta
        break
      if newloss <= oldloss:
        oldTheta = theta
      for k in range(ColSize):
        jTheta = err.dot(TrainingMatrix[0:RowSize, k])
        theta[k] = theta[k] - rate * jTheta
    newResult = 0.0
    for j in range(ColSize):
      newResult += theta[j] * TestMatrix[i][j]
    result.append(newResult)
  return result
