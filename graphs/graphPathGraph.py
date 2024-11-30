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
    updated.extend(visited)
    for edge in visited:
      ans[edge].extend(visited)

  return ans



      
