import turtle
from abc import ABC, abstractmethod

# Определяем абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self, fighter_turtle, monster_turtle):
        pass

# Реализуем конкретные типы оружия
class Sword(Weapon):
    def attack(self, fighter_turtle, monster_turtle):
        fighter_turtle.clear()
        fighter_turtle.color("blue")
        fighter_turtle.write("Меч", align="center", font=("Arial", 12, "normal"))
        fighter_turtle.forward(50)
        fighter_turtle.backward(50)

class Bow(Weapon):
    def attack(self, fighter_turtle, monster_turtle):
        fighter_turtle.clear()
        fighter_turtle.color("green")
        fighter_turtle.write("Лук", align="center", font=("Arial", 15, "normal"))
        fighter_turtle.forward(50)
        fighter_turtle.backward(50)

# Класс Monster
class Monster():
    def __init__(self, health, turtle_obj):
        self.health = health
        self.turtle_obj = turtle_obj

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.turtle_obj.color("red")
            self.turtle_obj.write("Побежден!", align="center", font=("Arial", 15, "normal"))

# Класс Fighter
class Fighter():
    def __init__(self, weapon: Weapon, turtle_obj):
        self.weapon = weapon
        self.turtle_obj = turtle_obj

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def fight(self, monster: Monster):
        self.weapon.attack(self.turtle_obj, monster.turtle_obj)
        monster.take_damage(10)

# Настройка turtle
def setup_turtle(shape, color, x, y):
    t = turtle.Turtle()
    t.shape(shape)
    t.color(color)
    t.penup()
    t.goto(x, y)
    return t

# Реализация боя
def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Создаем бойца и монстра
    fighter_turtle = setup_turtle("turtle", "blue", -100, 0)
    monster_turtle = setup_turtle("circle", "darkred", 100, 0)

    monster = Monster(health=20, turtle_obj=monster_turtle)
    sword = Sword()
    bow = Bow()

    fighter = Fighter(weapon=sword, turtle_obj=fighter_turtle)

    fighter.fight(monster)

    screen.ontimer(lambda: fighter.change_weapon(bow), 200)
    screen.ontimer(lambda: print("Боец выбирает лук."),200)
    screen.ontimer(lambda: fighter.fight(monster), 400)

    screen.mainloop()

if __name__ == "__main__":
    main()
