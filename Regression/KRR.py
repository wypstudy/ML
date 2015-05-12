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
  k = mlpy.kernel_gaussian(x, x, sigma=1)
  kt = mlpy.kernel_gaussian(t, x, sigma=1)
  krr = mlpy.KernelRidge(lmb=0.01)
  krr.learn(k, y)

  print "out......"
  re = krr.pred(t)
  return re