class Father:
    def skill(self):
        print("gardening, programming")

class Mother:
    def skill(self):
        print("cooking, music")

class Child(Father, Mother):
    def skill(self):
        Father.skill(self)
        Mother.skill(self)
        print("sport")

c=Child()
c.skill()