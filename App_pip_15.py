"""
PIP is a package manager for python packages, or modules if you like
to check for the version pip --version
to use pip you need the keyword: pip install thenPackageName
"""
import matplotlib.pyplot as pyplot
# from forex_python.converter import CurrencyRates
#

# Currency converter
# c = CurrencyRates()
# amount = int(input("Enter the amount: "))
# from_currency = input("From Currency: ").upper()
# to_currency = input("To Currency: ").upper()
# print(from_currency, " To ", to_currency, amount)
#
# result = c.convert(from_currency, to_currency, amount)
# print(result)

# plotting a pie chart

labels = ('python', 'java', 'php', 'web')
sizes = [150, 80, 10, 35]
pyplot.pie(sizes,
labels=labels,
autopct='%1.f%%',
counterclock=False,
startangle=105)

# DIsplay the fiquares
pyplot.show()