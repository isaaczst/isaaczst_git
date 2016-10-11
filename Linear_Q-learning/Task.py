# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 07:56:16 2016

@author: isaaczst
"""
import numpy as np
import matplotlib.pyplot as plt

class Task(object):
    def __init__(self,taskOption,inputSetPoint,plant):
        self.timeStepIndex=0        
        self.loadTask(plant)
    def loadTask(self):
        self.timeStepRange = inputSetPoint.setPoint.shape[0]
        self.state=np.zeros((plant.A.shpae[0],self.timeStepRange))
        self.action=np.zeros((plant.B.shape[1],self.timeStepRange))
        self.initLQR(taskOption)
    def simu(self):
        self.state[:,self.timeStepIndex+1]=np.matmul(plant.A,self.state[:,self.timeStepIndex])+np.matmul(plant.B, self.action[:,self.timeStepIndex])
    def approxQ(self):
        self.valueQ()
        self.rls1(self.dStateQ,self.dQ[self.timeStepIndex],self.cov,self.vecH[self.timeStepIndex])
    def genAction(self):
        self.action[self.timeStepIndex+1]=-np.matmul(np.matmul(np.mat(ss).I,ss1),self.state[self.timeStepIndex])
    def plotResult(self):
        plt.subplot(2,1,1)
        plt.title('input')
        plt.plot(np.arange(self.timeStepRange),self.state[0,:])
        plt.subplot(2,1,2)
        plt.title('output')
        plt.legend('simulation','setpoint')
        plt.plot(np.arange(self.timeStepRange),self.action[0,:])
    def initLQR(self,initOption=0):
        if initOption==1:
            self.P=np.random.random((self.A.shape[0]))
            self.Q=np.eye((self.A.shape[0]))
            self.R=np.eye((self.B.shape[0]))
            self.gamma=1
            Hxx=self.Q+np.matmul(self.A.T,np.matmul(self.P,self.A))
            Hxu=np.matmul(self.A.T,np.matmul(self.P,self.B))
            Hux=np.matmul(self.B.T,np.matmul(self.P,self.A))
            Huu=self.R+np.matmul(self.B.T,np.matmul(self.P,self.B))
            H=np.vstack((np.hstack((Hxx,Hxu)),np.hstack((Hux,Huu))))
            self.vecH[self.timeStepIndex]=H.reshape(H.shape[0]*H.shape[1],1)
            self.cov=np.random.random((self.A.shape[0]+self.B.shape[1]))
        else:
            self.P=np.random.random((self.A.shape))
    def valueQ(self): 
        state_new=self.state[:,self.timeStepIndex]
        action_new=self.action[:,self.timeStepIndex]
        self.dQ[self.timeStepIndex]=state_new.T.dot(np.matmul(self.Q,state_new))+action_new.T.dot(np.matmul(self.Q,action_new))
        stateQ_new=np.vstack((self.state[:,self.timeStepIndex],self.action[:,self.timeStepIndex]))
        kron_new=np.kron(stateQ_new,stateQ_new)
        stateQ_old=np.vstack((self.state[:,self.timeStepIndex-1],self.action[:,self.timeStepIndex-1]))
        kron_old=np.kron(stateQ_old,stateQ_old)
        self.dStateQ=stateQ_new-stateQ_old
        Q_new=self.vecH[self.timeStepIndex].dot(stateQ_new)
        Q_old=self.vecH[self.timeStepIndex].dot(stateQ_old)
        self.dQ_hat[self.timeStepIndex]=Q_new-Q_old
    def rls1(self,x,y,p,th,lam=1): # https://mail.scipy.org/pipermail/scipy-user/2007-October/013889.html
         a=np.matmul(p,x)
         g=(np.matmul(x.T,a)+lam).T #g=1/(x'*a+lam);
         k=np.matmul(g,a)
         e=y-np.matmul(x.T,th)
         self.vecH[self.timeStepIndex]=th+np.matmul(k,e)
         self.cov=(p-np.matmul(g,np.matmul(a,a.T)))/lam;


            

        
        