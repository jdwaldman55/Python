from abc import ABC, abstractmethod


class Dealer(ABC):
    def buyingCar(self, price):
        print("Your account will be charged: ",price)

    @abstractmethod
    def Notice(self, price):
        pass

class accountNotice(Dealer):
    def Notice(self, price):
        print("Your purchase of {} has been taken from your account".format(price))

obj = accountNotice()
obj.buyingCar('$25,000')
obj.Notice('$25,000')
