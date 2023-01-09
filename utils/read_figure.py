import pickle
import matplotlib.pyplot as plt

fig = pickle.load(open("./output.pickle", "rb"))

fig.show()

plt.show()
