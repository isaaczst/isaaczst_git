# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 07:21:41 2016

@author: isaaczst
"""
import numpy
from InputSetPoint import InputSetPoint
import Plant
import Task

inputSetPoint=InputSetPoint(1)
plant=Plant(1)
task=Task(1,inputSetPoint,plant)
def main():
    for i in range(task.timeStepRange):
        task.simu()
        task.approxQ()
        task.genAction()
    task.plotResult()
    

if __name__ == '__main__':
  main()



