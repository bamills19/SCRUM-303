#Name, Type, Hunger, Happiness, Bond

#Methods = Play, Eat, Sleep

#Show status


class Pet: 
    def __init__(self):

        self.Name = ["Jim", "Bradd", "Jett"]
        self.Type = ["Elephant", "Dog", "Raccoon"]
        self. Hunger = 100
        self.Happiness = 100
        self.Bond = 100

    def Play(self,Bond):
        self.Bond +=10

    def Eat(self,Hunger):
        self.Hunger +=10


    def Sleep(self,Happiness):
        self.Happiness +=10
    

    