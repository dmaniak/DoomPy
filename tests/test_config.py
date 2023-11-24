import unittest
from pathlib import Path
import sys

sys.path.append(Path(__file__).parents[1].joinpath("lib").as_posix())


from doompy.settings import Config


class TestConfig(unittest.TestCase):
    
    def test_singleton(self):

        inst1 = Config()

        inst2 = Config()

        self.assertEqual(inst1, inst2)

    def test_config_values(self):
        inst1 = Config()

        self.assertEqual(inst1.MOUSE_BORDER_LEFT, 100)
        self.assertEqual(inst1.TEXTURE_SIZE, 256)
        self.assertEqual(inst1.HALF_TEXTURE_SIZE, 128)

    def test_read_resources(self):
        inst1 = Config()
        texture = inst1.resource_root.joinpath("textures/1.png")
        self.assertTrue(texture.exists())

        self.assertTrue(texture.is_file())


if __name__ == "__main__":
    unittest.main(verbosity=2)
