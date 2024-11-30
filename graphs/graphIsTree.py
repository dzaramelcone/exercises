'''

/**
 * Given a directed graph, determine whether it's a tree or not. A directed graph is a tree if
 * the following two conditions hold:
 *
 * 1. There's exactly one vertex from which every other vertex is reachable
 * 2. No vertex is reachable in two different ways, i.e., via two different paths
 */
function graphIsTree(graph) {

}
'''


def transpose_graph(graph):
  ans = { v:[] for v in graph}
  for v, edges in graph.items():
    for edge in edges:
      ans[edge].append(v)
  return ans

def graph_is_tree(graph):
  source = None
  for v, e in transpose_graph(graph).items():
    if not e:
      if source:
        return False
      source = v

  visited = set()
  for v, edges in graph.items():
    for edge in edges:
      if edge in visited:
        return False
      visited.add(edge)
    
  return True



t1 = {'A': ['C'], 'B': ['A'], 'C': ['A', 'B']}
print(graph_is_tree(t1))
t2 = {'A': ['B'], 'B': ['C'], 'C': []}
print(graph_is_tree(t2))
  