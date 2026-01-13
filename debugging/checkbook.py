#!/usr/bin/python3
"""
Simple Checkbook simulator.

Allows a user to deposit, withdraw, and check balance interactively.
"""

class Checkbook:
    def __init__(self):
        """Initialize the checkbook with a zero balance."""
        self.balance = 0.0

    def deposit(self, amount):
        """Add money to the balance."""
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.balance += amount
        print("✅ Deposited ${:.2f}".format(amount))
        print("💰 Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """Withdraw money if funds are sufficient."""
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("❌ Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("💸 Withdrew ${:.2f}".format(amount))
            print("💰 Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Display current balance."""
        print("💰 Current Balance: ${:.2f}".format(self.balance))


def main():
    """Main program loop."""
    cb = Checkbook()
    print("📘 Welcome to your Checkbook!")
    print("You can deposit, withdraw, check balance, or exit.\n")

    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == "exit":
            print("\n👋 Thank you for using the Checkbook. Goodbye!")
            break

        elif action == "deposit":
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("⚠️ Invalid input. Please enter a numeric value.")

        elif action == "withdraw":
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("⚠️ Invalid input. Please enter a numeric value.")

        elif action == "balance":
            cb.get_balance()

        else:
            print("❓ Invalid command. Please try again.")

if __name__ == "__main__":
    main()

