
from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    """
    a savings account with interest
    """

    def __init__(self, acntOwner, bankName, interestRate):
        """

        :param acntOwner: string of user
        :param bankName: string of bank name
        :param interestRate: double
        """
        super().__init__(acntOwner, bankName)
        self._rate = interestRate

    def accrue_interest(self):
        """

        :return: new balance with interest calculated
        """
        self._balance += self._rate * self._balance


"""
Test section
"""

if __name__ == '__main__':
    savAccount = SavingsAccount("Jerry", "TD", 0.025)
    savAccount.deposit(100)
    savAccount.accrue_interest()
    savAccount += 101.1
    savAccount -= 5.55
    print(savAccount.get_balance())

    savAccount2 = SavingsAccount("Temp", "Temp", 0.015)
    savAccount2.deposit(50)
    savAccount2.accrue_interest()
    savAccount2 += 201.1
    savAccount2 -= 15.55
    print(savAccount2.get_balance())

    print(savAccount < savAccount2)
    print(savAccount2 < savAccount)
    print(savAccount > savAccount2)
    print(savAccount2 > savAccount)
