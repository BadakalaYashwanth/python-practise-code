# Parent class
class Animal:

    def sound(self):

        print("\nAnimal makes sound")


# Child class
class Dog(Animal):

    # Overriding parent method
    def sound(self):

        print("Dog barks")


# Creating object
dog = Dog()


# Calling overridden method
dog.sound()