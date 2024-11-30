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

  while queue:
    cur = queue.popleft()
    if cur.value == end:
      break
    for edge in graph[cur.value]:
      if edge in visited:
        continue
      queue.append(Node(edge, cur))
      visited.add(edge)

  if cur.value != end:
    return []

  ans = []
  
  while cur:
    ans.append(cur.value)
    cur = cur.prev
  return ans[::-1]
  
  
  
g = {
   1: [2, 3, 4],
   2: [1, 5],
   3: [1, 4],
   4: [1, 3, 5],
   5: [2, 4]
}

print(graph_shortest_path(g, 1, 5))
print(graph_shortest_path(g, 1, 4))
print(graph_shortest_path(g, 2, 3))