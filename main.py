import random

class Character:
    def __init__(self, strength, condition, brains, intuition):
        self.damage = strength
        self.hp = condition * 10
        self.brains = brains
        self.intuition = intuition


player = Character(10, 10, 50, 20)
enemy = Character(10, 10, 20, 20)


def hit(player, enemy):   
    if random.randint(1, 100) > enemy.intuition:
        if random.randint(1, 100) <= player.brains:
            return player.damage * (random.randint(16, 24) / 10)
        else:
            return player.damage
    else:
        return 0


def fight(player, enemy):
    while player.hp > 0 and enemy.hp > 0:
        enemy.hp =- hit(player, enemy)
        if enemy.hp == 0:
            return True
        
        player.hp =- hit(enemy, player)
        if player.hp == 0:
            return False

def main(player, enemy):
    pass

main(player, enemy)