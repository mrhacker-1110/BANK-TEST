class BankAccount:
    """Класс для работы с банковским счётом."""

    def __init__(self, owner: str, account_number: str):
        if not owner or not isinstance(owner, str):
            raise ValueError("Имя владельца должно быть непустой строкой.")
        if not account_number or not isinstance(account_number, str):
            raise ValueError("Номер счёта должен быть непустой строкой.")

        self.owner = owner
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, amount: float) -> None:
        """Пополнение счёта на указанную сумму."""
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть больше нуля.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Снятие денежных средств со счёта."""
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть больше нуля.")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счёте.")
        self.balance -= amount

    def transfer(self, target_account: "BankAccount", amount: float) -> None:
        """Перевод денег на другой счёт."""
        if not isinstance(target_account, BankAccount):
            raise TypeError("Целевой счёт должен быть объектом BankAccount.")
        if target_account is self:
            raise ValueError("Нельзя перевести деньги на тот же самый счёт.")

        # Если на счёте недостаточно денег, withdraw выбросит ошибку,
        # и состояние обоих счетов не изменится.
        self.withdraw(amount)
        target_account.deposit(amount)

    def get_balance(self) -> float:
        """Возвращает текущий баланс счёта."""
        return self.balance

    def is_empty(self) -> bool:
        """Определяет, является ли счёт пустым."""
        return self.balance == 0.0