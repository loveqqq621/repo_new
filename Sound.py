import pygame as pg
import os
file_path = os.path.abspath(__file__)
file_path = os.path.dirname(file_path)
file_path = os.path.join(file_path, 'materials/')



class Sound(object):
    def __init__(self):
        self.sounds = {}
        self.load_sounds()

    def load_sounds(self):
        # pg.mixer.pre_init(44100, -16, 2, 1024)
        self.sounds['overworld'] = pg.mixer.Sound(os.path.join(file_path, 'sounds/overworld.wav'))
        self.sounds['overworld_fast'] = pg.mixer.Sound(os.path.join(file_path, 'sounds/overworld-fast.wav'))
        self.sounds['level_end'] = pg.mixer.Sound(os.path.join(file_path, 'sounds/levelend.wav'))
        self.sounds['coin'] = pg.mixer.Sound(os.path.join(file_path, 'sounds/coin.wav'))
        self.sounds['small_mario_jump'] = pg.mixer.Sound(os.path.join(file_path, 'sounds/jump.wav'))
        self.sounds['big_mario_jump'] = pg.mixer.Sound(os.path.join(file_path, 'sounds/jumpbig.wav'))
        self.sounds['brick_break'] = pg.mixer.Sound(os.path.join(file_path, 'sounds/blockbreak.wav'))
        self.sounds['block_hit'] = pg.mixer.Sound(os.path.join(file_path, 'sounds/blockhit.wav'))
        self.sounds['mushroom_appear'] = pg.mixer.Sound(os.path.join(file_path, 'sounds/mushroomappear.wav'))
        self.sounds['mushroom_eat'] = pg.mixer.Sound(os.path.join(file_path, 'sounds/mushroomeat.wav'))
        self.sounds['death'] = pg.mixer.Sound(os.path.join(file_path, 'sounds/death.wav'))
        self.sounds['pipe'] = pg.mixer.Sound(os.path.join(file_path, 'sounds/pipe.wav'))
        self.sounds['kill_mob'] = pg.mixer.Sound(os.path.join(file_path, 'sounds/kill_mob.wav'))
        self.sounds['game_over'] = pg.mixer.Sound(os.path.join(file_path, 'sounds/gameover.wav'))
        self.sounds['scorering'] = pg.mixer.Sound(os.path.join(file_path, 'sounds/scorering.wav'))
        self.sounds['fireball'] = pg.mixer.Sound(os.path.join(file_path, 'sounds/fireball.wav'))
        self.sounds['shot'] = pg.mixer.Sound(os.path.join(file_path, 'sounds/shot.wav'))
        # self.sounds['bgm'] = pg.mixer.Sound(os.path.join(file_path, 'sounds/bgm.MP3'))

        # self.sounds['bgm'] = pg.mixer.music.load(os.path.join(file_path, 'sounds/bgm.MP3'))


    def play(self, name, loops, volume):
        self.sounds[name].play(loops=loops)
        self.sounds[name].set_volume(volume)

    def stop(self, name):
        self.sounds[name].stop()

    def start_fast_music(self, core):
        if core.get_map().get_name() == '1-1':
            self.stop('overworld')
            self.play('overworld_fast', 99999, 0.5)