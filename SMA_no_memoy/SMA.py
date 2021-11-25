#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 22:45:23 2021

@author: oem
"""
from time import time
import environment as env
import agent as agt

class SMA: 
    def __init__(self, nbAgents, file, xGoal, yGoal, canvas):
        self.canvas = canvas
        
        self.env = env.Environment(file, canvas)
        self.env.draw()
        
        ## Réseau d'agent ##
        #self.a1 = agt.Agent(89, 100, xGoal, yGoal, self.env.xShape(),  self.env.yShape(), '#FF4E15', canvas) #OK
        #self.a1 = agt.Agent(130, 260, xGoal, yGoal, self.env.xShape(),  self.env.yShape(), '#FF4E15', canvas) #Rouge
        #self.a2 = agt.Agent(133, 260, xGoal, yGoal, self.env.xShape(),  self.env.yShape(), '#43FF15', canvas) #Vert
        #self.a3 = agt.Agent(132, 263, xGoal, yGoal, self.env.xShape(),  self.env.yShape(), '#15B8FF', canvas) #Bleu
        #self.a4 = agt.Agent(133, 263, xGoal, yGoal, self.env.xShape(),  self.env.yShape(), '#C06BFF', canvas) #Violet
        #self.a1 = agt.Agent(130, 260, xGoal, yGoal, self.env.xShape(),  self.env.yShape(), '#FF4E15', canvas) #Rouge
        #self.a2 = agt.Agent(225, 460, xGoal, yGoal, self.env.xShape(),  self.env.yShape(), '#43FF15', canvas) #Vert
        #self.a3 = agt.Agent(180, 385, xGoal, yGoal, self.env.xShape(),  self.env.yShape(), '#15B8FF', canvas) #Bleu
        #self.a4 = agt.Agent(325, 335, xGoal, yGoal, self.env.xShape(),  self.env.yShape(), '#C06BFF', canvas) #Violet
        self.a1 = agt.Agent(130, 260, xGoal, yGoal, self.env.xShape(),  self.env.yShape(), '#FF4E15', canvas) #OK
        self.a2 = agt.Agent(133, 260, xGoal, yGoal, self.env.xShape(),  self.env.yShape(), '#43FF15', canvas) #OK
        self.a3 = agt.Agent(130, 263, xGoal, yGoal, self.env.xShape(),  self.env.yShape(), '#15B8FF', canvas)
        self.a4 = agt.Agent(133, 263, xGoal, yGoal, self.env.xShape(),  self.env.yShape(), '#C06BFF', canvas)
        

        # Ensemble d'agents
        self.agents = [self.a1, self.a2, self.a3, self.a4]
        
        self.startTime = time() 
        
    def isGoals(self): 
        for a in self.agents:
            if not a.isGoal() : 
                return False
            
        return True
        
    def moveToGoal(self):
        if not self.isGoals() :
            for a in self.agents:
                a.moveToGoal(self.env)
            
            return False
        else : 
            for a in self.agents:
                print(a.getCout()) 
            # Afficher le rapport et fermer la fenetre
            
            print("Temps d'execution : " + str(time() - self.startTime))
            print("Fin") 

            self.canvas.update()
            self.canvas.postscript(file="save.ps", colormode='color')
            return True
        