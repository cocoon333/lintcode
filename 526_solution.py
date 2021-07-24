"""
526. Load Balancer
中文
English

Implement a load balancer for web servers. It provide the following functionality:

    Add a new server to the cluster => add(server_id).
    Remove a bad server from the cluster => remove(server_id).
    Pick a server in the cluster randomly with equal probability => pick().

At beginning, the cluster is empty. When pick() is called you need to randomly return a server_id in the cluster.
Example

Example 1:

Input:
  add(1)
  add(2)
  add(3)
  pick()
  pick()
  pick()
  pick()
  remove(1)
  pick()
  pick()
  pick()
Output:
  1
  2
  1
  3
  2
  3
  3
Explanation: The return value of pick() is random, it can be either 2 3 3 1 3 2 2 or other.
"""

import random
class LoadBalancer:
    def __init__(self):
        self.servers = {}

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        self.servers[server_id] = 0

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        del self.servers[server_id]

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        return list(self.servers.keys())[random.randint(0, len(self.servers)-1)]

if __name__ == "__main__":
    lb = LoadBalancer()
    lb.add(1)
    print(lb.pick())
    lb.remove(1)
