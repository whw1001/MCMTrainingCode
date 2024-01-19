import numpy as np
from collections import defaultdict
import pathSearch
import simCaculator

#   顶点集和边(含权重信息)集
V = {1, 2, 3, 4, 5, 6, 7, 8, 9}
E = {
    (1, 2): 1, (1, 4): 4, (2, 3): 1, (2, 5): 1, (3, 6): 1, (4, 5): 1, (4, 7): 1, (5, 4): 3,
    (5, 6): 3, (5, 8): 1, (6, 5): 1, (6, 9): 1, (7, 8): 1, (8, 7): 1, (8, 9): 1, (9, 8): 1,
}

#   题目所给的有人走过的路线
historical_paths = {
    (1, 7): [
        [(1, 2), (2, 5), (5, 4), (4, 7)],
        [(1, 2), (2, 5), (5, 8), (8, 7)]
    ],
    (1, 9): [
        [(1, 2), (2, 5), (5, 6), (6, 9)],
        [(1, 2), (2, 3), (3, 6), (6, 5), (5, 8), (8, 9)]
    ]
}

#   创建邻接矩阵和邻接表
adj_matrix = np.zeros((len(V), len(V)))
adj_list = defaultdict(list)

for edge, weight in E.items():
    adj_matrix[edge[0] - 1, edge[1] - 1] = weight
    start, end = edge
    adj_list[start].append((end, weight))

#   计算当前图的SIM
SIM = simCaculator.caculateSIM(adj_list, adj_matrix, historical_paths)
print(SIM)
