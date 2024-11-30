'''
/**
 * Given a graph G, represented as an adjacency list, and a non-negative integer k
 * calculate the kth graph power of G, denoted G^k.
 *
 * See: https://en.wikipedia.org/wiki/Graph_power
 *
 * G^k has the same vertexes as G, but has an edge (u,v) if there's a path no
 * longer than k from u to v.
 */
function graphPower(graph, k) {

}

module.exports = {
  graphPower,
}
'''

from collections import deque
def graph_power(graph, k):
  queue = deque()
  visited = set()
  ans = {v:[] for v in graph}
  for v in graph:
    dist = 0
    visited.clear()
    queue.append(v)
    while queue:
      size = len(queue)
      if dist >= k:
        break
      for _ in range(size):
        cur = queue.popleft()
        for edge in graph[cur]:
          if edge not in visited:
            queue.append(edge)
            visited.add(edge)
      dist += 1
    queue.clear()
    ans[v].extend(visited)

  return ans

g = {
   1: [2, 3, 4],
   2: [1, 5],
   3: [1, 4],
   4: [1, 3, 5],
   5: [2, 4, 6],
   6: [5, 7],
   7: [6]

}
print(graph_power(g, 0))
print(graph_power(g, 1))
print(graph_power(g, 2))
print(graph_power(g, 3))