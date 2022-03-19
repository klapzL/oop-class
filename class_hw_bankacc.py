import datetime


class BankAccount:
    def __init__(self, first_name, last_name, balance):
<<<<<<< HEAD
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
        print(f'{self.__2nd_name} {self.__1st_name}, у вас {self.__balance}$')

    def show_history(self, key):
        print('; '.join(self.__history[self.__2nd_name][key]))
=======
        self.__first_name = first_name
        self.__last_name = last_name
        self.__balance = balance
        self.__history = {self.__last_name: {'Deposits': [], 'Withdraws': [], 'Transfers': []}}

    def __str__(self):
        return f'{self.__last_name} {self.__first_name}'

    @property
    def show_balance(self):
        print(f'{self.__last_name} {self.__first_name}, на вашем счету {self.__balance}$')

    def show_history(self, key):
        print('; '.join(self.__history[self.__last_name][key]))
>>>>>>> 12dbfb98055ad0036391e9f0f4883171e8df9ec9

    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Сумма не может быть отрицательным')
        else:
<<<<<<< HEAD
            history_lst = self.__history[self.__2nd_name]['Deposits']
            date = datetime.datetime.now().date()
            self.__balance += amount
            print(f'Счёт {self.__2nd_name}а был пополнен на {amount}')
            history_lst.append(f'{date}, сумма пополнения: {amount}')

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError('недостаточно средств')
        elif amount < 0:
            raise ValueError('Сумма не может быть отрицательной')
        else:
            history_lst = self.__history[self.__2nd_name]['Withdraws']
            date = datetime.datetime.now().date()
            self.__balance -= amount
            print(f'С счёта {self.__2nd_name}а было снято {amount}')
            history_lst.append(f'{date}, cумма снятия: {amount}')

    def transfer(self, account, amount):
        if amount > self.__balance:
            raise ValueError('недостаточно средств')
        elif amount < 0:
            raise ValueError('Сумма не может быть отрицательной')
        else:
            history_lst_1 = self.__history[self.__2nd_name]['Transfers']
            history_lst_2 = account.__history[account.__2nd_name]['Transfers']
            date = datetime.datetime.now().date()
            self.__balance -= amount
            print(f'{self.__2nd_name} перевёл {amount} {account.__2nd_name}у')
            account.deposit(amount)
            history_lst_1.append(f'{date}, cумма перевода {amount}')
            history_lst_2.append(f'{date}, cумма пополнения {amount}')
=======
            self.__balance += amount
            print(f'Счёт {self.__last_name}а {self.__first_name}а успешно был пополнен на {amount}$')

            self.__history[self.__last_name]['Deposits'].append(f'{datetime.datetime.now().date()}, сумма пополнения: {amount}')

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError('На вашем балансе недостаточно средств, для проведения транзакции')
        elif amount < 0:
            raise ValueError('Сумма не может быть отрицательным')
        else:
            self.__balance -= amount
            print(f'С счёта {self.__last_name}а {self.__first_name}а было снято {amount}$')
            self.__history[self.__last_name]['Withdraws'].append(f'{datetime.datetime.now().date()}, cумма снятия: {amount}')

    def transfer(self, account, amount):
        if amount > self.__balance:
            raise ValueError('На вашем балансе недостаточно средств, для проведения транзакции')
        elif amount < 0:
            raise ValueError('Сумма не может быть отрицательным')
        else:
            self.__balance -= amount
            print(f'{self.__last_name} {self.__first_name} перевёл {amount}$ на счёт {account.__last_name}а {account.__first_name}а')
            account.deposit(amount)
            self.__history[self.__last_name]['Transfers'].append(f'{datetime.datetime.now().date()}, cумма перевода {amount}')
            account.__history[account.__last_name]['Transfers'].append(f'{datetime.datetime.now().date()}, cумма пополнения {amount}')
>>>>>>> 12dbfb98055ad0036391e9f0f4883171e8df9ec9


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
<<<<<<< HEAD
    print('\n*****HISTORY*****')
=======
>>>>>>> 12dbfb98055ad0036391e9f0f4883171e8df9ec9
    account1.show_history('Withdraws')
    account1.show_history('Deposits')
    account2.show_history('Withdraws')
    account2.show_history('Deposits')
<<<<<<< HEAD
    print('**********\n')
=======
>>>>>>> 12dbfb98055ad0036391e9f0f4883171e8df9ec9

    account1.show_balance
    account2.show_balance

    account1.transfer(account2, 200)

    account1.show_balance
    account2.show_balance

    account2.transfer(account1, 500)

    account1.show_balance
    account2.show_balance
<<<<<<< HEAD
    print('\n*****HISTORY*****')
    account1.show_history('Transfers')
    account2.show_history('Transfers')
    print('**********\n')
=======
    account1.show_history('Transfers')
    account2.show_history('Transfers')
>>>>>>> 12dbfb98055ad0036391e9f0f4883171e8df9ec9

    # Ошибки
    # account1.deposit(-200)
    # account1.withdraw(-10)
<<<<<<< HEAD
    # account2.withdraw(10000000)
    # account1.transfer(account2, -200)
    # account1.transfer(account2, 20000000000)
=======
    # account2.withdraw(10000)
    # account1.transfer(account2, -200)
    # account1.transfer(account2, 20000)
>>>>>>> 12dbfb98055ad0036391e9f0f4883171e8df9ec9


if __name__ == '__main__':
    main()
