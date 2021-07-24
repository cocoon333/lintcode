"""
178. Graph Valid Tree

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
Example

Example 1:

Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.

Example 2:

Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.

Notice

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        tree = {}
        for edge in edges:
            if edge[0] in tree:
                tree[edge[0]].append(edge[1])
            else:
                tree[edge[0]] = [edge[1]]
            if edge[1] in tree:
                tree[edge[1]].append(edge[0])
            else:
                tree[edge[1]] = [edge[0]]
        for i in range(n):
            path = set()
            if i not in tree:
                return False
            while j in tree[i]:



        return True

if __name__ == "__main__":
    s = Solution()
    assert(s.validTree(5, [[4, 3], [4, 2], [2, 1], [2, 0]]))
    assert(s.validTree(5, [[4, 3], [3, 2], [2, 1], [1, 0]]))
    assert(s.validTree(8, [[0,1],[1,2],[3,2],[4,3],[4,5],[5,6],[6,7]]))
    assert(s.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
    assert(not s.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
