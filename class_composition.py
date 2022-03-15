from sympy import N


class BankAccount:
    def __init__(self, first_name, last_name, balance):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__balance = balance
    
    @property
    def show_balance(self):
        print(f'{self.__last_name} {self.__first_name}, на вашем счету {self.__balance}$')

    def __str__(self):
        return f'{self.__last_name} {self.__first_name}'

    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Сумма не может быть отрицательным')
        else:
            self.__balance += amount
            print(f'Счёт {self.__last_name}а {self.__first_name}а успешно был пополнен на {amount}$')

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError('На вашем балансе недостаточно средств, для проведения транзакции')
        elif amount < 0:
            raise ValueError('Сумма не может быть отрицательным')
        else:
            self.__balance -= amount
            print(f'С счёта {self.__last_name}а {self.__first_name}а было снято {amount}$')

    def transfer(self, account, amount):
        if amount > self.__balance:
            raise ValueError('На вашем балансе недостаточно средств, для проведения транзакции')
        elif amount < 0:
            raise ValueError('Сумма не может быть отрицательным')
        else:
            self.__balance -= amount
            print(f'{self.__last_name} {self.__first_name} перевёл {amount}$ на счёт {account.__last_name}а {account.__first_name}а')
            account.deposit(amount)

def main():
    account1 = BankAccount('Эмир', 'Медетбеков', 1000)
    account2 = BankAccount('Тахир', 'Умуркулов', 1000)

    print(account1)
    print(account2)
    print()


    account1.withdraw(500)
    account2.deposit(300)

    account1.show_balance
    account2.show_balance
    print()

    account1.transfer(account2, 200)

    account1.show_balance
    account2.show_balance
    print()

    account2.transfer(account1, 500)

    account1.show_balance
    account2.show_balance
    print()

    # Ошибки
    # account1.deposit(-200)
    # account1.withdraw(-10)
    # account2.withdraw(10000)
    # account1.transfer(account2, -200)
    # account1.transfer(account2, 20000)

if __name__ == '__main__':
    main()