# coding: utf-8
"""<Oral Presentation> Bioinformatic principal component analysis by using Python"""

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import datetime as dt


def pca_demo(size_x=16, size_y=10):
    plt.figure(figsize=(size_x, size_y))
    iris = load_iris()
    pca = PCA(n_components=2)
    datas = pca.fit_transform(iris['data'])
    labels = list(set(iris['target']))
    colors = ["r", "g", "b"]
    for idx, label in enumerate(labels):
        plt.scatter(datas[iris['target'] == label][:, 0],
                    datas[iris['target'] == label][:, 1],
                    label=iris['target_names'][idx],
                    c=colors[idx])
    plt.legend(loc='upper right')


if __name__ == '__main__':
    start_time = dt.datetime.now().microsecond
    pca_demo()  # input expected picture size x, y
    plt.savefig("iris.png")
    end_time = dt.datetime.now().microsecond
    print('Complete ...')
    print("Running time: %d microsecond" % (end_time - start_time))
