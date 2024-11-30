'''
/**
 * Given a graph G, represented as an adjacency list, return its line graph Line(G).
 *
 * See: https://en.wikipedia.org/wiki/Line_graph
 *
 * To form the line graph, we turn edges in to vertexes and vice versa. Every edge
 * in G becomes a vertex in Line(G).
 *
 * If e1 and e2 are edges in G then there's an edge (e1, e2) in Line(G) if e1 and e2
 * share a vertex in the original graph.
 */
function graphLineGraph(graph) {

}

module.exports = {
  graphLineGraph
}
'''

from pprint import pprint

def line(graph):
  ans = {}
  for v, edges in graph.items():
    new_vertices = []
    for e in edges:
      new_vert = (v, e)
      # I think if its nondirectional then uncomment this:
      if (e, v) in ans:
         new_vert = (e, v)
      new_vertices.append(new_vert)

    for new_vert in new_vertices:
        if new_vert not in ans:
           ans[new_vert] = set()
        ans[new_vert].update(new_vertices)
  for p, q in ans.items():
      q.remove(p)
  return ans
  
g = {
   1: [2, 3, 4],
   2: [1, 5],
   3: [1, 4],
   4: [1, 3, 5],
   5: [2, 4]
}
pprint(g)
# Not even confident I understand this concept enough to make more tests beyond the example on wiki.
# Will need to revisit tomorrow.
pprint(line(g))
