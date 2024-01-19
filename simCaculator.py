import numpy as np
import pathSearch

#   计算SIM
def caculateSIM(adj_list, adj_matrix, paths):
    total_paths = 0
    L = 0
    f = 0
    SIM = 0

    for start_end, paths in paths.items():
        shortest_path, D = pathSearch.aStarSearch(adj_list, start_end[0], start_end[1], 0)
        for path in paths:
            total_paths += 1
            L = 0
            for edge in path:
                L += adj_matrix[edge[0] - 1, edge[1] - 1]

            if L == D:
                f = 1
            else:
                f = 0
            SIM += f


    SIM = SIM / total_paths
    return SIM
