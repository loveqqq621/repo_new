import pygame as pg
import os
file_path = os.path.abspath(__file__)
file_path = os.path.dirname(file_path)
file_path = os.path.join(file_path, 'materials/')


class Flag(object):
    def __init__(self, x_pos, y_pos):
        self.rect = None

        self.flag_offset = 0
        self.flag_omitted = False

        # Flag object consists of 2 parts:

        self.pillar_image = pg.image.load(os.path.join(file_path, 'images/flag_pillar0.png')).convert_alpha()
        self.pillar_rect = pg.Rect(x_pos + 8, y_pos, 16, 368)

        # self.flag_image = pg.image.load('images/flag2.png').convert_alpha()
        # self.flag_rect = pg.Rect(x_pos - 50, y_pos + 16, 64, 64)

        # 尝试婚纱图片的大小
        self.flag_image = pg.image.load(os.path.join(file_path, 'images/dress_high_pixel.png')).convert_alpha()
        self.flag_rect = pg.Rect(x_pos - 58, y_pos - 45, 138, 156)


    def move_flag_down(self):
        self.flag_offset += 3
        self.flag_rect.y += 3

        if self.flag_offset >= 255:
            self.flag_omitted = True

    def render(self, core):
        self.rect = self.pillar_rect
        core.screen.blit(self.pillar_image, core.get_map().get_camera().apply(self))

        self.rect = self.flag_rect
        core.screen.blit(self.flag_image, core.get_map().get_camera().apply(self))