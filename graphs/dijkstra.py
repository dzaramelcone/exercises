'''
/**
 * Implement Dijkstra's algorithm to find the shortest path between two nodes in a weighted graph.
 * The graph is represented as an adjacency list where each entry is a node and an array of
 * objects, each with a 'node' and 'cost' indicating the weight of the edge.
 *
 * See: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
 */
function dijkstra(graph, startNode, endNode) {
  // Your code goes here.
}

module.exports = {
  dijkstra,
}
'''
import heapq

class Node:
  def __init__(self, value, dist, prev):
    self.value = value
    self.dist = dist
    self.prev = prev

def dijkstra(graph, start, end):
  pq = []
  visited = {}

  heapq.heappush(pq, (0, Node(start, 0, None)))

  def get_neighbors(node):
    return [Node(n, node.dist+c, node) for n, c in graph[node.value] if n not in visited or visited[n].dist > node.dist+c]

  while pq:
    dist, current = heapq.heappop(pq)
    for node in get_neighbors(current):
      heapq.heappush(pq, (node.dist, node))
      visited[node.value] = node
  
  if end not in visited:
    return None

  ans = []
  current = visited[end]
  length = current.dist
  while current:
    ans.append(current.value)
    current = current.prev

  return length, ans[::-1]
  
t1 = { 'A': [('B', 2), ('C', 11)], 'B': [('C', 5)], 'C': []}
print(dijkstra(t1, 'A', 'C'))

t2 = { 'A': [('B', 2)], 'B': [], 'C': []}
print(dijkstra(t2, 'A', 'C'))

t3 = { 'A': [('B', 2), ('C', 5)], 'B': [('A', 2), ('C', 5)], 'C': []}
print(dijkstra(t3, 'A', 'C'))
