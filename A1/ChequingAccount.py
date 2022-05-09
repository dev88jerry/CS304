
from BankAccount import BankAccount

class ChequingAccount(BankAccount):
    """
    a chequing account
    """

    def __init__(self, acntOwner, bankName, transactionFee):
        """
        constructor
        :param acntOwner: string of user
        :param bankName: string of bank
        :param transactionFee: fee to be charged
        """

        super().__init__(acntOwner, bankName)
        self._fee = transactionFee

    def make_purchase(self, amount):
        """
        make purchase on account and change fee
        :param amount: value of purchase
        :return: new balance on account
        """
        amount = float(amount)
        assert isinstance(amount, float)

        success = super().withdraw(amount)
        if success:
            self._balance -= self._fee + amount

        return success


"""
Test section
"""

if __name__ == '__main__':
    cheqAccount = ChequingAccount("Jerry", "BN", 1)
    cheqAccount.deposit(5000)
    cheqAccount.make_purchase(12)
    cheqAccount.make_purchase(1.01)
    cheqAccount.withdraw(50)
    cheqAccount.withdraw(5000)
    cheqAccount += 9000
    cheqAccount -= 1500
    print(cheqAccount.get_balance())

    cheq2 = ChequingAccount("Test", "test", 5)
    cheq2.deposit(999)
    cheq2.withdraw(9)
    cheq2.make_purchase(19)
    cheq2 += 11
    cheq2 -= 99
    print(cheq2.get_balance())

    print(cheq2 < cheqAccount)
    print(cheqAccount < cheq2)
    print(cheq2 > cheqAccount)
    print(cheqAccount > cheq2)
