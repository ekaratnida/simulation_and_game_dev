
from .SceneBase import SceneBase
from .RegressionScene import RegressionScene
import pygame
import pygame_gui

class TitleScene(SceneBase):

    manager = None
    regression_btn = None
    classification_btn = None
    screen = None
    
    def __init__(self,manager,screen):
        SceneBase.__init__(self)
        self.manager = manager
        self.screen = screen 

        self.regression_btn = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((self.screen.get_width()/2, self.screen.get_height()/2), (100, 50)),
                text='Regression',
                manager=self.manager)
        
        self.classification_btn = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((self.screen.get_width()/2, self.screen.get_height()/4), (100, 50)),
                text='Classification',
                manager=self.manager)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.regression_btn:
                    print('Regression')
                    self.regression_btn.visible = False
                    self.SwitchToScene(RegressionScene(self.manager, self.screen))
                
                if event.ui_element == self.classification_btn:
                    print('Classification')
                    self.classification_btn.visible = False
                    self.SwitchToScene(RegressionScene(self.manager, self.screen))

            self.manager.process_events(event)
    
    def Update(self,time_delta):
        self.manager.update(time_delta)
        pass
    
    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((255, 255, 255))
        self.manager.draw_ui(screen)