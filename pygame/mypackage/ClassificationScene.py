from .SceneBase import SceneBase
import pygame
import pygame_gui

class ClassificationScene(SceneBase):

    manager = None
    screen = None
    
    def __init__(self,manager,screen):
        SceneBase.__init__(self)
        self.manager = manager
        self.screen = screen
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                # self.SwitchToScene(RegressionScene(self.manager,self.screen))
                pass 
            
    def Update(self,time_delta):
        self.manager.update(time_delta)
        pass
    
    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((0, 0, 255))
        self.manager.draw_ui(screen)
