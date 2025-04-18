import unittest
from app.core.setting import _get_config


class TestConfig(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_get_config(self):
        config = _get_config()
        host = config.get("app", "host")
        self.assertEqual(host, "0.0.0.0")
        timeout = config.getint("es", "timeout")
        self.assertEqual(timeout, 300)

if __name__ == "__main__":
    unittest.main()