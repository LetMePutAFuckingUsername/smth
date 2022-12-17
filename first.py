import random

class itstep:
    Alive = True
    IP_Adress = 49.549949078716224, 25.627183265818076
    randomnuberforIQBOOST = random.randint(0,100)
    Adress = "проспект Степана Бандери, 83"
    Name = "IT STEP"
    def Info (self):
        print (f'Name: {self.Name}\nIP Adress: {self.IP_Adress} \nAlive: {self. Alive} \nAdress: {self.Adress}')

    def randomnumber (self):

        randomnumber = random.randint(0,100)
        print(f'Random number is {randomnumber}')
        
    def iqBoost (self, iq_added):
        self.number = self.randomnuberforIQBOOST + iq_added
        print(f'Number: {self.number}')
    
itstep1 = itstep()
itstep1.Info()
print("◙" *40)
itstep1.randomnumber()
print("#" *40)
itstep1.iqBoost(20)
