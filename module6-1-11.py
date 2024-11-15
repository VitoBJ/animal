class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


lion = Predator(name="Лев")
deer = Mammal(name="Олень")

rose = Flower(name="Розу")
apple = Fruit(name="Яблоко")


lion.eat(rose)
print(f"alive: {lion.alive}, fed: {lion.fed}")

lion.eat(apple)
print(f"alive: {lion.alive}, fed: {lion.fed}")

deer.eat(rose)
print(f"alive: {deer.alive}, fed: {deer.fed}")

deer.eat(apple)
print(f"alive: {deer.alive}, fed: {deer.fed}")
