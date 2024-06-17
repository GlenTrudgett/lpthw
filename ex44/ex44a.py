""" Inheritance versus Composition """

# Exercise 44a -  Inheritance versus Composition


class Parent(object):

    def implicit(self):
        print("PARENT implicit()")


class Child(Parent):
    pass


dad = Parent()
son = Child()

dad.implicit()
son.implicit()
