class Manager:
    def __init__(self, FIO, dolgn):
        self.FIO = FIO
        self.dolgn = dolgn
        Managers.append(self.FIO)

    def check(self, TV, buyer):
        TV.turn_on(buyer)

    def sell(self, Model, buyer):
        print('Телевизор ', Model, ' исправен, будете брать?')
        buyer.buy()

    def reject(self, Model, buyer):
        print('Телевизор ', Model, ' снят с продажи из-за неисправности')
        buyer.reject()

    def get_FIO(self):
        print(self.FIO)

    def get_dolgn(self):
        print(self.dolgn)


class TV:

    def __init__(self, Model, Workstate, Price):
        self.Model = Model
        self.Workstate = Workstate
        self.Price = Price

        TVs.append(self.Model)

    def turn_on(self, Manager, buyer):
        if (self.Workstate == 'working'):
            print('Телевизор работает')
            Manager.sell(self, self.Model, buyer)
        else:
            print('Телевизор не работает')
            Manager.reject(self, self.Model, buyer)

    def get_Model(self):
        print(self.Model)

    def get_Workstate(self):
        print(self.Workstate)

    def get_Price(self):
        print(self.Price)


class Buyer:
    def __init__(self, FIO, Manager):
        self.FIO = FIO
        self.Manager = Manager

    def get_FIO(self):
        print(self.FIO)

    def chooseTVrequest(self):
        print('Вот список всех телевизоров')
        show_TVs(TVs)

    def choose(self, TV):
        TV.turn_on(self.Manager, self)

    def buy(self):
        print('Я покупаю его')

    def reject(self):
        print('Жаль, что не работает')


def show_TVs(TVs):
    print(TVs)


def show_Managers(TVs):
    print(TVs)


TVs = []
Managers = []
Vasya = Manager('Vasiliy Pupkin', 'Starshiy')
Petya = Manager('Petr Lim', 'Mladshiy')
Igor = Manager('Igor Hort', 'Starshiy')
Egor = Manager('Egor Limon', 'Mladshiy')
Phillips = TV('Phillips', 'working', '45000')
Samsung = TV('Samsung', 'working', '40000')
Sony = TV('Sony', 'working', '65000')
Supra = TV('Supra', 'working', '15000')

Gleb = Buyer('Alisov Gleb', Manager)
Gleb.chooseTVrequest()
Gleb.choose(Supra)
