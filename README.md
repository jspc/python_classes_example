# Python Classes Example

A simple demonstration of what classes in python does.

This project uses pretty vanilla python; no types or pythonic tricks.

## Setup

This project uses [python 3](https://www.python.org/downloads/) and [Pipenv](https://pipenv.pypa.io/)

To configure this project for the first time:

```bash
$ pipenv install
```

## Tests

This project contains tests:

```bash
$ nose2
test_init (game.test_player.TestNPC) ... ok
test_resurrect_is_a_nop (game.test_player.TestNPC) ... ok
test_add_weapon (game.test_player.TestPlayer) ... ok
test_attack (game.test_player.TestPlayer) ... ok
test_attack_and_kill (game.test_player.TestPlayer) ... ok
test_die (game.test_player.TestPlayer) ... ok
test_equip_weapon (game.test_player.TestPlayer) ... ok
test_equip_weapon_negative_index (game.test_player.TestPlayer) ... ok
test_equip_weapon_out_of_range (game.test_player.TestPlayer) ... ok
test_init (game.test_player.TestPlayer) ... ok
test_resurrect (game.test_player.TestPlayer) ... ok
test_str (game.test_weapon.TestBaseWeapon) ... ok
test_str (game.test_weapon.TestCricketBat) ... ok
test_str (game.test_weapon.TestFists) ... ok
test_str (game.test_weapon.TestHandgun) ... ok
test_str (game.test_weapon.TestKnife) ... ok
test_str (game.test_weapon.TestMachinePistol) ... ok
test_simulate_attack (test_main.TestMain) ... ok
test_simulate_attack_by_dead_player (test_main.TestMain) ... ok
test_simulate_attack_on_dead_player (test_main.TestMain) ... ok

----------------------------------------------------------------------
Ran 20 tests in 0.003s

OK
Name                  Stmts   Miss  Cover
-----------------------------------------
game/__init__.py          0      0   100%
game/player.py           43      0   100%
game/test_player.py      77      0   100%
game/test_weapon.py      26      0   100%
game/weapon.py           29      0   100%
main.py                  33     12    64%
test_main.py             28      0   100%
-----------------------------------------
TOTAL                   236     12    95%
```

## Running

```bash
$ python main.py
Melissa Gomez                   <Handgun damage=20, cool_down=1 second>                 health: 3.33    k/d: 11/3 (=3.67)
Thomas Farrell                  <MachinePistol damage=15, cool_down=0.2 seconds>        health: 60.00   k/d: 13/3 (=4.33)
Tamara Ellis                    <Fists damage=3.3333, cool_down=1 second>               health: 68.33   k/d: 2/3 (=0.67)
Brad Mckee                      <Fists damage=3.3333, cool_down=1 second>               health: 65.00   k/d: 1/4 (=0.25)
Anthony Miller                  <MachinePistol damage=15, cool_down=0.2 seconds>        health: 18.33   k/d: 8/3 (=2.67)
David Stephens                  <CricketBat damage=10, cool_down=1 second>              health: 90.00   k/d: 5/4 (=1.25)
Jennifer Perry                  <MachinePistol damage=15, cool_down=0.2 seconds>        health: 13.33   k/d: 15/4 (=3.75)
Brian Nash                      <CricketBat damage=10, cool_down=1 second>              health: 90.00   k/d: 4/4 (=1.00)
Raymond Chavez                  <Handgun damage=20, cool_down=1 second>                 health: 33.33   k/d: 18/2 (=9.00)
Timothy Howell                  <Knife damage=10, cool_down=2 seconds>                  health: 100.00  k/d: 6/5 (=1.20)
Jill Jones                      <MachinePistol damage=15, cool_down=0.2 seconds>        health: 38.33   k/d: 16/2 (=8.00)
Karen Jennings                  <Handgun damage=20, cool_down=1 second>                 health: 45.00   k/d: 16/3 (=5.33)
Barbara Cain                    <Fists damage=3.3333, cool_down=1 second>               health: 23.33   k/d: 3/3 (=1.00)
Joseph Carpenter                <Knife damage=10, cool_down=2 seconds>                  health: 10.00   k/d: 6/2 (=3.00)
Matthew Doyle                   <Fists damage=3.3333, cool_down=1 second>               health: 36.67   k/d: 4/2 (=2.00)
Jordan Jarvis                   <Handgun damage=20, cool_down=1 second>                 health: 80.00   k/d: 17/4 (=4.25)
Philip Simpson                  <Knife damage=10, cool_down=2 seconds>                  health: 26.67   k/d: 7/3 (=2.33)
Gregory Simpson                 <Knife damage=10, cool_down=2 seconds>                  health: 51.67   k/d: 7/4 (=1.75)
Joseph Brown                    <Fists damage=3.3333, cool_down=1 second>               health: 20.00   k/d: 2/4 (=0.50)
Robert Myers                    <Handgun damage=20, cool_down=1 second>                 health: 11.67   k/d: 15/2 (=7.50)
William Moore                   <CricketBat damage=10, cool_down=1 second>              health: 10.00   k/d: 5/5 (=1.00)
Amanda Morris                   <Knife damage=10, cool_down=2 seconds>                  health: 46.67   k/d: 7/2 (=3.50)
Valerie Hodge                   <MachinePistol damage=15, cool_down=0.2 seconds>        health: 58.33   k/d: 11/4 (=2.75)
Ryan Sullivan                   <Knife damage=10, cool_down=2 seconds>                  health: 60.00   k/d: 7/3 (=2.33)
Brianna Rodriguez               <Knife damage=10, cool_down=2 seconds>                  health: 13.33   k/d: 5/3 (=1.67)
```
