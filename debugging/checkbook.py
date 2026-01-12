class Checkbook:
	"""
	A simple Checkbook class to manage deposits, withdrawals, and balance.

	Attributes:
		balance (float): The current balance of the checkbook.
	"""

	def __init__(self):
		"""Initialize the checkbook with a zero balance."""
		self.balance = 0.0

	def deposit(self, amount):
		"""
		Deposit money into the checkbook.

		Args:
			amount (float): The amount to deposit. Must be positive.
		"""
		if amount <= 0:
			print("Deposit amount must be positive.")
			return
		self.balance += amount
		print(f"Deposited ${amount:.2f}")
		print(f"Current Balance: ${self.balance:.2f}")

	def withdraw(self, amount):
		"""
		Withdraw money from the checkbook.

		Args:
			amount (float): The amount to withdraw. Must be positive and <= balance.
		"""
		if amount <= 0:
			print("Withdrawal amount must be positive.")
			return
		if amount > self.balance:
			print("Insufficient funds to complete the withdrawal.")
		else:
			self.balance -= amount
			print(f"Withdrew ${amount:.2f}")
			print(f"Current Balance: ${self.balance:.2f}")

	def get_balance(self):
		"""Print the current balance."""
		print(f"Current Balance: ${self.balance:.2f}")


def main():
	"""
	Main function to interact with the Checkbook class.

	Supports the following commands:
		- deposit: Deposit an amount into the checkbook
		- withdraw: Withdraw an amount from the checkbook
		- balance: Check current balance
		- exit: Exit the program
	"""
	cb = Checkbook()

	while True:
		action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

		if action == 'exit':
			print("Exiting program. Goodbye!")
			break

		elif action == 'deposit':
			try:
				amount = float(input("Enter the amount to deposit: $"))
				cb.deposit(amount)
			except ValueError:
				print("Invalid input. Please enter a numeric value.")

		elif action == 'withdraw':
			try:
				amount = float(input("Enter the amount to withdraw: $"))
				cb.withdraw(amount)
			except ValueError:
				print("Invalid input. Please enter a numeric value.")

		elif action == 'balance':
			cb.get_balance()

		else:
			print("Invalid command. Please try again.")


if __name__ == "__main__":
	main()
