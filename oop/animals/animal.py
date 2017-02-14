class Animal(object):
    def __init__(self, name, health=100):
       print "New Animal!"
       self.name = name
       self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print "Name: ", self.name
        print "Health: ", self.health
        return self



animal = Animal("Harry")
animal.walk().walk().walk().run().run().display_health()
# animal.fly().display_health()