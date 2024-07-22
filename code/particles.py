import pygame
from pygame.sprite import _Group
from support import import_folder

class AnimationPlayer:
    def __init__(self):
        self.frames = {
            
        }

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self,groups,animation_frames,pos):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.image.get_rect[self.frame_index]

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame >= len(self.frames):
            self.kill()
        else :
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()