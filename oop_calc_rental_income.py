class Home:
    def __init__(self, income, expenses, investments):
        self.income = income
        self.expenses = expenses
        self.cash_flow = 0
        self.roi = 0
        self.investments = investments

    def cash_flow(self):
        self.cash_flow = self.income - self.expenses
        return self.cash_flow

    def assets(self,amount):
        self.income += amount

    def calculate_cash_flow(self):
        self.cash_flow = self.cash_flow * 12
        return self.cash_flow
    
    def calculate_roi(self):
        self.roi = (self.cash_flow - self.investments) * 100
        return self.roi
    
monthly_income = int(input("Enter your monthly income: "))
assets = int(input("Enter your assets: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
investments = int(input("Enter your total investments: "))

r = Home(monthly_income, monthly_expenses, investments)
r.assets(assets)
r.cash_flow()
r.calculate_cash_flow()
r.calculate_roi()

print("Your total ROI is: " + str(r.roi) + "%") # print(r.roi)
