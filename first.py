import random
import time

class itstep:
    Alive = True
    Balance = random.randint(0,5500)
    LowerBalabce = 3000
    Adress = "проспект Степана Бандери, 83"
    AverageGrade = 10
    price = 750
    Name = "Ted Elliott"
    def Info (self):
        print (f"Information: \nName: {self.Name}  (Ім'я) \nAlive: {self. Alive}   (Живий або ні) \nAdress: {self.Adress}  (Адреса)")
    def Life (self):
        AverageGrade = random.randint(6,10)
        price = 750
        Balance = random.randint(0,4500)
        print("Balance: ", Balance)
        print("The Price of College: ", price)
        print("Average grade: ", AverageGrade)
        print("◙" *40)
        if Balance >= 2000 and AverageGrade >= 8:
            print(" У студента все окей(Перезапустіть Код)")
            
        if Balance <= 750 and AverageGrade <= 6:
            print("У студента багато проблем з грошми і оцінками, і його вигнули")
            
        while Balance >= 2000 and AverageGrade <= 8:
            print("Студент має пошані оцінки", AverageGrade)
            print("Студент пішов вчитися")
            time.sleep(3)
            AverageGrade = AverageGrade + 2
            print("Тепер студент має", AverageGrade)
            time.sleep(3)
            Balance = Balance - price
            print("Студент оплатив на коледж і його баланс є", Balance)
            if Balance >= 2000 and AverageGrade >= 8:
                print(" У студента все окей(Перезапустіть Код)")
                
            
        
        if Balance <= 2000:
            wage = random.randint(100,1100)
            print("Студент пішов на роботу")
            time.sleep(3)
            if wage <= 300:
                Balance = Balance + wage
                print("Студент працював погано і получив", wage, ". Його Баланс є", Balance)
            if wage >= 700:
                Balance = Balance + wage
                print("Студент працював добре і получив", wage, ". Його Баланс є", Balance)
            if wage >= 300 and wage <= 700:
                Balance = Balance + wage
                print("Студент працював нормально і получив", wage, ". Його Баланс є", Balance)
            time.sleep(3)
            Balance = Balance - price
            print("Студент оплатив на коледж і його баланс є", Balance)
            time.sleep(3)
            if Balance >= 2000 and AverageGrade >= 8:
                print("У студента все окей(Перезапустіть Код)")
                
            while Balance <= 2000:
                wage = random.randint(100,1100)
                print("Студент зрозумів що йому не буде хватати гроші то він пішов на роботу знову")
                time.sleep(3)
                if wage <= 300:
                    Balance = Balance + wage
                    AverageGrade = AverageGrade - 2
                    print("Студент працював погано і получив", wage, ". Його Баланс є", Balance, ". Студент почав получати пошані оцінки через то що він працював і не мав часу що робити домашнє і вчитися. Його середня оцінка дорівнює", AverageGrade)
                    while AverageGrade <= 8:
                        print("Студент має пошані оцінки", AverageGrade)
                        print("Студент пішов вчитися")
                        time.sleep(3)
                        AverageGrade = AverageGrade + 2
                        print("Тепер студент має", AverageGrade)
                        time.sleep(3)
                        Balance = Balance - price
                        if Balance <= 750 and AverageGrade <= 6:
                            print("У студента багато проблем з грошми і оцінками, і його вигнули")
                        if Balance >= 2000 and AverageGrade >= 8:
                            print(" У студента все окей(Перезапустіть Код)")
                            
                if wage >= 700:
                    Balance = Balance + wage
                    AverageGrade = AverageGrade - 2
                    print("Студент працював добре і получив", wage, ". Його Баланс є", Balance, ". Студент почав получати пошані оцінки через то що він працював і не мав часу що робити домашнє і вчитися. Його середня оцінка дорівнює", AverageGrade)
                    while AverageGrade <= 8:
                        print("Студент має пошані оцінки", AverageGrade)
                        print("Студент пішов вчитися")
                        time.sleep(3)
                        AverageGrade = AverageGrade + 2
                        print("Тепер студент має", AverageGrade)
                        time.sleep(3)
                        Balance = Balance - price
                        if Balance <= 750 and AverageGrade <= 6:
                            print("У студента багато проблем з грошми і оцінками, і його вигнули")
                        if Balance >= 2000 and AverageGrade >= 8:
                            print(" У студента все окей(Перезапустіть Код)")
                            
                if wage >= 300 and wage <= 700:
                    Balance = Balance + wage
                    AverageGrade = AverageGrade - 2
                    print("Студент працював нормально і получив", wage, ". Його Баланс є", Balance, ". Студент почав получати пошані оцінки через то що він працював і не мав часу що робити домашнє і вчитися. Його середня оцінка дорівнює", AverageGrade)
                    while AverageGrade <= 8:
                        print("Студент має пошані оцінки", AverageGrade)
                        print("Студент пішов вчитися")
                        time.sleep(3)
                        AverageGrade = AverageGrade + 2
                        print("Тепер студент має", AverageGrade)
                        time.sleep(3)
                        Balance = Balance - price
                        if Balance <= 750 and AverageGrade <= 6:
                            print("У студента багато проблем з грошми і оцінками, і його вигнули")
                        if Balance >= 2000 and AverageGrade >= 8:
                            print(" У студента все окей(Перезапустіть Код)")
                            

                
    
itstep1 = itstep()
itstep1.Info()
print("◙" *40)
itstep1.Life()

#for i in range(100):
#    if itlstep1.Balance <= 3000:
  #      wage = random.randint(100,1100)
  #      print("Студент пішов на роботу")
   #     wait(3)
   #     if wage <= 300:
   #         print("Студент працював погано і получив", wage)
   ##     if wage >= 700:
   #        print("Студент працював добре і получив", wage)
  # Z##     if wage >= 300 and wage <= 700:
    #        print("Студент працював нормально і получив", wage)
    
