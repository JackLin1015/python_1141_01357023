class bankperson:
    def __init__(self, name, money): 
        self.name = name
        self.money = money
    def deposit(self, mo):
        self.money += mo
    def withdraw(self, mo):
        self.money -= mo
    def balance(self):
        print(str(self.money))

person = [] 
while True:
    check = 0
    do = input().split()
    if do[0] == "create":
        for p in person:
            if p.name == do[1]:
                p.money = int(do[2])
                check = 1
        if(check == 0):
            person.append(bankperson(do[1], int(do[2])))
    elif do[0] == "deposit":
        count = 0
        for p in person:
            if p.name == do[1]:
                p.deposit(int(do[2]))
            else:
                count += 1
        if(count == len(person)):
            print("Account not found")
    elif do[0] == "withdraw":
        count = 0
        for p in person:
            if p.name == do[1]:
                money = int(do[2])
                if(p.money < money):
                    print("Insufficient funds")
                else:
                    p.withdraw(int(do[2]))
            else:
                count += 1
        if(count == len(person)):
            print("Account not found")
    elif do[0] == "balance":
        count = 0
        for p in person:
            if p.name == do[1]:
                p.balance()
            else:
                count += 1
        if(count == len(person)):
            print("Account not found")
    elif do[0] == "stop":
        break