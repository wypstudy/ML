# -*- coding: utf-8 -*-
# Author : banehallow
# Email  : 1140664142@qq.com

import numpy
import math
import mlpy

def f(TrainIn, TrainOut, TestIn):
  print "init......"
  x = numpy.array(TrainIn)
  y = numpy.array(TrainOut)
  t = numpy.array(TestIn)

  print "learn......"
  ldac = mlpy.LDAC()
  ldac.learn(x, y)

  print "out......"
  re = ldac.pred(t)
  return re