## minipy

> author = RQDYSGN
>
> date = 2021.10.11
>
> version = 0.3

#### 1. 简介

​	基于python3.7环境，通过py原生库和leetcode上的一些习题构建的超小型py lib。

​	v 0.3更新了mcmc的两个常用算法：Metropolis-Hasting算法、Gibbs采样。

#### 2. 环境

* Python 3.7

#### 2. 结构

```tex
${project_name}/
|-- __init__.py
|-- __pycache__
|   `-- __init__.cpython-37.pyc
|-- main.py
|-- minipy
|   |-- __init__.py
|   |-- __pycache__
|   |   |-- __init__.cpython-37.pyc
|   |   `-- math.cpython-37.pyc
|   |-- geometry
|   |   |-- Hypersphere.py
|   |   |-- Point.py
|   |   |-- __init__.py
|   |   `-- __pycache__
|   |       |-- Hypersphere.cpython-37.pyc
|   |       |-- Point.cpython-37.pyc
|   |       `-- __init__.cpython-37.pyc
|   |-- graph
|   |   |-- __init__.py
|   |   |-- __pycache__
|   |   |   |-- __init__.cpython-37.pyc
|   |   |   `-- graph.cpython-37.pyc
|   |   `-- graph.py
|   |-- list
|   |   |-- __init__.py
|   |   |-- __pycache__
|   |   |   |-- __init__.cpython-37.pyc
|   |   |   `-- numList.cpython-37.pyc
|   |   `-- numList.py
|   |-- math.py
|   `-- string
|       |-- SingleString.py
|       |-- __init__.py
|       `-- __pycache__
|           |-- SingleString.cpython-37.pyc
|           `-- __init__.cpython-37.pyc
|-- setup.py
`-- test_py
    |-- __init__.py
    |-- __pycache__
    |   |-- __init__.cpython-37.pyc
    |   |-- test_geometry.cpython-37-pytest-5.4.1.pyc
    |   |-- test_graph.cpython-37-pytest-5.4.1.pyc
    |   |-- test_list.cpython-37-pytest-5.4.1.pyc
    |   `-- test_string.cpython-37-pytest-5.4.1.pyc
    |-- test_geometry.py
    |-- test_graph.py
    |-- test_list.py
    `-- test_string.py
```

#### 3. 测试

需提前安装pytest。基于pytest的简单测试，操作步骤：

```bash
cd leetcode/
py.test test_py/
```

Out:

![image-20211009202706499](./test-fig.png)

#### 4. 安装&卸载

install:

```bash
cd leetcode/
pip install dist/minipy-0.1.tar.gz
```

uninstall:

```
pip uninstall minipy
```

#### 5. 使用

An simple example：

```python
import minipy as py

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    adj = [
        [0, 2, 6, 4],
        [float("inf"), 0, 3, float("inf")],
        [7, float("inf"), 0, 1],
        [5, float("inf"), 12, 0]
    ]
    g = py.graph(adj)
    g.print_adjacency()
    gg = py.shortestPathClass(g)
    print(gg.shortestPath(1, 0))
    print(gg.shortestCost(1, 0))
    print()

    numList1 = py.numList([])
    numList2 = py.numList([1, 1, 1, 1, 1])
    numList3 = py.numList([1, 2, 3, 4, 5])
    numList4 = py.numList([5, 1, 3, 2, 4])
    print(numList1.findMiddleIndex())
    print(numList1.minimumDifference(2))
    print(numList1.insertionSort())
    print(numList1.mergeSort())
    print(numList2.findMiddleIndex())
    print(numList2.minimumDifference(2))
    print(numList2.insertionSort())
    print(numList2.mergeSort())
    print(numList3.findMiddleIndex())
    print(numList3.minimumDifference(2))
    print(numList3.insertionSort())
    print(numList3.mergeSort())
    print(numList4.findMiddleIndex())
    print(numList4.minimumDifference(2))
    print(numList4.insertionSort())
    print(numList4.mergeSort())
    print()

    s = ""
    ss = py.SingleString(s)
    print('max power is', ss.maxPower())
    print()

    point1 = tuple([1, 2])
    point2 = tuple([-2, -2])
    p1 = py.Point2D(point1)
    p2 = py.Point2D(point2)
    print("p1 coordinate is", p1.coordinate)
    print("p2 coordinate is", p2.coordinate)
    print("Distance between p1 and p2 is", py.distance(p1, p2))
```

Out：

```tex
Graph:
0	2	6	4	
∞	0	3	∞	
7	∞	0	1	
5	∞	12	0	
[1, 2, 3, 0]
9

-1
-1
[]
[]
2
0
[1, 1, 1, 1, 1]
[1, 1, 1, 1, 1]
-1
1
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
2
1
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]

max power is 0

p1 coordinate is (1, 2)
p2 coordinate is (-2, -2)
Distance between p1 and p2 is 5.0

```

