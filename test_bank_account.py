import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        """Подготовка тестовых данных перед каждым тестом."""
        self.acc1 = BankAccount("Иван Иванов", "ACC1001")
        self.acc2 = BankAccount("Пётр Петров", "ACC1002")

    def test_initial_state(self):
        """Тест: начальное состояние нового счёта."""
        self.assertEqual(self.acc1.owner, "Иван Иванов")
        self.assertEqual(self.acc1.account_number, "ACC1001")
        self.assertEqual(self.acc1.get_balance(), 0.0)
        self.assertTrue(self.acc1.is_empty())

    def test_deposit_valid(self):
        """Тест: корректное пополнение счёта."""
        self.acc1.deposit(500.0)
        self.assertEqual(self.acc1.get_balance(), 500.0)
        self.assertFalse(self.acc1.is_empty())

    def test_deposit_invalid_amount(self):
        """Тест: попытка пополнить счёт на 0 или отрицательную сумму."""
        with self.assertRaises(ValueError):
            self.acc1.deposit(0)
        with self.assertRaises(ValueError):
            self.acc1.deposit(-100)
        self.assertEqual(self.acc1.get_balance(), 0.0)

    def test_withdraw_valid(self):
        """Тест: корректное снятие средств со счёта."""
        self.acc1.deposit(1000.0)
        self.acc1.withdraw(400.0)
        self.assertEqual(self.acc1.get_balance(), 600.0)

    def test_withdraw_exceeds_balance(self):
        """Тест: попытка снять больше, чем есть на балансе."""
        self.acc1.deposit(100.0)
        with self.assertRaises(ValueError):
            self.acc1.withdraw(150.0)
        self.assertEqual(self.acc1.get_balance(), 100.0)

    def test_withdraw_invalid_amount(self):
        """Тест: попытка снять 0 или отрицательную сумму."""
        self.acc1.deposit(100.0)
        with self.assertRaises(ValueError):
            self.acc1.withdraw(0)
        with self.assertRaises(ValueError):
            self.acc1.withdraw(-50)

    def test_transfer_success(self):
        """Тест: успешный перевод средств с одного счёта на другой."""
        self.acc1.deposit(1000.0)
        self.acc2.deposit(200.0)

        self.acc1.transfer(self.acc2, 400.0)

        self.assertEqual(self.acc1.get_balance(), 600.0)
        self.assertEqual(self.acc2.get_balance(), 600.0)

    def test_transfer_insufficient_funds(self):
        """Тест: неуспешный перевод при недостатке денег (балансы не меняются)."""
        self.acc1.deposit(100.0)
        self.acc2.deposit(500.0)

        with self.assertRaises(ValueError):
            self.acc1.transfer(self.acc2, 200.0)

        self.assertEqual(self.acc1.get_balance(), 100.0)
        self.assertEqual(self.acc2.get_balance(), 500.0)

    def test_is_empty(self):
        """Тест: проверка счёта на пустоту."""
        self.assertTrue(self.acc1.is_empty())
        self.acc1.deposit(100.0)
        self.assertFalse(self.acc1.is_empty())
        self.acc1.withdraw(100.0)
        self.assertTrue(self.acc1.is_empty())


if __name__ == "__main__":
    unittest.main()