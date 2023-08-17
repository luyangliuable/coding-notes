import sys
import math
sys.path.append("/Users/rubber/University-notes/FIT2004/directed-graph/")
import undirected_graph
import directed_graph


graph1 = undirected_graph.adjacency_matrix(5)

matrix1 = [[None, 1, 1, None, None, None, None, None],
           [1, None, None, None, 1, 1, None, None],
           [1, None, None, 1, None, None, None, None],
           [None, None, 1, None, None, None, None, None],
           [None, None, None, None, None, None, None, 1],
           [None, 1, None, None, None, None, 1, None],
           [None, None, None, None, 1, 1, None, 1],
           [None, None, None, None, 1, None, 1, None]]

graph1.define_matrix(matrix1)


graph2 = undirected_graph.adjacency_matrix(5)
matrix2 = [[None, 1, None, None, 1],
           [1, None, 1, 1, 1],
           [None, 1, None, 1, None],
           [None, 1, 1, None, 1],
           [1, 1, None, 1, None]]


graph2.define_matrix(matrix2)
print(graph2.get_matrix())


graph3 = directed_graph.adjacency_matrix(5)
matrix3 = [[None, 1, None, None, 1],
           [1, None, 1, 1, 1],
           [None, 1, None, 1, None],
           [None, 1, 1, None, 1],
           [1, 1, None, 1, None]]

graph2.define_matrix(matrix2)
print(graph2.get_matrix())
