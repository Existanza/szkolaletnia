import matplotlib.pyplot as plt
import numpy as np

f = open("res.txt", 'r')
res_list = []
for word in f.read().split():
    res_list.append(float(word))
f.close()
plt.figure()
plt.bar(np.arange(len(res_list)), sorted(res_list))
# plt.show()
plt.savefig("res_plot.png", dpi=300)
plt.close()
