# The first half is just boiler-plate stuff...

import pygame
import pygame_gui

class SceneBase:
    def __init__(self):
        self.next = self
    
    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)

def run_game(width, height, fps):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    
    manager = pygame_gui.UIManager((width, height))
    clock = pygame.time.Clock()
    active_scene = TitleScene(manager,screen)

    while active_scene != None:
        time_delta = clock.tick(60)/1000.0
        pressed_keys = pygame.key.get_pressed()
        
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            
            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
        
        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update(time_delta)
        active_scene.Render(screen)
        
        active_scene = active_scene.next
        
        pygame.display.flip()
        clock.tick(fps)

# The rest is code where you implement your game using the Scenes model

class TitleScene(SceneBase):

    manager = None
    hello_button = None
    screen = None
    
    def __init__(self,manager,screen):
        SceneBase.__init__(self)
        self.manager = manager
        self.screen = screen 

        self.hello_button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((self.screen.get_width()/2, self.screen.get_height()/2), (100, 50)),
                text='Say Hello',
                manager=self.manager)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.hello_button:
                    print('Hello World!')
                    self.hello_button.visible = False
                    self.SwitchToScene(GameScene(self.manager, self.screen))

            self.manager.process_events(event)
    
    def Update(self,time_delta):
        self.manager.update(time_delta)
        pass
    
    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((255, 0, 0))
        self.manager.draw_ui(screen)

class GameScene(SceneBase):

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
                self.SwitchToScene(TitleScene(self.manager,self.screen))
        
    def Update(self,time_delta):
        self.manager.update(time_delta)
        pass
    
    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((0, 0, 255))
        self.manager.draw_ui(screen)

run_game(400, 300, 60)