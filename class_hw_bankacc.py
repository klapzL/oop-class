import datetime

from click import option


class BankAccount:
    def __init__(self, first_name, last_name, balance):
        self.__1st_name = first_name
        self.__2nd_name = last_name
        self.__balance = balance
        self.__history = {
            self.__2nd_name:
                {
                    'Deposits': [],
                    'Withdraws': [],
                    'Transfers': []
                }
            }

    def __str__(self):
        return f'{self.__2nd_name} {self.__1st_name}'

    @property
    def show_balance(self):
        print(f'На вашем счету {self.__balance}$')

    def show_history(self, key):
        print('; '.join(self.__history[self.__2nd_name][key]))

    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Сумма не может быть отрицательным')
        else:
            date = datetime.datetime.now().date()
            history = self.__history[self.__2nd_name]['Deposits']
            self.__balance += amount
            print(f'Счёт {self.__2nd_name}а был пополнен на {amount}$')
            history.append(f'{date}, сумма пополнения: {amount}')

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError('На вашем балансе недостаточно средств')
        elif amount < 0:
            raise ValueError('Сумма не может быть отрицательным')
        else:
            date = datetime.datetime.now().date()
            history = self.__history[self.__2nd_name]['Withdraws']
            self.__balance -= amount
            print(f'С счёта {self.__2nd_name}а было снято {amount}$')
            history.append(f'{date}, cумма снятия: {amount}')

    def transfer(self, account, amount):
        if amount > self.__balance:
            raise ValueError('На вашем балансе недостаточно средств')
        elif amount < 0:
            raise ValueError('Сумма не может быть отрицательным')
        else:
            date = datetime.datetime.now().date()
            history_self = self.__history[self.__2nd_name]['Transfers']
            history_acc = account.__history[account.__2nd_name]['Transfers']
            self.__balance -= amount
            print(f'{self.__2nd_name} перевёл {amount}$ {account.__2nd_name}у')
            account.deposit(amount)
            history_self.append(f'{date}, cумма перевода {amount}')
            history_acc.append(f'{date}, cумма пополнения {amount}')


def main():
    account1 = BankAccount('Эмир', 'Медетбеков', 1000)
    account2 = BankAccount('Тахир', 'Умуркулов', 1000)

    print(account1)
    print(account2)

    account1.withdraw(500)
    account1.deposit(200)
    account2.deposit(300)
    account2.withdraw(600)
    account2.withdraw(300)
    print('\n***HISTORY***')
    account1.show_history('Withdraws')
    account1.show_history('Deposits')
    account2.show_history('Withdraws')
    account2.show_history('Deposits')
    print('*************\n')

    account1.show_balance
    account2.show_balance

    account1.transfer(account2, 200)

    account1.show_balance
    account2.show_balance

    account2.transfer(account1, 500)

    account1.show_balance
    account2.show_balance
    print('\n***HISTORY***')
    account1.show_history('Transfers')
    account2.show_history('Transfers')
    print('*************\n')

    # Ошибки
    # account1.deposit(-200)
    # account1.withdraw(-10)
    # account2.withdraw(10000)
    # account1.transfer(account2, -200)
    # account1.transfer(account2, 20000)


if __name__ == '__main__':
    main()
