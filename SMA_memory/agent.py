import math as mt
import position as ps
import numpy as np
import random 

class Agent: 
    
    def __init__(self, x, y, xGoal, yGoal, xMemory, yMemory, color, canvas):
        # Position courante de l'agent 
        self.x = x
        self.y = y
        
        self.color = color
        
        self.cout = 0 
        
        # Posoition but de l'agent 
        self.xGoal = xGoal
        self.yGoal = yGoal
        
        # Initialisation de la mémmoire
        self.xMemory = xMemory
        self.yMemory = yMemory
        # Les positions non-exploré valent 0, deje exploré 1 et interdite 2
        self.memory = np.zeros((self.xMemory, self.yMemory))
        
        # Constante d'affichage
        self.aRadius = 2#0.5
        self.sRadius = 4

        self.canvas = canvas
        self.goalDraw =  self.canvas.create_oval(self.xGoal - self.sRadius, self.yGoal - self.sRadius , self.xGoal + self.sRadius, self.yGoal + self.sRadius, outline='green')
        self.agentDraw = self.canvas.create_oval(self.x - self.aRadius, self.y - self.aRadius , self.x + self.aRadius, self.y + self.aRadius, fill=color, outline=color)


    def up(self):
        self.eraseAgent()
        self.y = self.y - 1
        self.drawAgent()

    def down(self): 
        self.eraseAgent()
        self.y = self.y + 1
        self.drawAgent()

    def left(self): 
        self.eraseAgent()
        self.x = self.x - 1
        self.drawAgent()

    def right(self): 
        self.eraseAgent()
        self.x = self.x + 1
        self.drawAgent()
        
        
    def upANDright(self):
        self.eraseAgent()
        #up
        self.y = self.y - 1
        #right
        self.x = self.x + 1
        self.drawAgent()

    def rightANDdown(self): 
        self.eraseAgent()
        #right
        self.x = self.x + 1
        #down
        self.y = self.y + 1
        self.drawAgent()

    def downANDleft(self): 
        self.eraseAgent()
        #down
        self.y = self.y + 1
        #left
        self.x = self.x - 1
        self.drawAgent()

    def leftANDup(self): 
        self.eraseAgent()
        #left
        self.x = self.x - 1
        #up
        self.y = self.y - 1
        self.drawAgent()
        
    def positionNonExplore(self, x, y): 
        return self.memory[x, y] == 0
    
    def positionExplore(self, x, y): 
        return self.memory[x, y] == 1
    
    def memoriserPosition(self): 
        self.memory[self.x][self.y] = 1
        self.canvas.create_oval(self.x + self.xMemory - 0.5, self.y - 0.5 , self.x+ self.xMemory + 0.5, self.y + 0.5, fill=self.color, outline=self.color)
        
    def supprimerPosition(self, x, y): 
        self.memory[x][y] = 2
        
    def getCout(self):
        return self.cout
    
    def isGoal(self):
        return self.x == self.xGoal and self.y == self.yGoal
    
    def rightTo(self, pos): 
        if pos == "up":
            return "upANDright"
        elif pos == "upANDright":
            return "right"
        elif pos == "right": 
            return "rightANDdown"
        elif pos == "rightANDdown": 
            return "down"
        elif pos == "down":
            return "downANDleft"
        elif pos == "downANDleft":
            return "left"
        elif pos == "left": 
            return "leftANDup"
        elif pos == "leftANDup": 
            return "up"

    def moveToGoal(self, env):
        if not(self.x == self.xGoal and self.y == self.yGoal):
            #Memoriser une position 
            # if env.free(self.x, self.y): 
            #     env.memoriserPosition(self.x, self.y)
            #     self.canvas.create_oval(self.x + self.xMemory - 0.5, self.y - 0.5 , self.x+ self.xMemory + 0.5, self.y + 0.5, fill=self.color, outline=self.color)
                
            
            # Dict de toutes le positions possibles 
            positions = {"up": ps.position(self.x, self.y-1, mt.sqrt((self.xGoal - self.x)**2 + (self.yGoal - self.y-1)**2)),
                         "upANDright": ps.position(self.x+1, self.y-1, mt.sqrt((self.xGoal - self.x+1)**2 + (self.yGoal - self.y-1)**2)),
                         "right": ps.position(self.x+1, self.y, mt.sqrt((self.xGoal - self.x+1)**2 + (self.yGoal - self.y)**2)),
                         "rightANDdown": ps.position(self.x+1, self.y+1, mt.sqrt((self.xGoal - self.x+1)**2 + (self.yGoal - self.y+1)**2)),
                         "down": ps.position(self.x, self.y+1, mt.sqrt((self.xGoal - self.x)**2 + (self.yGoal - self.y+1)**2)), 
                         "downANDleft": ps.position(self.x-1, self.y+1, mt.sqrt((self.xGoal - self.x-1)**2 + (self.yGoal - self.y+1)**2)),
                         "left": ps.position(self.x-1, self.y, mt.sqrt((self.xGoal - self.x-1)**2 + (self.yGoal - self.y)**2)),
                         "leftANDup": ps.position(self.x-1, self.y-1, mt.sqrt((self.xGoal - self.x-1)**2 + (self.yGoal - self.y-1)**2))}
            
            # Dict des positions Impossible
            positionsImpossible = {}
            
            positionsPossible = {}
            
            # Dcit des positions non-explore
            positionsNonExplore = {}
            
            # BUG
            # for p in positions : 
            #     if env.free(positions[p].getX(), positions[p].getY()) and self.positionNonExplore(positions[p].getX(), positions[p].getY()):
            #         positionsNonExplore[p] = ps.position(positions[p].getX(), positions[p].getY(), positions[p].getH())
            #     else : 
            #         positionsImpossible[p] = ps.position(positions[p].getX(), positions[p].getY(), positions[p].getH())
            
            # On ajout les positions libres dict des positions libre (positionsPossible)
            for p in positions : 
                if env.free(positions[p].getX(), positions[p].getY()):
                    positionsPossible[p] = ps.position(positions[p].getX(), positions[p].getY(), positions[p].getH())
                else : 
                    positionsImpossible[p] = ps.position(positions[p].getX(), positions[p].getY(), positions[p].getH())
                    
            # On ajout les positions pas encore exploré
            for p in positionsPossible : 
                if env.positionNonExplore(positions[p].getX(), positions[p].getY()): 
                    positionsNonExplore[p] = ps.position(positions[p].getX(), positions[p].getY(), positions[p].getH())
                    
            #Dessiner les murs sur l'espace mémoire        
            for p in positionsImpossible: 
                self.canvas.create_oval(positions[p].getX() + self.xMemory - 0.5, positions[p].getY() - 0.5 , positions[p].getX() + self.xMemory + 0.5, positions[p].getY() + 0.5, fill='black', outline='black' )
            
            
            # On recher la meilleure option parmis le positions libres
            action = ""
            h = 0
            
            if bool(positionsNonExplore): 
            # Meilleure heuristique des positions non-explore
                for p in positionsNonExplore: 
                    if positionsNonExplore[p].getH() > h: 
                        h = positionsNonExplore[p].getH()
                        action = p
            else : 
                if bool(positionsImpossible): 
                    action = self.rightTo(list(positionsImpossible.keys())[-1]) 
                    
                    while action in positionsImpossible:
                        action = self.rightTo(action)
                else : 
                    action = str(random.choice(list(positionsPossible.keys())))
                    print("randChoice")
                
                
            #Memoriser une position 
            
            # On execut l'actions qui a été selectionné
            if action == "up":
                self.up()
            elif action == "right":
                self.right()
            elif action == "down": 
                self.down()
            elif action == "left": 
                self.left()
            elif action == "upANDright":
                self.upANDright()
            elif action == "rightANDdown":
                self.rightANDdown()
            elif action == "downANDleft": 
                self.downANDleft()
            elif action == "leftANDup": 
                self.leftANDup()
                
            if env.free(self.x, self.y) and not self.isGoal(): 
                env.memoriserPosition(self.x, self.y)
                self.canvas.create_oval(self.x + self.xMemory - 0.5, self.y - 0.5 , self.x+ self.xMemory + 0.5, self.y + 0.5, fill=self.color, outline=self.color)

            self.cout += 1
            
            return False

        else: 
            return True

    def drawAgent(self):
        self.agentDraw = self.canvas.create_oval(self.x - self.aRadius, self.y - self.aRadius , self.x + self.aRadius, self.y + self.aRadius, fill=self.color, outline=self.color )

    def eraseAgent(self): 
        self.canvas.delete(self.agentDraw)