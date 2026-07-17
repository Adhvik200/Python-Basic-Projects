class Category:
    def __init__(self, name: str):
        self.name = name
        self.ledger = []

    def check_funds(self, amount):
        return self.get_balance() >= amount


    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
    
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        
        for item in self.ledger:
            description = item["description"][:23].ljust(23)
            amount = f"{item['amount']:>7.2f}"
            items += f"{description}{amount}\n"
            total += item["amount"]
                
            output = title + items + f"Total: {total:.2f}"
        return output



def create_spend_chart(categories):
    output = "Percentage spent by category\n"

    spent = []
    total_spent = 0

    
    for category in categories:
        amount = 0
        for item in category.ledger:
            if item["amount"] < 0:
                amount += -item["amount"]
        spent.append(amount)
        total_spent += amount

    
    percentages = []
    for amount in spent:
        percent = int((amount / total_spent) * 100)
        percentages.append((percent // 10) * 10)

    
    for level in range(100, -1, -10):
        output += f"{level:>3}|"
        for percent in percentages:
            if percent >= level:
                output += " o "
            else:
                output += "   "
        output += " \n"

    
    output += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    
    max_length = max(len(category.name) for category in categories)

   
    for i in range(max_length):
        output += "     "
        for category in categories:
            if i < len(category.name):
                output += category.name[i] + "  "
            else:
                output += "   "
        if i != max_length - 1:
            output += "\n"

    return output

food = Category("Food")
clothing = Category("Clothing")
entertainment = Category("Entertainment")

food.deposit(1000, "Initial deposit")
food.withdraw(150.25, "Groceries")
food.withdraw(50, "Dinner")

clothing.deposit(500, "Salary")
clothing.withdraw(75.50, "Shopping")

entertainment.deposit(300)
entertainment.withdraw(100, "Movie")
entertainment.transfer(50, food)

print(food)
print()
print(clothing)
print()
print(entertainment)
print()
print(create_spend_chart([food, clothing, entertainment]))
