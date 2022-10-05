import numpy as np
import pygame

def cost_function(theta0, theta1, x, y, m):
    c = sum([(theta0 + theta1*x[i] - y[i])**2 for i in range(m)])
    return c

y = 0
dir = 1
running = 1
clickPos = []
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
lineColor = 0, 0, 255
pointColor = 255, 0, 0
bgcolor = 255, 255, 255

#x = np.array([[random.randint(100,width-100) for r in range(5) ]]).T
#y = np.array([random.randint(100,height-100) for r in range(5) ])
x = np.array([[0, 1, 2, 3, 4, 5]]).T # or x = np.array([[0],[2],[3]])
y = np.array([1, 1, 1.2, 2.5, 4, 6])
z = zip(x,y)
#print(x," ",y)

#GD
alpha = 0.001 # learning rate
converged = False
iter = 0
m = x.shape[0] # number of samples
# initial theta
t0 = 0 #np.random.random(x.shape[1])
t1 = 0 #np.random.random(x.shape[1])
J = cost_function(t0,t1,x,y,m)
print("Init cost = ",J)
ep = 0.00000001

while running:

    event = pygame.event.poll()
    
    if event.type == pygame.QUIT:
        running = 0

    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        print(pos)
        clickPos.append(pos)
    
    screen.fill(bgcolor)

    if not converged:

        grad0 = sum([(t0 + t1*x[i] - y[i]) for i in range(m)]) 
        grad1 = sum([(t0 + t1*x[i] - y[i])*x[i] for i in range(m)])

        # update the theta_temp
        temp0 = t0 - alpha * grad0
        temp1 = t1 - alpha * grad1
        # update theta
        t0 = temp0
        t1 = temp1

        # error
        e = cost_function(t0,t1,x,y,m)
    
        diffE = abs(J-e)
        #print("diffE = ",diffE)
        
        if diffE <= ep:
            print("Converged")
            converged = True

        J = e   # update error s

    else:
        print("Converged")

    for i,j in zip(x.flatten(),y):
        #print(i," ",j)
        pygame.draw.circle(screen, pointColor, (i*100, width - (j*100)), 4, 0)
    
    startPos = (0,width-(t0[0]*100))
    endPos = (width,width - ((t0[0]*100) + (t1[0]*width)))
    pygame.draw.line(screen, lineColor, startPos, endPos, 2)
    for p in clickPos:
        pygame.draw.circle(screen, pointColor, p, 4, 0)


    #y += dir
    #if y == 0 or y == height-1: dir *= -1

    pygame.display.flip()
    pygame.time.delay(100)