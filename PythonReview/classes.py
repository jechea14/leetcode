class Beach:
    # parts = ['water', 'sand'] # class variable
    def __init__(self, location, water_color, temperature):
        self.location = location  # instance variables
        self.water_color = water_color
        self.temperature = temperature
        self.heat_rating = "hot" if temperature > 80 else "cool"
        self.parts = ["water", "sand"]

    def add_part(self, part):
        self.parts.append(part)


class Dog:
    def __init__(self, name, age, friendliness) -> None:
        self.name = name
        self.age = age
        self.friendliness = friendliness

    def likes_walks(self):
        return True

    def bark():
        return "woof"


class Samoyed(Dog):  # inherited from dog
    def __init__(self, name, age, friendliness) -> None:
        super().__init__(name, age, friendliness)

    # polymorphism
    def bark():
        return "ARK BARK"


class Poodle(Dog):
    def __init__(self, name, age, friendliness) -> None:
        super().__init__(name, age, friendliness)

    def shedding_amount(self):
        return 0


class GoldenRetriever(Dog):
    def __init__(self, name, age, friendliness) -> None:
        super().__init__(name, age, friendliness)

    def fetch_ability(self):
        if self.age < 2:
            return 8
        elif self.age < 10:
            return 10
        else:
            return 7


# multiple inheritance
class GoldenDoodle(Poodle, GoldenRetriever):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    # polymorphism
    def bark():
        return "AROOOOO"


# polymorphism: many forms, child class overrides a method of the parent class to take a new form
def main():
    sammy = Samoyed("sammy", 2, 10)
    print(sammy.likes_walks())
    print(sammy.name, sammy.age, sammy.friendliness)
    goldie = GoldenDoodle("Goldie", 1, 10)
    print(goldie.name, goldie.age, goldie.friendliness)
    print(goldie.likes_walks())
    print(goldie.shedding_amount(), goldie.fetch_ability())

    cape_code_beach: Beach = Beach("Cape Cod", "dark blue", 70)
    cancuun: Beach = Beach("Cacuun", "crystal blue", 90)
    print(cape_code_beach.location, cape_code_beach.heat_rating)
    print(cancuun.location)
    cape_code_beach.add_part("rock")
    print(cape_code_beach.parts)
    la_beach: Beach = Beach("LA", "truqiuse", 85)
    hot_not_rocky = []

    for beach in [cape_code_beach, cancuun, la_beach]:
        if beach.heat_rating == "hot" and "rock" not in beach.parts:
            hot_not_rocky.append(beach)
    return hot_not_rocky


if __name__ == "__main__":
    beaches = main()
    print([beach.location for beach in beaches])
