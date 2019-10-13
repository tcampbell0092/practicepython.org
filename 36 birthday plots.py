import json
from collections import Counter
from bokeh.plotting import figure, show, output_file


# month list
month = []

# converts numbers to string for months
num_to_string = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}


# function to read json file and return info from file
with open('birthdays.json', 'r') as f:
    birthdays = json.load(f)


# function to convert months into string
months = []
for x in birthdays.values():
    month.append(num_to_string[int(x.split('/')[0])])
counter_months = Counter(month)

# creates categories for values to see
x_categories = []
x = []
y = []

for key, value in counter_months.items():
    x.append(key)
    y.append(value)

# outputs given filename
output_file('plot.html')

# appends key and value to plot
for key, value in num_to_string.items():
    x_categories.append(value)

# creates histogram itself with specific height and length
p = figure(x_range=x_categories)
p.vbar(x=x, top=y, width=0.5)

# trigger to show histogram in plot.html
show(p)
