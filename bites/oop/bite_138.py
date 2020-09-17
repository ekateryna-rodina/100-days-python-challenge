class Animal:
    animal_count = 0
    instances = []
    def __init__(self, name):
        Animal.animal_count = Animal.animal_count + 1
        self.name = name
        self.number = Animal.animal_count
        Animal.instances.append((self))
        

    def __str__(self):
        return f'{10000 + self.number}. {self.name.title()}'

    @classmethod
    def zoo(cls):
        result = ''
        for a in cls.instances:
            result += str(a) + ' \n'
        return result.strip()