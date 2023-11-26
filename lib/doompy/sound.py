import pygame as pg
from doompy.settings import config


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = config.resource_root.joinpath('sound')
        self.shotgun = pg.mixer.Sound(self.path.joinpath('shotgun.wav'))
        self.shotgun.set_volume(config.VOLUME)
        self.npc_pain = pg.mixer.Sound(self.path.joinpath('npc_pain.wav'))
        self.npc_pain.set_volume(config.VOLUME)
        self.npc_death = pg.mixer.Sound(self.path.joinpath('npc_death.wav'))
        self.npc_death.set_volume(config.VOLUME)
        self.npc_shot = pg.mixer.Sound(self.path.joinpath('npc_attack.wav'))
        self.npc_shot.set_volume(config.VOLUME)
        self.player_pain = pg.mixer.Sound(self.path.joinpath('player_pain.wav'))
        self.player_pain.set_volume(config.VOLUME)
        self.theme = pg.mixer.music.load(self.path.joinpath('theme.mp3'))
        pg.mixer.music.set_volume(config.MUSIC_VOLUME)
