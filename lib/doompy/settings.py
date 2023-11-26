import math
from pathlib import  Path
from typing import  Union, List
import  json


class Config:

    inited = False

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls)
            cls.__version__ = "0.1"
            config_path = Path(__file__).parents[2].resolve().joinpath("etc/config.json")
            cls.load_config(config_path)
        return cls.instance

    @classmethod
    def load_config(cls, config_file_path: Union[str, Path]):

        config_file_path = Path(config_file_path) if isinstance(config_file_path, str) else config_file_path
        with config_file_path.open("r") as fp:
            config = json.load(fp)

        # game settings
        # RES = WIDTH, HEIGHT = 1600, 900
        cls.RES: List[int]
        cls.FPS: int
        cls.PLAYER_POS: List[float]
        cls.PLAYER_ANGLE: float
        cls.PLAYER_SPEED: float
        cls.PLAYER_ROT_SPEED: float
        cls.PLAYER_SIZE_SCALE: float
        cls.PLAYER_MAX_HEALTH: int


        cls.MOUSE_SENSITIVITY: float
        cls.MOUSE_MAX_REL: float
        cls.MOUSE_BORDER_LEFT: int
        cls.FLOOR_COLOR: List[int]
        cls.MAX_DEPTH: float
        cls.TEXTURE_SIZE: int
        cls.VOLUME: float
        cls.MUSIC_VOLUME: float

        for k, v in config.items():
            setattr(cls, k, v)

        cls.WIDTH, cls.HEIGHT = cls.RES
        cls.HALF_WIDTH = cls.WIDTH // 2
        cls.HALF_HEIGHT = cls.HEIGHT // 2
     
        cls.MOUSE_BORDER_RIGHT = cls.WIDTH - cls.MOUSE_BORDER_LEFT

        cls.FOV = math.pi / 3
        cls.HALF_FOV = cls.FOV / 2
        cls.NUM_RAYS = cls.WIDTH // 2
        cls.HALF_NUM_RAYS = cls.NUM_RAYS // 2
        cls.DELTA_ANGLE = cls.FOV / cls.NUM_RAYS

        cls.SCREEN_DIST = cls.HALF_WIDTH / math.tan(cls.HALF_FOV)
        cls.SCALE = cls.WIDTH // cls.NUM_RAYS

        cls.HALF_TEXTURE_SIZE = cls.TEXTURE_SIZE // 2

        cls.resource_root = Path(__file__).parents[2].resolve().joinpath("resources")


config = Config()
