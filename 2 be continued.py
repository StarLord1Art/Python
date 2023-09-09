class A:
    def __init__(self, one, two):
        self.one = one
        self.two = 15
    
    def test (self):
        print (self.one**self.two)


some = A(2, 3)
some.one = 10
some.test()
