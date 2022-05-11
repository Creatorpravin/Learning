import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 10, 5])
mylabels = ["Apples", "Bananas", "Cherries", "Dates", "nuts"]
mycolors = ["red", "yellow", "darkred", "green", "brown"]

plt.pie(y, labels = mylabels, colors=mycolors)
plt.legend(title = "Four Fruits:")
plt.show() 