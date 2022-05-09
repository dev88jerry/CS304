
class BankAccount:
    """
    A bank account
    """

    def __init__(self, acntOwner, bankName):
        """
        Create a new bank account instance

        Initial balance is 0.0 (float)
        :param acntOwner: name of account owner/customer (string)
        :param bankName: name of bank (string)
        """
        assert isinstance(acntOwner, str)
        assert isinstance(bankName, str)

        self._acntOwner = acntOwner
        self._bankName = bankName
        self._balance = 0.0

    def get_customer(self):
        """
        getter for customer name
        :return: bank account owner name
        """
        return self._acntOwner

    def get_balance(self):
        """
        getter for balance on the account
        :return: balance of the account
        """
        return self._balance

    def get_bank(self):
        """
        getter for bank name of the account
        :return: name of bank
        """
        return self._bankName

    def deposit(self, amount):
        """
        function to deposit an amount to account balance
        :param amount: added to the bank balance
        :return:
        """
        amount = float(amount)
        assert isinstance(amount, float)
        self._balance += amount

    def withdraw(self, amount):
        """
        function to withdraw an amount from account balance
        :param amount: attempt to remove amount from balance
        :return: bool for operation success
        """
        amount = float(amount)
        assert isinstance(amount, float)

        if self._balance - amount > 0.00:
            self._balance -= amount
            return True
        else:
            return False

    def __iadd__(self, other):
        """
        override += used to add value to account balance
        :param other: value to be added to balance
        :return: new balance
        """
        other = float(other)
        assert isinstance(other, float)
        self._balance += other
        return self

    def __isub__(self, other):
        """
        override -= used to remove value to account balance
        :param other: value to be remove on balance
        :return: new balance
        """
        other = float(other)
        assert isinstance(other, float)
        self._balance -= other
        return self

    def __gt__(self, other):
        """
        override > operator to compare balance from 1 account to another
        :param other: another bank account instance
        :return: bool on operation
        """
        assert isinstance(other, BankAccount)
        if self._balance > other.get_balance():
            return True
        else:
            return False

    def __lt__(self, other):
        """
        override < operator to compare balance from 1 account to another
        :param other: another bank account instance
        :return: bool on operation
        """
        assert isinstance(other, BankAccount)
        if self._balance < other.get_balance():
            return True
        else:
            return False

