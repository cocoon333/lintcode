"""
137. Clone Graph
中文
English

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors. Nodes are labeled uniquely.

You need to return a deep copied graph, which has the same structure as the original graph, and any changes to the new graph will not have any effect on the original graph.
Example

Example1

Input:
{1,2,4#2,1,4#4,1,2}
Output: 
{1,2,4#2,1,4#4,1,2}
Explanation:
1------2  
 \     |  
  \    |  
   \   |  
    \  |  
      4   

Clarification

How we serialize an undirected graph: http://www.lintcode.com/help/graph/
Notice

You need return the node with the same label as the input node.
"""

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        if not node:
            return

        return self.helper(node, {})

    def helper(self, node, cache):
        if node.label in cache:
            return cache[node.label]
        new_node = UndirectedGraphNode(node.label)
        cache[node.label] = new_node
        for n in node.neighbors:
            if n.label not in cache:
                new_node.neighbors.append(self.helper(n, cache))
            else:
                new_node.neighbors.append(cache[n.label])
        return new_node
