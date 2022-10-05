#from mypackage.TitleScene import TitleScene

from .SceneBase import SceneBase
#from .TitleScene import TitleScene
import pygame
import numpy as np

class RegressionScene(SceneBase):

    manager = None
    screen = None

    x = None
    y = None
    z = None

    #GD
    alpha = None
    converged = False
    iter = 0
    m = None
    t0 = 0
    t1 = 0
    ep = 0.00000001
    J = None

    lineColor = 0, 0, 255
    pointColor = 255, 0, 0
    width = None
    clickPos = None

    def cost_function(self, theta0, theta1, x, y, m):
        c = sum([(theta0 + theta1*x[i] - y[i])**2 for i in range(m)])
        return c

    def __init__(self,manager,screen):
        SceneBase.__init__(self)
        self.manager = manager
        self.screen = screen
        self.width = self.screen.get_width()

        self.x = np.array([[0, 1, 2, 3, 4, 5]]).T
        self.y = np.array([1, 1, 1.2, 2.5, 4, 6])
        self.z = zip(self.x,self.y)

        #GD
        self.alpha = 0.001 # learning rate
        self.converged = False
        self.iter = 0
        self.m = self.x.shape[0] # number of samples
        # initial theta
        self.t0 = 0 #np.random.random(x.shape[1])
        self.t1 = 0 #np.random.random(x.shape[1])
        
        self.ep = 0.00000001
        self.J = self.cost_function(self.t0, self.t1, self.x, self.y, self.m)
        self.clickPos = []
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                from mypackage.TitleScene import TitleScene
                self.SwitchToScene(TitleScene(self.manager,self.screen))
                pass 
            
    def Update(self,time_delta):
        self.manager.update(time_delta)
        #print("update")

        if not self.converged:

            grad0 = sum([(self.t0 + self.t1*self.x[i] - self.y[i]) for i in range(self.m)]) 
            grad1 = sum([(self.t0 + self.t1*self.x[i] - self.y[i]) * self.x[i] for i in range(self.m)])

            # update the theta_temp
            temp0 = self.t0 - self.alpha * grad0
            temp1 = self.t1 - self.alpha * grad1
            # update theta
            self.t0 = temp0
            self.t1 = temp1

            # error
            e = self.cost_function(self.t0, self.t1, self.x, self.y, self.m)
        
            diffE = abs(self.J-e)
            #print("diffE = ",diffE)
            
            if diffE <= self.ep:
                print("Converged")
                converged = True

            J = e   # update error s

        else:

            print("Converged")
        
        
        #for p in self.clickPos:
        #    pygame.draw.circle(self.screen, self.pointColor, p, 4, 0)
    
    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((255, 255, 255))
        self.manager.draw_ui(screen)

        for i,j in zip(self.x.flatten(),self.y):
            #print(i," ",j)
            pygame.draw.circle(self.screen, self.pointColor, (i*100, self.width - (j*100)), 4, 0)
        
        startPos = (0,self.width-(self.t0[0]*100))
        #print('sp' , startPos)
        endPos = (self.width, self.width - ((self.t0[0]*100) + (self.t1[0]* self.width)))
        #print('ep' , endPos)
        pygame.draw.line(self.screen, self.lineColor, startPos, endPos, 2)
        #pygame.draw.line(screen, self.lineColor)
    