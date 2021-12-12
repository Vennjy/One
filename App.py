class Hero:
    def __init__(self, name, hp, defense, damage):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.damage = damage

    def attack(self):
        return self.name + ' attacks for ' + str(self.damage) + ' damage.'


hero = Hero('Mogri', 20, 5, 8)
print(hero.attack())


class Assasin(Hero):
    def __init__(self, name, hp, defense, damage):
        super(Assasin, self).__init__(name, hp, defense, damage)
        self.ability = self.assassinate()

    def __str__(self):
        return '{} (Name: {}, hp: {}, defense: {}, damage: {})'.format(self.__class__.__name__, self.name, self.hp,
                                                                       self.defense, self.damage)

    def assassinate(self):
        return self.name + ' attacks for ' + str(self.damage * 2) + ' damage.'


assasin = Assasin('Rigward', 5, 0, 15)
print(assasin.attack())
print(assasin)
