class Hello:
    def __init__(self, str):
        self.str = str
class Hello2(Hello):
    def __init__(self, str, name):
        super().__init__(str)
        self.name = name

    def working(self):
        return self.name




