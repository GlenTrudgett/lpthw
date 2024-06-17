""" Inheritance Versus Composition """

# Exercise 44d - Inheritance Versus Composition


class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def overrride(self):
        print("PARENT overrride()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

dad.override()
son.override()

dad.implicit()
son.implicit()

dad.altered()
son.altered()
