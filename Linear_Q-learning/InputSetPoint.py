# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 09:17:50 2016

@author: isaaczst
"""
import numpy as np
class InputSetPoint(object,iinputOption=0):
    def __init__(self,inputOption):
        if inputOption==1:
            self.setPoint=np.ones((100))
            self.setPoint[:1]=0
        elif inputOption==2:
            pass
        else:
            pass
        return        
        
            