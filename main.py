import random

class Character:
    def __init__(self, strength, condition, brains, intuition):
        self.damage = strength
        self.condition = condition
        self.hp = condition * 10
        self.brains = brains
        self.intuition = intuition

    def reset(self):
        self.hp = self.condition * 10


def hit(player, enemy, echo = False):   
    if random.randint(1, 100) > enemy.intuition:
        if random.randint(1, 100) <= player.brains:
            # crit
            damage = round(player.damage * (random.randint(16, 24) / 10))  # 1.6 - 2.4 spread (TODO)
            if echo: 
                print(f"{damage}!!")
            return damage
        else:
            # normal hit
            damage = round(player.damage)  # TODO: spread check
            if echo: 
                print(f"{damage}") 
            return damage
    else:
        # dodge
        damage = 0
        if echo:
            print("Unik!")
        return 0


def fight(player, enemy):
    player.reset()
    enemy.reset()

    while True:
        enemy.hp -= hit(player, enemy)
        # print(f"Enemy HP: {enemy.hp}")
        if enemy.hp <= 0:
            return True
        
        player.hp -= hit(enemy, player)
        # print(f"Your HP: {player.hp}")
        if player.hp <= 0:
            return False

def main():
    player = Character(10, 10, 20, 2)
    enemy = Character(10, 10, 20, 20)
    echo = False  # be careful with echo when simulating multiple battles
    simulation_count = 10000  # number of simulates to perform

    wins = 0

    for i in range(simulation_count):
        if(fight(player, enemy)):
            wins += 1

    winrate = (wins / simulation_count) * 100

    print(f"You won {wins} of {simulation_count} fights ({winrate}% winrate.).")

main()