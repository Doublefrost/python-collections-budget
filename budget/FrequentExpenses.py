from . import Expense
import collections
import matplotlib.pyplot as plt

expenses = Expense.Expenses()
expenses.read_expenses("data/spending_data.csv")

spending_catagories = []
for expense in expenses.list:
    spending_catagories.append(expense.catagory)

spending_counter = collections.Counter(spending_catagories)

top5 = spending_counter.most_common(5)

catagories, count = zip(*top5)

fig, ax = plt.subplots()

ax.bar(catagories, count)
ax.set_title('# of Purchases by Category')
plt.show()
