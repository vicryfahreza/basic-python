class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "Esport":
            print(self.name, "Plays Esport")
        if self.occupation == "body builder":
            print(self.name, "Do Exercising alot")

    def do_speak(self):
        print(self.name,"Says Hello everynyan")

vicry=Human("vicry", "Esport")
vicry.do_work()
vicry.do_speak()