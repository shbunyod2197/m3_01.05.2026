# 11
class Shape:
    def __init__(self, name, color, border):
        self.name = name
        self.color = color
        self.border = border

    def area(self):
        print(f"aniqlanmagan")


class Circle(Shape):
    def __init__(self, name, color, border, radius, diameter):
        super().__init__(name, color, border)
        self.radius = radius
        self.diameter = diameter

    def area(self):
        super().area()
        print(self.diameter * 0.3)


a = Circle("tort burchak", "oq", 32, 18, 40)
a.area()

# 12
class Worker:
    def __init__(self, name, salary, company):
        self.name = name
        self.salary = salary
        self.company = company

    def work(self):
        print(self.name,"ishda")

class Programmer(Worker):
    def __init__(self, name, salary, company, language, level):
        Worker.__init__(self, name, salary, company)
        self.language = language
        self.level = level

    def work(self):
        super().work()
        print(self.language, self.level)


a = Programmer("", 20000, "Python", "English", "Math")
a.work()

# 13
class Appliance:
    def __init__(self, brand, power, voltage):
        self.brand = brand
        self.power = power
        self.voltage = voltage

    def start(self):
        print(f"{self.brand} ishga tushdi")

class WashingMachine(Appliance):
    def __init__(self, brand, power, voltage, capacity, mode):
        super().__init__(brand, power, voltage)
        self.capacity = capacity
        self.mode = mode

    def start(self):
        super().start()
        print(f"Hajmi: {self.capacity}, Rejim: {self.mode}")

    def wash(self):
        print(f"{self.brand} kir yuvmoqda")

a = WashingMachine("Samsung", 2000, 220, "7kg", "Auto")
a.start()
a.wash()


# 14
class Game:
    def __init__(self, title, genre, size):
        self.title = title
        self.genre = genre
        self.size = size

    def play(self):
        print(f"{self.title} boshlandi")

class OnlineGame(Game):
    def __init__(self, title, genre, size, server, players):
        super().__init__(title, genre, size)
        self.server = server
        self.players = players

    def play(self):
        super().play()
        print(f"Server: {self.server}, O'yinchilar: {self.players}")

    def connect(self):
        print(f"{self.server} serverga ulanildi")

b = OnlineGame("Minecraft", "Sandbox", "1GB", "EU-1", 100)
b.play()
b.connect()


# 15
class Account:
    def __init__(self, owner, balance, currency):
        self.owner = owner
        self.balance = balance
        self.currency = currency

    def deposit(self, amount):
        self.balance += amount
        print(f"Balans oshdi: {self.balance} {self.currency}")

class BankAccount(Account):
    def __init__(self, owner, balance, currency, account_type, bank_name):
        super().__init__(owner, balance, currency)
        self.account_type = account_type
        self.bank_name = bank_name

    def deposit(self, amount):
        super().deposit(amount)
        print(f"Hisob turi: {self.account_type}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Pul yechildi: {amount} {self.currency}, Qoldiq: {self.balance}")

c = BankAccount("Ali", 1000, "UZS", "Jamg'arma", "Kapitalbank")
c.deposit(500)
c.withdraw(200)
