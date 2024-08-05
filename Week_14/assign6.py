class A:
    def __init__(self, one):
        self.one = one

class B:
    def __init__(self, two):
        self.two = two

class C:
    def __init__(self, three):
        self.three = three


class Text(A, B, C):
    def __init__(self, one, two, three):
        A.__init__(self,one)
        B.__init__(self, two)
        C.__init__(self, three)

    def show_name(self):
        return self.one + self.two + self.three


name = Text('Ya', 'ss', 'er')

print(name.show_name())