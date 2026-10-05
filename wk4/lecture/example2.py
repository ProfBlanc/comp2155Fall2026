"""
Create a Fighting Game
    two TYPES of players
        Fighter
        Boss
    both PLAYERS have
        name
        health
        power
    Boss has a can use a special move between 1 and 3 times that attacks by 3x power
    Player can block an attack between 1 and 3 times


How many classes to make? Name them
    4

    Player
    Boss
    Fighter
    Game
"""
import random
from abc import ABC, abstractmethod
class Player(ABC):
    def __init__(self, name, health, power):
        self.__name = name
        self.__health = health
        self.__power = power
    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError("Invalid name. Min 3 characters")
        self.__name = value
    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self, value):
        if type(value) != int or value < 50 or value > 100: raise ValueError("Invalid health. Values must be between 50 and 100")
        self.__health = value
    @property
    def power(self):
        return self.__power
    @power.setter
    def power(self, value):
        if type(value) != int or value < 4 or value > 10: raise ValueError("Invalid power. Values must be between 5 and 10")
        self.__power = value
    @abstractmethod
    def shout_catch_phrase(self):
        pass
    # common actions between Boss & Player

    def _gets_attacked(self, opponent):
        self._verify_opponent(opponent)
        self.__health -= opponent.power

    def _verify_opponent(self, opponent):
        if not isinstance(opponent, Player):
            raise TypeError("opponent must be an Player")

    def attack(self, opponent):
        self._verify_opponent(opponent)
        opponent._gets_attacked(self)
        self._summarize_attack(opponent)

    def _summarize_attack(self, opponent):
        self._verify_opponent(opponent)
        print(self.name, "is attacking", opponent.name, "with a power of", self.power)
        if opponent.health <= 0:
            print(opponent.name, "no longer has any health remaining")
        else:
            print(opponent.name, "now has a health of", opponent.health)

    def _amplify_power(self, magnifier):
        if magnifier < 2 or magnifier > 5: raise ValueError("Invalid Power Magnifier")
        self.__power *= magnifier

    def is_alive(self): return self.health > 0

class Fighter(Player):
    def __init__(self, name, health, power, block_attempts=random.randint(1, 3)):
        super().__init__(name, health, power)
        self.__block_attempts = block_attempts

    def _gets_attacked(self, opponent):
        self._verify_opponent(opponent)
        if self.__block_attempts > 0:
            use_block = input(f"{self.name} has {self.__block_attempts} blocks remaining. Do you want to use one? y/n: ")
            if use_block.strip().lower() == "y":
                self.__block_attempts -= 1
                return
        super()._gets_attacked(opponent)

    def shout_catch_phrase(self):
        choices = ["You're not that tough!", "Ha, Ha, Ha!", "Resistance is futile!", "Too bad, so sad!"]
        return f"I'm {self.name}! {random.choice(choices)}"
    @classmethod
    def duplicate_boss(cls, boss):
        if not isinstance(boss, Boss):
            raise TypeError("fighter must be a Boss")
        return cls(boss.name, boss.health, boss.power)

class Boss(Player):
    def __init__(self, name, health, power, attack_amplifier=random.randint(1, 3)):
        super().__init__(name, health, power)
        self.__attack_amplifier = attack_amplifier
    def attack(self, opponent):
        if self.__attack_amplifier > 0:
            answer = input(f"{self.name} has {self.__attack_amplifier} attack amplifiers remaining. Do you want to use one? y/n: ")
            if answer.strip().lower() == "y":
                self.__attack_amplifier -= 1

                stronger_self = Fighter.duplicate_boss(self)
                stronger_self._amplify_power(3)

                opponent._gets_attacked(stronger_self)
                stronger_self._summarize_attack(opponent)
                return
        super().attack(opponent)
    def shout_catch_phrase(self):
        choices = ["That was easy as 1,2,3", "I was waiting for this moment!", "Who did you think you were!", "Booooooo"]
        return f"They call me Boss {self.name}! {random.choice(choices)}"

class Game:
    """
    start a game without specify Players
    """
    def __init__(self):
        self.__players = [
            Fighter("Fighter", 100, 4),
            Boss("Boss", 100, 5),
            Fighter("Batman", 100, 6),
            Boss("Venom", 100, 7),
        ]
    # a fight method
    # randomly choose a player
    # that player attack the other player
    # feedback on who attacked who
    # repeat until a player no longer has health
    def fight(self):
        while len(self.__players) > 1:

            attacker = random.choice(self.__players)
            opponents = [player for player in self.__players if player is not attacker and player.is_alive()]
            defender = random.choice(opponents)

            attacker.attack(defender)

            if not defender.is_alive():
                print(defender.name, "has been defeated")
                self.__players.remove(defender)


            print("*" * 20)

        print("#" * 20)
        print(attacker.name, "has won the fight")
        print(attacker.shout_catch_phrase())
fight = Game()
fight.fight()
