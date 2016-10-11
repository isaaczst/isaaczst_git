# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 09:03:38 2016

@author: isaaczst
"""
import numpy as np
class Plant(object):
    def __init__(self,plantOption):
        if plantOption==1:
            self.A=np.array([[1.,1.],[0.,1.]])
            self.B=np.array([[1.],[0.]])