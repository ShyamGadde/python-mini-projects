from math import floor


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.budget = 0

    def deposit(self, amount, description=""):
        self.budget += amount
        self.ledger.append({"amount": amount, "description": description})

    def check_funds(self, amount):
        return amount <= self.budget

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.budget -= amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return self.budget

    def transfer(self, amount, transfer_category):
        if self.withdraw(amount, f"Transfer to {transfer_category.name}"):
            transfer_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        tmp = [self.name.center(30, "*")]
        tmp.extend(
            f'{entry["description"][:23].ljust(23)}{"{0:>7.2f}".format(entry["amount"])}'
            for entry in self.ledger
        )
        tmp.append(f"Total: {self.budget}")
        return "\n".join(tmp)


def create_spend_chart(categories):
    total_categories = len(categories)
    output = ["Percentage spent by category"]
    spending = [
        abs(sum(entry["amount"] for entry in category.ledger if entry["amount"] < 0))
        for category in categories
    ]
    total_spending = sum(spending)
    category_spending = [floor(x / total_spending * 10) * 10 for x in spending]
    output.extend(
        " ".join(
            [
                f"{y}|".rjust(4),
                (" " * 2).join([" " if x < y else "o" for x in category_spending]),
                " ",
            ]
        )
        for y in range(100, -1, -10)
    )
    output.append(" " * 4 + "-" * (total_categories * 3 + 1))
    labels = [category.name for category in categories]
    longest_label = max(len(label) for label in labels)
    labels = [label.ljust(longest_label) for label in labels]
    output.extend(
        " " * 5 + (" " * 2).join([label[i] for label in labels]) + (" " * 2)
        for i in range(longest_label)
    )
    return "\n".join(output)
