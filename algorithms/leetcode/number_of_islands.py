class Solution(object):
    def numIslands(self, grid):
        # The question itself does not involve a actual graph data structure (i.e. grid). But it can be treated a graph.
        # Loop over every single cell and whenever land on a cell that is marked as 1:
        # * do a dfs on all the adjacent cells and mark them as visited
        # * increment the number of islands count by 1
