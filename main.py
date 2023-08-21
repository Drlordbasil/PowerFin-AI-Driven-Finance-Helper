import random
import time


class RetryError(Exception):
    pass


class RetryHelper:
    def __init__(self, max_retries=3, delay=1):
        self.max_retries = max_retries
        self.delay = delay

    def retry(self, func):
        tries = 0
        while tries < self.max_retries:
            try:
                return func()
            except RetryError:
                tries += 1
                time.sleep(self.delay)

        raise RetryError("Exceeded maximum number of retries")


class Transaction:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount


class ExpenseTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def track_spending_patterns(self):
        categories = {}
        total_spending = 0

        for transaction in self.transactions:
            category = transaction.category
            amount = transaction.amount

            if category not in categories:
                categories[category] = 0

            categories[category] += amount
            total_spending += amount

        spending_patterns = {
            category: (amount / total_spending) * 100
            for category, amount in categories.items()
        }

        return spending_patterns


class Budget:
    def __init__(self, income, expenses, savings_goal):
        self.income = income
        self.expenses = expenses
        self.savings_goal = savings_goal

    def suggest_spending_limits(self):
        total_expenses = sum(self.expenses.values())

        spending_limits = {
            category: (amount / total_expenses) * self.income
            for category, amount in self.expenses.items()
        }

        return spending_limits


class FinancialAssistant:
    def __init__(self):
        self.expense_tracker = ExpenseTracker()
        self.budget = None
        self.retry_helper = RetryHelper()

    def track_expenses(self):
        transactions = [
            Transaction("Food", 50),
            Transaction("Rent", 1000),
            Transaction("Transportation", 100),
            Transaction("Food", 30),
            Transaction("Entertainment", 80),
        ]

        for transaction in transactions:
            self.expense_tracker.add_transaction(transaction)

    def analyze_spending_patterns(self):
        def _analyze_spending_patterns():
            spending_patterns = self.expense_tracker.track_spending_patterns()
            print("Spending patterns:")
            for category, percentage in spending_patterns.items():
                print(f"- {category}: {percentage:.2f}%")
        
        self.retry_helper.retry(_analyze_spending_patterns)

    def set_budget(self):
        self.budget = Budget(
            income=2000, expenses={"Food": 300, "Rent": 1000, "Utilities": 200}, savings_goal=5000
        )

    def suggest_spending_limits(self):
        def _suggest_spending_limits():
            spending_limits = self.budget.suggest_spending_limits()
            print("Suggested spending limits:")
            for category, limit in spending_limits.items():
                print(f"- {category}: ${limit:.2f}")
            
        self.retry_helper.retry(_suggest_spending_limits)

    def execute_autonomous_program(self):
        self.track_expenses()
        self.analyze_spending_patterns()

        self.set_budget()
        self.suggest_spending_limits()


if __name__ == "__main__":
    assistant = FinancialAssistant()
    assistant.execute_autonomous_program()