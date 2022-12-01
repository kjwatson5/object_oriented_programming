# Box 1: income:
# Rental income, etc...

# Box 2: expenses:
# tax, insurance, utilities, HOA, lawn/snow, vacancy, repairs, capex, property manage, mortgage

# Box 3: Cash Flow:
# Income expense

# Box 4: cash on cash ROI:
# Down Payment
# Closing costs
# rehab budget
# misc
# annual cash flow / total investment = % cash on cash

class roiCalculator():

    def __init__(self, price_of_property):
        self.price_of_property = price_of_property

    def cash_flow(self):
        total_expenses = {}
        income = input('What is the total income from this property per month? ')
        while True:
            prompt = input('Do you want to add a monthly expense? Y = yes N = No: ')

            if prompt.title() == 'Y':
                expense = input('What is the expense you would like to add? ')
                expense_amount = input('How much is this expense per month?')
                total_expenses[expense] = int(expense_amount)
            elif prompt.title() == 'N':
                break

        sum_of_expenses = sum(total_expenses.values())
        cash_on_cash = {}
        while True:
            cash_prompt = input('Do you want to add an investment expense? Y = Yes N = No: ')

            if cash_prompt.title() == 'Y':
                cash_expense = input('What is the expense you would like to add? ')
                cash_amount = input('How much is this expense? ')
                cash_on_cash[cash_expense] = int(cash_amount)
            elif cash_prompt.title() == 'N':
                break

        sum_of_cash_expenses = sum(cash_on_cash.values())

        result = int(income) - sum_of_expenses

        raw_num = ((result * 12) / sum_of_cash_expenses * 100)
        finished_num = f"{raw_num}%"
        print(finished_num)
        return finished_num


def run():
    example_house = roiCalculator(200000)
    while True:
        prompt = input('Do you want to use this calculator again? Y = yes N = No: ')

        if prompt.title() == 'Y':
            example_house.cash_flow()

        elif prompt.title() == 'N':
            print('Goodbye')
            break

run()
