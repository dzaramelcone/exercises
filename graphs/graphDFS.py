'''
/**
 * Given a graph and a starting node, perform a depth-first traversal of the graph.
 * You can supply both a pre-order and post-order callback.
 */
function graphDFSFromNode(graph, startNode, { preOrderCallback, postOrderCallback }, visited = new Set()) {
  if (visited.has(startNode)) {
    return;
  }

  visited.add(startNode);

  if (typeof preOrderCallback === 'function') {
    preOrderCallback(startNode);
  }


  for (let neighbor of graph[startNode]) {
    graphDFSFromNode(graph, neighbor, { preOrderCallback, postOrderCallback }, visited);
  }

  if (typeof postOrderCallback === 'function') {
    postOrderCallback(startNode);
  }
}

/**
 * Perform a depth-first traversal of the given graph.
 * You can supply both a pre-order and post-order callback.
 */
function graphDFS(graph, { preOrderCallback, postOrderCallback }) {
  let visited = new Set();

  for (let node of Object.keys(graph)) {
    graphDFSFromNode(graph, node, { preOrderCallback, postOrderCallback }, visited);
  }
}

module.exports = {
  graphDFSFromNode,
  graphDFS,
}
'''

def dfs(graph, start, preoderCallback, postorderCallback):
  visited = set()
  def helper(node):
    if node in visited:
      return
    visited.add(node)
    preoderCallback()
    for neighbor in graph[node]:
      helper(neighbor)
    postorderCallback()


def dfs(graph, preoderCallback, postorderCallback):
  visited = set()
  def helper(node):
    if node in visited:
      return
    visited.add(node)
    preoderCallback()
    for neighbor in graph[node]:
      helper(neighbor)
    postorderCallback()

  for node in graph:
    helper(node)
