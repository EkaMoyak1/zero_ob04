import random

class Hero:
    def __init__(self, name, hero_type):
        self.name = name
        self.health = 100
        self.attack_power = 20
        self.hero_type = hero_type
        self.special_ability_used = False

        # Уникальные характеристики для каждого типа героя
        if self.hero_type == "Воин":
            self.health += 20
            self.attack_power += 5
        elif self.hero_type == "Маг":
            self.attack_power += 10
        elif self.hero_type == "Лучник":
            self.attack_power += 7

    def attack(self, other):
        damage = self.attack_power
        # Случайный шанс на критический удар
        if random.randint(1, 10) == 1:
            damage *= 2
            print(f"{self.name} наносит критический удар!")
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

    def defend(self):
        # Уменьшает урон в следующей атаке
        self.defending = True
        print(f"{self.name} готовится к защите!")

    def use_special_ability(self, other):
        if self.hero_type == "Воин":
            if not self.special_ability_used:
                damage = self.attack_power * 2
                other.health -= damage
                self.special_ability_used = True
                print(f"{self.name} использует специальную способность 'Мощный удар' и наносит {damage} урона!")
            else:
                print(f"{self.name} уже использовал специальную способность!")
        elif self.hero_type == "Маг":
            self.health += 20
            print(f"{self.name} использует специальную способность 'Лечение' и восстанавливает 20 здоровья!")
        elif self.hero_type == "Лучник":
            damage = self.attack_power + 15
            other.health -= damage
            print(f"{self.name} использует специальную способность 'Точный выстрел' и наносит {damage} урона!")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name, player_type, difficulty="легкая"):
        self.player = Hero(player_name, player_type)
        self.computer = Hero("Компьютер", random.choice(["Воин", "Маг", "Лучник"]))
        self.difficulty = difficulty

        # Увеличиваем сложность компьютера
        if self.difficulty == "средняя":
            self.computer.health += 10
            self.computer.attack_power += 5
        elif self.difficulty == "сложная":
            self.computer.health += 20
            self.computer.attack_power += 10

    def start(self):
        print("Начало игры 'Битва героев'!")
        print(f"{self.player.name} ({self.player.hero_type}) vs {self.computer.name} ({self.computer.hero_type})")
        print(f"Уровень сложности: {self.difficulty}")
        print("-----------------------------")

        current_turn = 0  # 0 - ход игрока, 1 - ход компьютера

        while self.player.is_alive() and self.computer.is_alive():
            if current_turn == 0:
                self.player_turn()
            else:
                self.computer_turn()

            current_turn = 1 - current_turn  # Смена хода

        if self.player.is_alive():
            print(f"{self.player.name} побеждает!")
        else:
            print(f"{self.computer.name} побеждает!")

    def player_turn(self):
        print(f"Ход {self.player.name}:")
        print("1. Атака")
        print("2. Защита")
        print("3. Использовать специальную способность")
        choice = input("Выберите действие (1-3): ")

        if choice == "1":
            self.player.attack(self.computer)
        elif choice == "2":
            self.player.defend()
        elif choice == "3":
            self.player.use_special_ability(self.computer)
        else:
            print("Неверный выбор! Пропуск хода.")

        print(f"У {self.computer.name} осталось {self.computer.health} здоровья.\n")

    def computer_turn(self):
        print(f"Ход {self.computer.name}:")
        # Компьютер выбирает случайное действие
        action = random.choice(["attack", "defend", "special"])
        if action == "attack":
            self.computer.attack(self.player)
        elif action == "defend":
            self.computer.defend()
        elif action == "special":
            self.computer.use_special_ability(self.player)

        print(f"У {self.player.name} осталось {self.player.health} здоровья.\n")

if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    player_type = input("Выберите тип героя (Воин, Маг, Лучник): ")
    difficulty = input("Выберите уровень сложности (легкая, средняя, сложная): ").lower()
    game = Game(player_name, player_type, difficulty)
    game.start()