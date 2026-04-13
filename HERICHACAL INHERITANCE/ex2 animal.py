class animal:
    def eat(self):
        print("the animal eat chicken")
class cat(animal):
    def meow(self):
        print("the cat sounds meow")
class dog(animal):
    def bark(self):
        print("the dog barks")
c=cat()
d=dog()
c.meow()
c.eat()
d.bark()
