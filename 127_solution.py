"""
127. Topological Sorting
中文
English

Given an directed graph, a topological order of the graph nodes is defined as follow:

    For each directed edge A -> B in graph, A must before B in the order list.
    The first node in the order can be any node in the graph with no nodes direct to it.

Find any topological order for the given graph.
Example

For graph as follow:

picture

The topological order can be:

[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...

Challenge

Can you do it in both BFS and DFS?
Clarification

Learn more about representation of graphs
Notice

You can assume that there is at least one topological order in the graph.
"""
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
    def __str__(self):
        return str(self.label)


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        res = []
        head_nodes = self.getHead(graph)
        for head in head_nodes:
            temp = []
            print("head", head)
            self.helper(head, set(), temp)
            res.extend(temp)
        return res

    def helper(self, node, cache, res):
        temp = []
        if node not in cache:
            res.append(node.label)
            cache.add(node)
        for neighbor in node.neighbors:
            if neighbor not in cache:
                cache.add(neighbor)
                res.append(neighbor.label)
                temp.append(neighbor)

        for node in temp:
            self.helper(node, cache, res)

    def getHead(self, graph):
        res = []
        non_head_nodes = set() 
        for node in graph:
            for neighbor in node.neighbors:
                non_head_nodes.add(neighbor)
        for node in graph:
            if node not in non_head_nodes:
                res.append(node)
        return res

if __name__ == "__main__":
    s = Solution()
    n1 = DirectedGraphNode(0)
    n2 = DirectedGraphNode(1)
    n3 = DirectedGraphNode(2)
    n4 = DirectedGraphNode(3)
    n5 = DirectedGraphNode(4)
    n1.neighbors = [n2, n3, n4, n5]
    n2.neighbors = [n4, n5]
    n3.neighbors = [n2, n5]
    n4.neighbors = [n5]
    print(s.topSort([n5, n2, n1, n3, n4]))
"""
    n6 = DirectedGraphNode(5)
    n1.neighbors = [n2, n3, n4]
    n2.neighbors = [n5]
    n3.neighbors = [n5, n6]
    n4.neighbors = [n5, n6]
    print(s.topSort([n1, n2, n3, n4, n5, n6]))
    """
