import unittest

from main import simulate_attack, create_player


class TestMain(unittest.TestCase):
    def test_simulate_attack(self):
        attacker = create_player()
        attacker.equip_weapon(0)

        victim = create_player()

        simulate_attack(attacker, victim)

        self.assertEqual(victim.alive, True)
        self.assertEqual(victim.health, 96.6667)

    def test_simulate_attack_by_dead_player(self):
        attacker = create_player()
        attacker.equip_weapon(0)
        attacker.die()

        victim = create_player()

        self.assertEqual(attacker.alive, False)
        simulate_attack(attacker, victim)
        self.assertEqual(attacker.alive, True)

        self.assertEqual(victim.alive, True)
        self.assertEqual(victim.health, 100)

    def test_simulate_attack_on_dead_player(self):
        attacker = create_player()
        attacker.equip_weapon(0)

        victim = create_player()
        victim.die()

        simulate_attack(attacker, victim)

        self.assertEqual(victim.alive, False)
        self.assertEqual(victim.health, 0)
