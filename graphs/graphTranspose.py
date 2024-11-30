'''
/**
 * Given a directed graph, represented as an adjacency list, return its graph transpose
 * (aka opposite graph). This graph is formed by reversing the direction of all
 * the edges.
 *
 * See: https://en.wikipedia.org/wiki/Transpose_graph
 */
function graphTranspose(graph) {

}

module.exports = {
  graphTranspose,
}

'''


def transpose_graph(graph):
  ans = { v:[] for v in graph}
  for v, edges in graph.items():
    for edge in edges:
      ans[edge].append(v)
  return ans

t1 = {'A': ['B'], 'B': ['C'], 'C': ['A']}
t2 = {'A': ['B', 'C', 'D', 'E', 'F'], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [] }
print(transpose_graph(t1))
print(transpose_graph(t2))