'''
/**
 * Given a graph, represented as an adjacency list, iterate through it breadth-first
 * and call the callback for each node.
 */
function graphBFS(graph, startNode, callback) {
  let queue = [startNode];
  let visited = new Set();

  while (queue.length > 0) {
    let node = queue.shift();
    if (!visited.has(node)) {
      visited.add(node);

      if (typeof callback === 'function') {
        callback(node);
      }

      queue.push(...graph[node]);
    }
  }
}

module.exports = {
  graphBFS,
}

'''
from collections import deque
def graphBFS(graph, start, callback):
  queue = deque()
  visited = set()
  if start:
    visited.add(start)
    queue.append(start)

  while queue:
    current = queue.popleft()
    callback(current)
    for neighbor in graph[current]:
      if neighbor not in visited:
        queue.append(neighbor)
        visited.add(neighbor)

  

  
g = {
   1: [2, 3, 4],
   2: [1, 5],
   3: [1, 4],
   4: [1, 3, 5],
   5: [2, 4]
}

graphBFS(g, 1, lambda x: print(x, g[x]))