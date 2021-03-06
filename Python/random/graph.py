import matplotlib.pyplot as plt
import numpy as np

n = 6
X = np.arange(n)
Y1 = (1-X/n)*np.random.uniform(0.5, 1.0, n)
Y1 = (1-X/n)*np.random.uniform(0.5, 1.0, n)

# 由于返回值，进过提取是str，操作小数位数不方便，外面提前处理好
p1 = plt.bar(X, np.round(Y1, 2), width=0.8, facecolor='blue', label='uniform')


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{}'.format(height),
                     xy=(rect.get_x() + rect.get_width() / 2, height),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom')

# 为什么有两个hight


def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2,
                 height, height, ha='center', va='bottom')
        rect.set_edgecolor('white')

# add_labels(p1)


autolabel(p1)

plt.legend(loc='best')
plt.show()
