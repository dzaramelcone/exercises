'''
/**
 * Given a graph, represented as an adjacency list, return its path graph.
 *
 * The path graph of a graph G has the same vertexes, but has (u, v) as an
 * edge if there's a path from u to v in the original graph.
 *
 * See: https://en.wikipedia.org/wiki/Path_graph
 */
function graphPathGraph(graph) {

}

module.exports = {
  graphPathGraph,
}
'''

def path_graph(graph):
  visited = set()
  updated = set()
  ans = {v:[] for v in graph}

  def helper(node):
    if node in visited:
      return
    visited.add(node)
    for edge in graph[node]:
      helper(edge)

  for v in graph:
    if v in updated:
      continue
    visited.clear()
    helper(v)
    updated.update(visited)
    for edge in visited:
      # This works fine for undirected graphs but directed graphs can end up with duplicates.
      # if directed, you need to create sets with this approach and convert them to lists if desired
      # i wonder if there is a way to neatly pull it off without sets for directed graphs..
      ans[edge].extend([x for x in visited if x != edge])

  return ans



      
g = {
   1: [2, 3, 4],
   2: [1, 5],
   3: [1, 4],
   4: [1, 3, 5],
   5: [2, 4],
   6: []
}
print(path_graph(g))

g = {
   1: [2, 3, 4],
   2: [1, 5],
   3: [1, 4],
   4: [1, 3, 5],
   5: [2, 4],
   6: [1]
}
print(path_graph(g))