
from tabulate import tabulate

class Organism:
    population = []

    def __init__(self, name, species):
        self.name = name
        self.species = species

        self.max = 2  # Number of class attributes for iteration

    def __repr__(self):
        return 'Name: {}, Species: {}'.format(self.name, self.species)

    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):
        self.start = self.start + 1
        if self.start > self.max:
            raise StopIteration
        if self.start == 1:
            return self.name
        if self.start == 2:
            return self.species

    def create(self):
        name = input('Write the name: ')
        species = input('Write the species: ')
        variable = Organism(name[0].upper() + name[1:].lower(), species[0].upper() + species[1:].lower())
        print('Organism successfully created!\n')
        self.population.append(tuple(variable))
        return variable

    def remove(self):
        name = input('Write the name: ')
        for x in self.population:
            if name[0].upper() + name[1:].lower() in x[0]:
                self.population.remove(x)
                print('Organism successfully removed!\n')

            else:
                pass

    def all(self):
        print('')
        print(tabulate(self.population, headers=['Name', 'Species'], tablefmt='orgtbl'))
        print('')

    @staticmethod
    def help():
        a = ['1. Create Organism', 'Create']
        b = ['2. Remove Organism', 'Remove']
        c = ['3. Show population', 'Show']
        d = ['4. Population list', 'List']
        e = ['5. Show Commands', 'Help']
        f = ['7. End the Script', 'X']
        g = ['6. Clear Terminal', 'Clear']

        print(tabulate([a, b, c, d, e, g, f], headers=['Action', 'Command'], tablefmt='orgtbl'))
        print('')
