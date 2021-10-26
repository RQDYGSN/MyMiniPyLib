"""
main
"""
import minipy as py
import numpy as np
import math
import matplotlib.pyplot as plt

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # adj = [
    #     [0, 2, 6, 4],
    #     [float("inf"), 0, 3, float("inf")],
    #     [7, float("inf"), 0, 1],
    #     [5, float("inf"), 12, 0]
    # ]
    # g = py.graph(adj)
    # g.print_adjacency()
    # gg = py.shortestPathClass(g)
    # print(gg.shortestPath(1, 0))
    # print(gg.shortestCost(1, 0))
    # print()
    #
    # numList1 = py.numList([])
    # numList2 = py.numList([1, 1, 1, 1, 1])
    # numList3 = py.numList([1, 2, 3, 4, 5])
    # numList4 = py.numList([5, 1, 3, 2, 4])
    # print(numList1.findMiddleIndex())
    # print(numList1.minimumDifference(2))
    # print(numList1.insertionSort())
    # print(numList1.mergeSort())
    # print(numList2.findMiddleIndex())
    # print(numList2.minimumDifference(2))
    # print(numList2.insertionSort())
    # print(numList2.mergeSort())
    # print(numList3.findMiddleIndex())
    # print(numList3.minimumDifference(2))
    # print(numList3.insertionSort())
    # print(numList3.mergeSort())
    # print(numList4.findMiddleIndex())
    # print(numList4.minimumDifference(2))
    # print(numList4.insertionSort())
    # print(numList4.mergeSort())
    # print()
    #
    # a = np.array([1, 2, 3])
    # print(1, a.dot(a))
    # print(2, np.dot(a, a))
    # print(3, np.core.dot(a, a))
    # print(4, np.core.multiarray.dot(a, a))
    # print()
    #
    # s = ""
    # ss = py.SingleString(s)
    # print('max power is', ss.maxPower())
    # print()
    #
    # point1 = tuple([1, 2])
    # point2 = tuple([-2, -2])
    # p1 = py.Point2D(point1)
    # p2 = py.Point2D(point2)
    # print("p1 coordinate is", p1.coordinate)
    # print("p2 coordinate is", p2.coordinate)
    # print("Distance between p1 and p2 is", py.distance(p1, p2))

    def p(x):#从混合正态分布p中采样数据
        y = 0.5/(math.sqrt(2*math.pi))*math.exp(-1*(x+3)**2/2) + 0.5/(math.sqrt(2*math.pi)*2)*math.exp(-1*(x-3)**2/8)
        return y

    theta = py.metropolis_hasting_sampling(p, T=50000, combustion_period=100, thetamin=-10, thetamax=15, q_sigma=1)

    plt.figure(figsize=(6, 4))
    plt.hist(theta, bins=50, density=1, facecolor='orange', alpha=0.7)
    plt.show()


    def p(x):
        '''
        二维正态分布
        x is tuple or list.
        '''
        assert len(x) == 2
        x1 = x[0]
        x2 = x[1]
        mu1 = 5
        mu2 = -1
        sigma1 = 1
        sigma2 = 2
        rho = 0.5
        return (2*math.pi*sigma1*sigma2*math.sqrt(1-rho**2))**(-1)*math.exp(-0.5/(1-rho**2)*(((x1-mu1)**2/sigma1**2)-(2*rho*(x1-mu1)*(x2-mu2)/sigma1/sigma2)+((x2-mu2)**2/sigma2**2)))

    x_res = py.gibbs_sampling(p, dim=2, combustion_period=100, T=20210, thetamin=-10, thetamax=10, q_sigma=1)

    num_bins = 40
    plt.hist([i[0] for i in x_res], bins=num_bins, density=1, facecolor='green', alpha=0.5)
    plt.hist([i[1] for i in x_res], bins=num_bins, density=1, facecolor='red', alpha=0.5)
    plt.title('Histogram')
    plt.show()

    # 绘图设置
    fig = plt.figure()
    # X和Y的个数要相同
    plt.hist2d([i[0] for i in x_res], [i[1] for i in x_res], bins=50)
    plt.show()
