import unittest

from .weapon import *

class TestBaseWeapon(unittest.TestCase):
    def test_str(self):
        s = str(BaseWeapon())

        self.assertEqual(s,
                         " damage=0, cool_down=0 seconds",
                         )


class TestHandgun(unittest.TestCase):
    def test_str(self):
        s = str(Handgun())

        self.assertEqual(s,
                         "Handgun damage=20, cool_down=1 second",
                         )


class TestKnife(unittest.TestCase):
    def test_str(self):
        s = str(Knife())

        self.assertEqual(s,
                         "Knife damage=10, cool_down=2 seconds",
                         )


class TestMachinePistol(unittest.TestCase):
    def test_str(self):
        s = str(MachinePistol())

        self.assertEqual(s,
                         "MachinePistol damage=15, cool_down=0.2 seconds",
                         )


class TestCricketBat(unittest.TestCase):
    def test_str(self):
        s = str(CricketBat())

        self.assertEqual(s,
                         "CricketBat damage=10, cool_down=1 second",
                         )


class TestFists(unittest.TestCase):
    def test_str(self):
        s = str(Fists())

        self.assertEqual(s,
                         "Fists damage=3.3333, cool_down=1 second",
                         )
