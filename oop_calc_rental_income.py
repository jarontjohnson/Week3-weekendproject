class Home:
    def __init__(self, income, expenses, cash_flow, cash_on_cash_roi):
        self.income = income
        self.expenses = expenses
        self.cash_flow = cash_flow
        self.cash_on_cash_roi = cash_on_cash_roi

    def income(self):
        income = input("Enter Income(or type 'q' to exit): ")
        if income.lower() == "q":
            sys.exit()

    def expenses(self):
        expenses = input("Enter Income(or type 'q' to exit): ")
        if expenses.lower() == "q":
            sys.exit()

    def calculate_cash_flow(self):
        return self.income - self.expenses
    
    def calculate_cash_on_cash_return(self):
        total_cash_investment = (self.income - self.expenses) 
        annual_cash_flow = self.calculate_cash_flow() * 12
        return (annual_cash_flow / total_cash_investment) * 100
    

print(income)
print(expenses)
print(cash_flow)
print(cash_on_cash_roi)
    

