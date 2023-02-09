# coding: utf-8
"""The principle of K Nearest Neighbors is that when we predict a new value x,
   we will determine which class x belongs to according to the class of the K nearest neighbors"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

"""
def KNeighborsClassifier(n_neighbors = 5,   # KNN 中的 “K”。
                         weights='uniform',   # ‘uniform’:不管远近权重都一样; ‘distance’:权重和距离成反比。
                         algorithm = '',   # ‘brute’:蛮力实现;‘kd_tree’:KD 树实现 KNN;‘ball_tree’:球树实现 KNN;‘auto’: 默认参数:自动选择合适的方法构建模型。
                         leaf_size = '30',   # 如果是选择蛮力实现，那么这个值是可以忽略的。当使用 Kd 树或球树，它就是停止建子树的叶子节点数量的阈值。默认30，但如果数据量增多这个参数需要增大，否则速度过慢不说，还容易过拟合。
                         p = 2,   # 和 metric 结合使用，当 metric 参数是 “minkowski” 的时候，p=1 为曼哈顿距离， p=2 为欧式距离。默认为p=2。
                         metric = 'minkowski',   # ‘euclidean’:欧式距离;‘manhattan’:曼哈顿距离;‘chebyshev’:切比雪夫距离;‘minkowski’:闵可夫斯基距离，默认参数。
                         metric_params = None,   
                         n_jobs = None   # 指定多少个CPU进行运算，默认是-1，也就是全部都算。
                         )
"""


n_neighbors = 11
# 导入一些要玩的数据
iris = datasets.load_iris()
x = iris.data[:, :2]  # 我们只采用前两个feature,方便画图在二维平面显示
y = iris.target

h = .02  # 网格中的步长

# 创建彩色的图
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

# weights是KNN模型中的一个参数，上述参数介绍中有介绍，这里绘制两种权重参数下KNN的效果图
for weights in ['uniform', 'distance']:
    # 创建了一个knn分类器的实例，并拟合数据
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(x, y)

    # 绘制决策边界，为此，我们将为每个分配一个颜色
    # 来绘制网格中的点 [x_min, x_max]x[y_min, y_max].
    x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
    y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # 将结果放入一个彩色图中
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # 绘制训练点
    plt.scatter(x[:, 0], x[:, 1], c=y, cmap=cmap_bold)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class classification (k = %i, weights = '%s')" % (n_neighbors, weights))

if __name__ == '__main__':
    plt.show()

