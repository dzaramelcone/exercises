'''

let { graphBFS } = require('./graph-bfs');

/**
 * Given a graph, a starting node `startNode`, and an ending node `endNode`,
 * find the shortest path from `startNode` to `endNode`.
 */
function graphShortestPath(graph, startNode, endNode) {

}
'''
from collections import deque
class Node:
  def __init__(self, value, prev=None):
    self.value = value
    self.prev = prev

def graph_shortest_path(graph, start, end):
  queue = deque()
  visited = set()
  if start:
    queue.append(Node(start))
    visited.add(start)

  while queue and cur != end:
    cur = queue.popleft()

    for edge in graph[cur.value]:
      if edge in visited:
        continue
      queue.append(Node(edge, cur))
      visited.add(edge)

    ans = []
    while cur:
      ans.append(cur)
      cur = cur.prev
    return ans[::-1]
  
  