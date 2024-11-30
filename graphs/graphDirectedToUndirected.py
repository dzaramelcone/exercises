'''
/**
 * Given a directed graph, represented by an adjacency list, return an undirected graph
 * formed by "forgetting" the directions of the original edges.
 *
 * Do this by creating a new adjacency list where there's an edge in both directions
 * for every edge in the original graph.
 */

function graphDirectedToUndirected(graph) {

}

module.exports = {
  graphDirectToUndirected,
}
'''

def graph_dir_to_undir(graph):
  new_edges = set()
  for v, e in graph.items():
    for edge in e:
      new_edges.add((v, edge))
      new_edges.add((edge, v))

  ans = {}
  for a, b in new_edges:
    if a not in ans:
      ans[a] = []
    if b not in ans:
      ans[b] = []
    ans[a].append(b)
  return ans

t1 = {'A': ['C'], 'B': ['A'], 'C': ['A', 'B']}
print(graph_dir_to_undir(t1))
t2 = {'A': ['B'], 'B': ['C'], 'C': []}
print(graph_dir_to_undir(t2))