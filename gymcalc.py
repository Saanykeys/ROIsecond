# Gym ROI Calc.

print('ROI GYM Calc!')

income = float(input('Enter your carry over income ($): '))
additional = float(input('Enter any additional income ($): ')) #youtube channel #personal trainning

total_income = income + additional
print('Great your total income next month will be ' + str(total_income))
print('Now what is your overhead..')

def total_expenses():
    tax = float(input('Enter your monthly county tax $: '))
    utilities = float(input('Enter your monthly utilities $: '))
    insurance = float(input('Enter your monthly insurance expense $: '))
    Smoothie_bar = float(input('Enter your monthly smoothie expense $: '))
    cleanning = float(input('Enter your cleaning expense $: '))
    payroll = float(input('Enter payroll expenses $: '))
    misc = float(input('Enter any additional monthly expenses $: '))
    broken_equipment = float(input('Enter any broken equipment monthly expenses $: '))
    total_expenses = tax + utilities + insurance + Smoothie_bar + cleanning + misc + payroll + broken_equipment
    return total_expenses

expense_total = total_expenses()
print('Great your total expenses next month will be' + str(expense_total))
margin = total_income - expense_total
if margin >= 0:
    print('Your total surplus next month will be $' + str(margin))
else:
    print('You will come up $' + str(margin) + ' negative!')

print('ROI Gym Calculator signing out!')

