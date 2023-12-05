import pygame as pg
import sys
from pathlib import Path
sys.path.append(Path(__file__).parents[1].joinpath("lib").as_posix())

from doompy.settings import config
from doompy.map import Map
from doompy.player import Player
from doompy.raycasting import RayCasting
from doompy.object_renderer import ObjectRenderer
from doompy.object_handler import ObjectHandler
from doompy.weapon import Weapon
from doompy.sound import Sound
from doompy.pathfinding import PathFinding


class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(config.RES)
        pg.event.set_grab(True)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.is_running = True
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        pg.mixer.music.play(-1)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(config.FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        # self.screen.fill('black')
        self.object_renderer.draw()
        self.weapon.draw()
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                print("todo")
                self.is_running = not self.is_running
                pg.draw.rect(self.screen, 'black', (0, 0, WIDTH/2, HEIGHT/2))
                self.sound.pause()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def run(self):
        while True:
            if(self.is_running == False):
                continue
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
