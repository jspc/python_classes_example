class BaseWeapon:
    '''
    BaseWeapon is the SuperClass for weaponry; containing common logic, such as
    reload logic, cool_downs, or whatever else a weapon might have in a game
    '''
    name = ""
    damage = 0
    cool_down = 0

    def __init__(self):
        pass

    def __str__(self):
        pluralised_suffix = 's' if self.cool_down != 1 else ''

        return f'{self.name} damage={self.damage}, cool_down={self.cool_down} second{pluralised_suffix}'


class Handgun(BaseWeapon):
    '''Handgun is a pew-pew pistol'''
    name = "Handgun"
    damage = 20
    cool_down = 1


class Knife(BaseWeapon):
    '''Stabby stabby'''
    name = "Knife"
    damage = 10
    cool_down = 2


class MachinePistol(BaseWeapon):
    '''Once they caught us off-guard, the MAC-10 was in the grass, and
    I ran like a cheetah, with thoughts of an assassin'''
    name = "MachinePistol"
    damage = 15
    cool_down = 0.2


class CricketBat(BaseWeapon):
    '''Smashy smashy'''
    name = "CricketBat"
    damage = 10
    cool_down = 1


class Fists(BaseWeapon):
    '''Thump 'em'''
    name = "Fists"
    damage = 3.3333
    cool_down = 1
