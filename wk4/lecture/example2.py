"""
Create a Fighting Game
    two TYPES of players
        Fighter
        Boss
    both PLAYERS have
        name
        health
        power
    Boss has a can use a special move once that attacks by 3x power
    Player can block an attack twice


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
        self.name = name
        self.health = health
        self.power = power
    @abstractmethod
    def shout_catch_phrase(self): pass
    # common actions between Boss & Player

    def attack(self, opponent):
        if not isinstance(opponent, Player):
            raise TypeError("opponent must be an Player")
        opponent.health -= self.power
    def is_alive(self): return self.health > 0

class Fighter(Player):
    def __init__(self, name, health, power, block_attempts=2):
        super().__init__(name, health, power)
        self.__block_attempts = block_attempts
    def attack(self, opponent):
        super().attack(opponent)

        if self.__block_attempts > 0:
            use_block = input(f"You have {self.__block_attempts} blocks remaining. Do you want to use one? y/n: ")
            if use_block.strip().lower() == "y":
                opponent.health += self.power
                self.__block_attempts -= 1
            # just as an example. currently in reserve order

    def shout_catch_phrase(self):
        return f"You're not that tough!"

class Boss(Player):
    def __init__(self, name, health, power, attack_amplifier=1):
        super().__init__(name, health, power)
        self.__attack_amplifier = attack_amplifier
    def shout_catch_phrase(self): return "Easy as 1,2,3"

class Game:
    """
    start a game without specify Players
    """
    def __init__(self):
        self.__players = [
            Fighter("Fighter", 20, 4),
            Boss("Boss", 22, 5)
        ]
    # a fight method
    # randomly choose a player
    # that player attack the other player
    # feedback on who attacked who
    # repeat until a player no longer has health
    def fight(self):
        while self.__players[0].is_alive() and self.__players[1].is_alive():
            rand_num = random.randint(1, 100)  # get a random number

            attacker = rand_num % 2  # 0 or 1
            attacked = 1 if attacker == 0 else 0

            player_attacker = self.__players[attacker]
            player_attacked = self.__players[attacked]

            player_attacker.attack(player_attacked)

            print(player_attacker.name, "attacked", player_attacked.name, "with a power of", player_attacker.power)
            print(player_attacked.name, "now has a health of", player_attacked.health)
            print("*" * 20)

        print(player_attacker.name, "has won the fight")
        print(player_attacker.shout_catch_phrase())
fight = Game()
fight.fight()
