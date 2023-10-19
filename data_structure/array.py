"""Expenses in each month index as month"""

expenses = [2200, 2350, 2600, 2130, 2190]

# In feburary how much you spend more

print(expenses[1] - expenses[0])

# expense in first 3 months
quarter_expense = 0
for i in range(3):
    quarter_expense += expenses[i]

print(quarter_expense)

for i in range(len(expenses)):
    if expenses[i] == 2200:
        print("you have spend 2200 in ", i)

# append june expense
expenses.append(1980)

# refund in april
expenses[3] = expenses[3] + 200
print(expenses)
