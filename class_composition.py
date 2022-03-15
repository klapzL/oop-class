class BankAccount:
    def __init__(self, first_name, last_name, balance):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__balance = balance
    
    def show_balance(self):
        return self.__balance

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def transfer(self, account, amount):
        if amount > self.__balance or amount < 0:
            raise ValueError('Неккоректо веддено')
        else:
            self.__balance -= amount

account1 = BankAccount('Emir', 'Medetbekov', 1000)
account2 = BankAccount('Takhir', 'Umurkulov', 1000)

account1.transfer(account2, 200)
