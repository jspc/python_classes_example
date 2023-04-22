import unittest

from .player import Player, NPC, npcWeapon
from .weapon import MachinePistol


class TestPlayer(unittest.TestCase):
    def test_init(self):
        p = Player("Tess Tests", 250, [npcWeapon])
        str(p)

        for assertion in [
            (p.health, 250),
            (p.name, "Tess Tests"),
            (p.equipped_weapon.name, "Fists"),
            (p.kills, 0),
            (p.deaths, 0),
            (p.alive, True),
        ]:
            self.assertEqual(assertion[0], assertion[1])

    def test_add_weapon(self):
        p = Player("Tess Tests", 250, [npcWeapon])
        self.assertEqual(len(p.weapons), 1)

        p.add_weapon(MachinePistol())
        self.assertEqual(len(p.weapons), 2)
        self.assertEqual(p.weapons[1].name, "MachinePistol")

    def test_equip_weapon(self):
        p = Player("Tess Tests", 250, [npcWeapon])
        self.assertEqual(p.equipped_weapon.name, "Fists")

        p.add_weapon(MachinePistol())
        p.equip_weapon(1)
        self.assertEqual(p.equipped_weapon.name, "MachinePistol")

    def test_equip_weapon_out_of_range(self):
        p = Player("Tess Tests", 250, [npcWeapon])
        self.assertEqual(p.equipped_weapon.name, "Fists")

        # Try to set weapon to a massively out of range weapon
        p.equip_weapon(1_000_000)
        self.assertEqual(p.equipped_weapon.name, "Fists")

    def test_equip_weapon_negative_index(self):
        p = Player("Tess Tests", 250, [npcWeapon])
        self.assertEqual(p.equipped_weapon.name, "Fists")

        # Try to set weapon to a massively out of range weapon
        p.equip_weapon(-10)
        self.assertEqual(p.equipped_weapon.name, "Fists")

    def test_die(self):
        p = Player("Tess Tests", 250, [npcWeapon])
        self.assertEqual(p.alive, True)
        self.assertEqual(p.deaths, 0)

        p.die()
        self.assertEqual(p.alive, False)
        self.assertEqual(p.deaths, 1)

    def test_resurrect(self):
        p = Player("Tess Tests", 250, [npcWeapon])
        self.assertEqual(p.alive, True)
        self.assertEqual(p.deaths, 0)

        p.die()
        self.assertEqual(p.alive, False)
        self.assertEqual(p.deaths, 1)

        p.resurrect()
        self.assertEqual(p.alive, True)

    def test_attack(self):
        attacker = Player("Tess Tests", 250, [npcWeapon])
        victim = Player("Valentino Victimo", 250, [npcWeapon])

        self.assertEqual(victim.alive, True)
        self.assertEqual(victim.health, 250)

        attacker.attack(victim)
        self.assertEqual(victim.alive, True)
        self.assertEqual(victim.health, 246.6667)

    def test_attack_and_kill(self):
        attacker = Player("Tess Tests", 250, [npcWeapon])
        victim = Player("Valentino Victimo", 1, [npcWeapon])

        self.assertEqual(victim.alive, True)
        self.assertEqual(victim.health, 1)
        self.assertEqual(victim.deaths, 0)

        attacker.attack(victim)
        self.assertEqual(victim.alive, False)
        self.assertEqual(victim.health, 0)
        self.assertEqual(victim.deaths, 1)


class TestNPC(unittest.TestCase):
    def test_init(self):
        p = NPC()

        for assertion in [
            (p.health, 20),
            (p.name, "NPC"),
            (p.equipped_weapon.name, "Fists"),
            (p.kills, 0),
            (p.deaths, 0),
            (p.alive, True),
        ]:
            self.assertEqual(assertion[0], assertion[1])
