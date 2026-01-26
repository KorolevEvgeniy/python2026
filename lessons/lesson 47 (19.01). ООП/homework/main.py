class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def open(self):
        print(f"Книга '{self.title}' открыта на первой странице")

    def read(self):
        print(f"Читаем книгу '{self.title}' автора {self.author}")

    def close(self):
        print(f"Книга '{self.title}' закрыта.")

    def info(self):
       print(f"'{self.title}' - {self.author}, {self.pages} стр.")


# Создаём объект
my_book = Book("1984", "Джорж Оруэлл", 328)
my_book.open()
my_book.read()
my_book.close()
my_book.info()

print("=" * 50)

class BankAccount:
    interest_rate = 0.05
    
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float):
        if not self.is_valid_amount(amount):
            print('Некорректная сумма')
        else:
            self.balance += amount
    
    def withdraw(self, amount: float):
        if not self.is_valid_amount(amount):
            print('Некорректная сумма')
        elif amount > self.balance:
            print('Недостаточно средств')
        else:
            self.balance -= amount
    
    @staticmethod
    def is_valid_amount(amount: float) -> bool:
        return isinstance(amount, (int, float)) and amount > 0
    
    @classmethod
    def set_interest_rate(cls, new_rate: float):
        cls.interest_rate = new_rate
        print(f'Процентная ставка изменена на {cls.interest_rate}')
    
    def __str__(self):
        return f'Владелец: {self.owner}, Баланс: {self.balance}'
    
account1 = BankAccount("Иван Иванов", 1000)
account2 = BankAccount("Петр Петров", 500)
    
print(f"До операций:")
print(f"  {account1}")
print(f"  {account2}")
    
account1.deposit(500)
account1.withdraw(200)
account2.deposit(-100) 
account2.withdraw(600)  
account2.withdraw(300)
    
print(f"После операций:")
print(f"  {account1}")
print(f"  {account2}")
    
    
BankAccount.set_interest_rate(0.07)
print(f"Текущая процентная ставка: {BankAccount.interest_rate}")

print("=" * 50)


class LibraryBook(Book):
    def __init__(self, title: str, author: str, pages: int):
        super().__init__(title, author, pages)
        self.reader = None
    
    def take(self, name: str):
        if self.reader is not None:
            print('Книга уже выдана')
        else:
            self.reader = name
            print(f'Книга выдана: {name}')
    
    def return_back(self):
        if self.reader is None:
            print('Книга и так в библиотеке')
        else:
            print('Книга возвращена')
            self.reader = None


lib_book = LibraryBook("Мастер и Маргарита", "Михаил Булгаков", 480)
lib_book.info()

lib_book.take("Анна")
lib_book.take("Сергей")  

lib_book.return_back()

lib_book.take("Сергей")  
lib_book.return_back()