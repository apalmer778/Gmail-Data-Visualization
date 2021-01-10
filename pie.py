
import matplotlib.pyplot as plt
from email_data import search_inbox
data = search_inbox('ALL', 'to')
labels = []
values = []
for item in data:
    labels.append(item[0])
    values.append(item[1])


plt.figure(figsize = (5,5))
plt.pie(values, labels = labels, autopct = '%.1f%%')
plt.show()

