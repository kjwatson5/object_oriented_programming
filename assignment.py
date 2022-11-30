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
        income = input('What is the total income from this property? ')
        expenses = input('What is the total cost of expenses for this property? ')
        result = int(income) - int(expenses)
        cash_on_cash = input('What is the total cost of investment? ')
        raw_num = ((result * 12) / int(cash_on_cash)) * 100
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
