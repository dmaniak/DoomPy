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


if __name__ == "__main__":
    unittest.main(verbosity=2)
