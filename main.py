import random

class Character:
    def __init__(self, strength, condition, brains, intuition):
        self.damage = strength
        self.hp = condition * 10
        self.brains = brains
        self.intuition = intuition


player = Character(10, 10, 50, 2)
enemy = Character(10, 10, 20, 0)


def hit(player, enemy):   
    if random.randint(1, 100) > enemy.intuition:
        if random.randint(1, 100) <= player.brains:
            return player.damage * (random.randint(16, 24) / 10)
        else:
            return player.damage
    else:
        return 0


def main(player, enemy):
    while player.hp > 0 and enemy.hp > 0:
        pass


hit(player, enemy)