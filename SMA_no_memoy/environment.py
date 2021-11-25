import numpy as np
from matplotlib import image

class Environment: 
    def __init__(self, file, canvas):
        self.img = image.imread(file)
        
        rgb_weights = [0.2989, 0.5870, 0.1140]

        self.env = np.dot(self.img[...,:3], rgb_weights)

        for i in range(0, self.env.shape[0]): 
            for j in range(0,self.env.shape[1]):
                if self.env[i, j] < 0.5:
                    self.env[i, j] = 1
                else :
                    self.env[i, j] = 0
        
        self.canvas = canvas
        self.canvas.config(width=self.env.shape[0]*2, height=self.env.shape[1])
        
        #print(self.env.shape) (435, 600)
        

    def draw(self):
        for i in range(0, self.env.shape[0]): 
            for j in range(0, self.env.shape[1]):
                if self.env[i, j] == 1:
                    self.canvas.create_rectangle(i-0.5, j-0.5, i+0.5 , j+0.5, fill='black', outline='black')
                    
    def xShape(self):
        return self.env.shape[0]
    
    def yShape(self):
        return self.env.shape[1]
        
    def free(self, x, y):
        return self.env[x][y] == 0