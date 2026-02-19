class Fighter :
    
    def __init__(self , name , health , power):
        self.name = name
        self.health = health
        self.power = power
    
    def Show_status(self) :
        print(f"Name : {self.name}")
        print(f"Health : {self.health}")
        print(f"power : {self.power}")
        print()

    def attack (self , other) :
        other.health -= self.power 

f1 = Fighter(f"Ali" , 100 , 20)
f2 = Fighter(f"Reza" , 80 , 15 )

f1.attack(f2)
f2.Show_status()

f2.attack(f1)
f1.Show_status()
