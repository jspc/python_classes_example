#!/usr/bin/env python

from game.weapon import *
from game.player import NPC, Player

from faker import Faker
import random

players = []

weapons = [
    Fists(),
    Handgun(),
    Knife(),
    MachinePistol(),
    CricketBat(),
]

default_weapon = weapons[0]

fake = Faker()


def simulate_attack(attacker, victim):
    # A dead attacker can't attack anything, so resurrect
    # and continue, representing a missed turn
    if not attacker.alive:
        attacker.resurrect()
        return

    # There's no point attacking a dead player, so do nothing
    if not victim.alive:
        return

    attacker.attack(victim)


def create_player():
    player = Player(fake.name(), 100, [default_weapon])
    player.add_weapon(random.sample(weapons, 1)[0])
    player.equip_weapon(1)

    return player


if __name__ == "__main__":
    # Create a load of NPCS
    for _ in range(250):
        players.append(NPC())

    # Create a load of players and give them each a random weapon
    for _ in range(25):
        players.append(create_player())

    # Simulate a load of attacks
    for _ in range(100_000):
        attacker = random.sample(players, 1)[0]
        victim = random.sample(players, 1)[0]

        simulate_attack(attacker, victim)

    # Let's have a look at K/Ds for non NPCs
    for player in players:
        if player.npc:
            continue

        print(player)
