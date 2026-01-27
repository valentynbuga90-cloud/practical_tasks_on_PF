class Humanity:
    def __init__(self, planet, population):
        self.planet = planet              
        self.__population = population    

    def get_population(self):
        return self.__population

    def set_population(self, population):
        if population >= 0:
            self.__population = population
        else:
            print("Населення не може бути від'ємним")

    def info(self):
        return f"Людство живе на планеті {self.planet}. Населення: {self.__population}"

    def live(self):
        return "Людство існує та розвивається."


class Person(Humanity):
    def __init__(self, planet, population, name, age):
        super().__init__(planet, population)
        self.name = name
        self.age = age

    def info(self):
        return f"Людина: {self.name}, вік: {self.age}, планета: {self.planet}"

    def live(self):
        return f"{self.name} живе, навчається та взаємодіє з суспільством."


humanity = Humanity("Земля", 8000000000)
person = Person("Земля", 8000000000, "Андрій", 18)

print(humanity.info())
print(humanity.live())

print()

print(person.info())
print(person.live())

print("\nНаселення (через getter):", humanity.get_population())
humanity.set_population(8100000000)
print("Оновлене населення:", humanity.get_population())
