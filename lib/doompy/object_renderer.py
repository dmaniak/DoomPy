import pygame as pg
from doompy.settings import config


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture(config.resource_root.joinpath('textures/sky.png'), (config.WIDTH, config.HALF_HEIGHT))
        self.sky_offset = 0
        self.blood_screen = self.get_texture(config.resource_root.joinpath('textures/blood_screen.png'), config.RES)
        self.digit_size = 90
        self.digit_images = [self.get_texture(config.resource_root.joinpath(f'textures/digits/{i}.png'), [self.digit_size] * 2)
                             for i in range(11)]
        self.digits = dict(zip(map(str, range(11)), self.digit_images))
        self.game_over_image = self.get_texture(config.resource_root.joinpath('textures/game_over.png'), config.RES)
        self.win_image = self.get_texture(config.resource_root.joinpath('textures/win.png'), config.RES)

    def draw(self):
        self.draw_background()
        self.render_game_objects()
        self.draw_player_health()

    def win(self):
        self.screen.blit(self.win_image, (0, 0))

    def game_over(self):
        self.screen.blit(self.game_over_image, (0, 0))

    def draw_player_health(self):
        health = str(self.game.player.health)
        for i, char in enumerate(health):
            self.screen.blit(self.digits[char], (i * self.digit_size, 0))
        self.screen.blit(self.digits['10'], ((i + 1) * self.digit_size, 0))

    def player_damage(self):
        self.screen.blit(self.blood_screen, (0, 0))

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % config.WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + config.WIDTH, 0))
        # floor
        pg.draw.rect(self.screen, config.FLOOR_COLOR, (0, config.HALF_HEIGHT, config.WIDTH, config.HEIGHT))

    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(config.TEXTURE_SIZE, config.TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            2: self.get_texture(config.resource_root.joinpath('textures/2.png')),
            3: self.get_texture(config.resource_root.joinpath('textures/3.png')),
            1: self.get_texture(config.resource_root.joinpath('textures/1.png')),
            4: self.get_texture(config.resource_root.joinpath('textures/4.png')),
            5: self.get_texture(config.resource_root.joinpath('textures/5.png')),
        }
