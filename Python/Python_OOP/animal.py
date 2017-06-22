class Animal(object):
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print "Name: " + self.name + " health: " + str(self.health)
        return self
    def __repr__(self):
        return "<Animal object name {}, health {}>".format(self.name, self.health)

if __name__ == '__main__':
    animal = Animal("animal")
    animal.walk().walk().walk().run().run().displayHealth()


class Dog(Animal):
    def __init__(self,name):

        super(Dog, self).__init__(name)
        self.name = name
        self.health = 150

    def pet(self):
        self.health += 5
        return self
    def __repr__(self):
        return "<Dog object name {}, health {}>".format(self.name, self.health)

if __name__ == '__main__':
    dog = Dog('dog')
    dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self,name):

        super(Dragon, self).__init__(name)
        self.name = name
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        print "this is a dragon"
        super(Dragon, self).displayHealth()
        return self
    def __repr__(self):
        return "<Dragon object name {}, health {}>".format(self.name, self.health)


if __name__ == '__main__':
    dragon = Dragon('drodro')
    dragon.walk().walk().walk().run().run().fly().fly().displayHealth()
