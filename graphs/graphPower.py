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
  updated = set()
  ans = {v:[] for v in graph}
  for v in graph:
    if v in updated:
      continue
    dist = 0
    visited.clear()
    queue.append(v)
    while queue:
      size = len(queue)
      if dist > k:
        break
      for _ in range(size):
        cur = queue.popleft()
        visited.add(edge)
        for edge in graph[cur]:
          if edge not in visited:
            queue.append(edge)
      dist += 1
    
    queue.clear()
    updated.extend(visited)
    for v in visited:
      ans[v].extend(visited)

  return ans

