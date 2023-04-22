from .weapon import Fists

npcWeapon = Fists()


class Player:
    """
    Player represents a person; whether a real one or an NPC and allows
    contains the various bits of logic necessary for player operations, such
    as attacking other players, or K/D ratios
    """

    health = 20
    alive = True
    npc = False
    kills = 0
    deaths = 0

    def __init__(self, name, health, weapons):
        """
        Create a new player

        Args:
            name (string): The name of this player
            health (int): How many health points this player starts with
            weapons([Weapon]): A list of weapons this player has

        Returns:
            A new player
        """
        self.name = name
        self.health = health

        self.weapons = weapons
        if len(self.weapons) > 0:
            self.equipped_weapon = self.weapons[0]

    def add_weapon(self, weapon):
        """
        Add a weapon to this player's load out

        Args:
            weapon (Weapon): A weapon to add to loadout
        """
        self.weapons.append(weapon)

    def equip_weapon(self, idx):
        """
        Equip a weapon from a load out, but index. If requested
        weapon does not exist in the layout then do nothing

        Args:
            idx (int): the index of the weapon to load
        """
        if idx < 0 or idx >= len(self.weapons):
            return

        self.equipped_weapon = self.weapons[idx]

    def die(self):
        """
        Kill this player, including setting health to 0, and incrementing
        the deaths
        """
        self.health = 0
        self.alive = False
        self.deaths += 1

    def resurrect(self):
        """
        Bring this player back from the dead, setting health back to 100
        """
        self.alive = True
        self.health = 100

    def attack(self, victim):
        """
        Attack another player, optionally killing them if the victim's health
        drops to, or below, zero.

        Args:
            victim (Player): The player to attack with the equipped weapon
        """
        victim.health -= self.equipped_weapon.damage
        if victim.health <= 0:
            self.kills += 1
            victim.die()

    def __str__(self):
        elems = [
            self.name.ljust(30, " "),
            f"<{self.equipped_weapon}>".ljust(50, " "),
            f'health: {"%.2f" % self.health}'.ljust(15, " "),
            f'k/d: {self.kills}/{self.deaths} (={"%.2f" % (self.kills/self.deaths if self.deaths > 0 else self.kills)})',
        ]

        return "\t".join(elems)


class NPC(Player):
    """NPC represents a player with lower health, no name, and very little else"""

    name = "NPC"
    npc = True
    health = 20

    def __init__(self):
        """
        Create an NPC, and give it some fists as a weapon

        Returns:
            A new NPC
        """
        self.equipped_weapon = npcWeapon

    def resurrect(self):
        """Override resurrect for NPCs; when they die, they die"""
        pass
