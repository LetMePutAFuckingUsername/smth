import random

class Human:
    power = 6
    health = 75
    mana = 15

    def simpleHit(self):
        return self.power
    def takeHit(self,hit):
        if self.health>hit:
            self.health = self.health - hit
        else:
            self.health = self.health - hit
        return 0

    def Heal(self):
        RandomNumberForHeal = random.randint(5,13)
        self.health = self.health + RandomNumberForHeal
        return 0

    def superHit(self):
        if self.makeSkill(5) != 0:
            return self.power + self.power % 50
        else:
            print("Bot doesn't have enough mana to use super hit.")
            return 0

    def makeSkill(self,mana):
        if self.mana >=mana:
            self.mana = self.mana-mana
        else:
            print('Not enough mana')
            return 0
    def __str__(self):
        return (f'''Health: {self.health}
Mana: {self.mana}
''')
    def isAlive(self):
        return self.health>0

class Knight(Human):
    def __init__(self):
        self.health = 100
        self.power = 7

    def superHit(self):
        if self.makeSkill(5) != 0:
            return self.power + self.power % 50
        return 0
    def Heal(self):
        RandomNumberForHeal = random.randint(5,13)
        self.health = self.health + RandomNumberForHeal
        return 0

hero = Knight()
enemy = Human()

while(hero.isAlive() and enemy.isAlive()):
    ManaRegenForAPlayer = random.randint(1, 3)
    ManaRegenForABot = random.randint(1, 3)
    RobotChoice = random.randint(1, 4)
    choice = int(input('''1-Simple hit | 2-Critical hit | 3-Block | 4-Heal
    '''))
    if choice == 1 and RobotChoice == 1:
        hero.takeHit(enemy.simpleHit())
        enemy.takeHit(enemy.simpleHit())
        print("You chose a simple hit and the Bot chose a simple hit.")
        print("About you:")
        print(hero)
        print("About enemy: ")
        print(enemy)
        print("You  got ", ManaRegenForAPlayer, " mana, and Bot got ", ManaRegenForABot, " mana.")
        hero.mana = hero.mana + ManaRegenForAPlayer
        enemy.mana = enemy.mana + ManaRegenForABot
        print("So, you got ", hero.mana, " mana, And bot got ", enemy.mana, 'mana.')
    elif choice == 2 and RobotChoice == 1:
        print("You chose a super hit and the Bot chose a simple hit.")
        enemy.takeHit(hero.superHit())
        hero.takeHit(enemy.simpleHit())
        print("About you:")
        print(hero)
        print("About enemy: ")
        print(enemy)
        print("You  got ", ManaRegenForAPlayer, " mana, and Bot got ", ManaRegenForABot, " mana.")
        hero.mana = hero.mana + ManaRegenForAPlayer
        enemy.mana = enemy.mana + ManaRegenForABot
        print("So, you got ", hero.mana, " mana, And bot got ", enemy.mana, 'mana.')
    elif choice == 3 and RobotChoice == 1:
        print("You chose a block and the Bot chose a simple hit.")
        print("About you:")
        print(hero)
        print("About enemy: ")
        print(enemy)
        print("You  got ", ManaRegenForAPlayer, " mana, and Bot got ", ManaRegenForABot, " mana.")
        hero.mana = hero.mana + ManaRegenForAPlayer
        enemy.mana = enemy.mana + ManaRegenForABot
        print("So, you got ", hero.mana, " mana, And bot got ", enemy.mana, 'mana.')
    elif choice == 4 and RobotChoice == 1:
        hero.takeHit(enemy.simpleHit())
        hero.takeHit(hero.Heal())
        print("You chose heal and the Bot chose a simple hit.")
        print("About you:")
        print(hero)
        print("About enemy: ")
        print(enemy)
        print("You  got ", ManaRegenForAPlayer, " mana, and Bot got ", ManaRegenForABot, " mana.")
        hero.mana = hero.mana + ManaRegenForAPlayer
        enemy.mana = enemy.mana + ManaRegenForABot
        print("So, you got ", hero.mana, " mana, And bot got ", enemy.mana, 'mana.')
    elif choice == 1 and RobotChoice == 2:
        hero.takeHit(enemy.superHit())
        enemy.takeHit(hero.simpleHit())
        print("You chose a simple hit and the Bot chose a super hit.")
        print("About you:")
        print(hero)
        print("About enemy: ")
        print(enemy)
        print("You  got ", ManaRegenForAPlayer, " mana, and Bot got ", ManaRegenForABot, " mana.")
        hero.mana = hero.mana + ManaRegenForAPlayer
        enemy.mana = enemy.mana + ManaRegenForABot
        print("So, you got ", hero.mana, " mana, And bot got ", enemy.mana, 'mana.')
    elif choice == 2 and RobotChoice == 2:
        print("You chose a super hit and the Bot chose a super hit.")
        enemy.takeHit(hero.superHit())
        hero.takeHit(enemy.superHit())
        print("About you:")
        print(hero)
        print("About enemy: ")
        print(enemy)
        print("You  got ", ManaRegenForAPlayer, " mana, and Bot got ", ManaRegenForABot, " mana.")
        hero.mana = hero.mana + ManaRegenForAPlayer
        enemy.mana = enemy.mana + ManaRegenForABot
        print("So, you got ", hero.mana, " mana, And bot got ", enemy.mana, 'mana.')
    elif choice == 3 and RobotChoice == 2:
        hero.takeHit(enemy.simpleHit())
        print("You chose a block and the Bot chose a super hit. You got 50% of super hit damage due block.")
        print("About you:")
        print(hero)
        print("About enemy: ")
        print(enemy)
        print("You  got ", ManaRegenForAPlayer, " mana, and Bot got ", ManaRegenForABot, " mana.")
        hero.mana = hero.mana + ManaRegenForAPlayer
        enemy.mana = enemy.mana + ManaRegenForABot
        print("So, you got ", hero.mana, " mana, And bot got ", enemy.mana, 'mana.')
    elif choice == 4 and RobotChoice == 2:
        hero.takeHit(enemy.superHit())
        hero.takeHit(hero.Heal())
        print("You chose heal and the Bot chose a super hit.")
        print("About you:")
        print(hero)
        print("About enemy: ")
        print(enemy)
        print("You  got ", ManaRegenForAPlayer, " mana, and Bot got ", ManaRegenForABot, " mana.")
        hero.mana = hero.mana + ManaRegenForAPlayer
        enemy.mana = enemy.mana + ManaRegenForABot
        print("So, you got ", hero.mana, " mana, And bot got ", enemy.mana, 'mana.')
    elif choice == 1 and RobotChoice == 3:
        print("You chose a simple hit and the Bot chose a block.")
        print("About you:")
        print(hero)
        print("About enemy: ")
        print(enemy)
        print("You  got ", ManaRegenForAPlayer, " mana, and Bot got ", ManaRegenForABot, " mana.")
        hero.mana = hero.mana + ManaRegenForAPlayer
        enemy.mana = enemy.mana + ManaRegenForABot
        print("So, you got ", hero.mana, " mana, And bot got ", enemy.mana, 'mana.')
    elif choice == 2 and RobotChoice == 3:
        enemy.takeHit(hero.simpleHit())
        print("You chose super hit and the Bot chose a block. Bot got 50% of super hit damage due block.")
        print("About you:")
        print(hero)
        print("About enemy: ")
        print(enemy)
        print("You  got ", ManaRegenForAPlayer, " mana, and Bot got ", ManaRegenForABot, " mana.")
        hero.mana = hero.mana + ManaRegenForAPlayer
        enemy.mana = enemy.mana + ManaRegenForABot
        print("So, you got ", hero.mana, " mana, And bot got ", enemy.mana, 'mana.')
    elif choice == 3 and RobotChoice == 3:
        print("You chose a block and the Bot chose a block. So, nothing happened")
        print("About you:")
        print(hero)
        print("About enemy: ")
        print(enemy)
        print("You  got ", ManaRegenForAPlayer, " mana, and Bot got ", ManaRegenForABot, " mana.")
        hero.mana = hero.mana + ManaRegenForAPlayer
        enemy.mana = enemy.mana + ManaRegenForABot
        print("So, you got ", hero.mana, " mana, And bot got ", enemy.mana, 'mana.')
    elif choice == 4 and RobotChoice == 3:
        hero.takeHit(hero.Heal())
        print("You chose heal and the Bot chose block.")
        print("About you:")
        print(hero)
        print("About enemy: ")
        print(enemy)
        print("You  got ", ManaRegenForAPlayer, " mana, and Bot got ", ManaRegenForABot, " mana.")
        hero.mana = hero.mana + ManaRegenForAPlayer
        enemy.mana = enemy.mana + ManaRegenForABot
        print("So, you got ", hero.mana, " mana, And bot got ", enemy.mana, 'mana.')
    elif choice == 1 and RobotChoice == 4:
        enemy.takeHit(hero.simpleHit())
        enemy.takeHit(enemy.Heal())
        print("You chose heal and the Bot chose a simple hit.")
        print("About you:")
        print(hero)
        print("About enemy: ")
        print(enemy)
        print("You  got ", ManaRegenForAPlayer, " mana, and Bot got ", ManaRegenForABot, " mana.")
        hero.mana = hero.mana + ManaRegenForAPlayer
        enemy.mana = enemy.mana + ManaRegenForABot
        print("So, you got ", hero.mana, " mana, And bot got ", enemy.mana, 'mana.')
    elif choice == 2 and RobotChoice == 4:
        enemy.takeHit(hero.superHit())
        enemy.takeHit(enemy.Heal())
        print("You chose heal and the Bot chose a super hit.")
        print("About you:")
        print(hero)
        print("About enemy: ")
        print(enemy)
        print("You  got ", ManaRegenForAPlayer, " mana, and Bot got ", ManaRegenForABot, " mana.")
        hero.mana = hero.mana + ManaRegenForAPlayer
        enemy.mana = enemy.mana + ManaRegenForABot
        print("So, you got ", hero.mana, " mana, And bot got ", enemy.mana, 'mana.')
    elif choice == 3 and RobotChoice == 4:
        enemy.takeHit(enemy.Heal())
        print("You chose block and the Bot chose heal.")
        print("About you:")
        print(hero)
        print("About enemy: ")
        print(enemy)
        print("You  got ", ManaRegenForAPlayer, " mana, and Bot got ", ManaRegenForABot, " mana.")
        hero.mana = hero.mana + ManaRegenForAPlayer
        enemy.mana = enemy.mana + ManaRegenForABot
        print("So, you got ", hero.mana, " mana, And bot got ", enemy.mana, 'mana.')
    elif choice == 4 and RobotChoice == 4:
        enemy.takeHit(enemy.Heal())
        hero.takeHit(hero.Heal())
        print("You chose heal and the Bot chose heal.")
        print("About you:")
        print(hero)
        print("About enemy: ")
        print(enemy)
        print("You  got ", ManaRegenForAPlayer, " mana, and Bot got ", ManaRegenForABot, " mana.")
        hero.mana = hero.mana + ManaRegenForAPlayer
        enemy.mana = enemy.mana + ManaRegenForABot
        print("So, you got ", hero.mana, " mana, And bot got ", enemy.mana, 'mana.')


