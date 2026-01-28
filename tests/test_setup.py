# pylint: disable-all

import os
import importlib.util
import unittest


def is_package_installed(package_name):
    spec = importlib.util.find_spec(package_name)
    return spec is not None


class TestSumOfThree(unittest.TestCase):
    def test_running_in_virtual_env(self):
        self.assertIn(
            "reinforcement",
            os.environ["VIRTUAL_ENV"].lower(),
            msg="It seems you're not running in the correct virtual environment.",
        )

    def test_the_packages(self):
        self.assertTrue(is_package_installed('gymnasium'))
        self.assertTrue(is_package_installed("stable_baselines3"))
        self.assertTrue(is_package_installed("tensorboard"))
