'''
/**
 * Given a 2D binary matrix of size N * M where '0' represents an empty space and '1' represents
 * a wall, determine the minimum number of steps required to travel from the top left corner (0, 0)
 * to the bottom right corner (N-1, M-1). You are allowed to remove up to K walls. If it is not
 * possible to reach the target, return -1.
 *
 * We'll call K the "removal budget".
 *
 * Example input:
 * matrix: [
 *   [0, 1, 0, 0, 0],
 *   [0, 1, 0, 1, 0],
 *   [0, 1, 0, 1, 0],
 *   [0, 1, 0, 1, 0],
 *   [0, 0, 0, 1, 0]
 * ],
 * k: 2
 * Output: 8 (minimum steps, including wall removals)
 */
function minimumStepsWithWallRemoval(matrix, removalBudget) {
  // Your code goes here.
}

module.exports = {
  minimumStepsWithWallRemoval,
}
'''

class Node:
  def __init__(self, pos, matrix, parent=None):
    self.pos = pos
    x, y = pos
    self.steps = parent.steps + 1 if parent else 0
    self.k = parent.k - matrix[y][x] if parent else 0
    self.distance = (len(matrix[0])-1-x) + (len(matrix)-1-y)

  def __lt__(self, other):
    if self.distance < other.distance:
      return True
    if self.distance + self.steps < other.distance + other.steps:
      return True
    if self.distance + self.steps + self.k < other.distance + other.steps + other.k:
      return True
    return self.pos > other.pos

import heapq

def minimum_steps_with_wall_removal(matrix, removal):
  n, m = len(matrix[0]), len(matrix)
  def in_bounds(pos):
    x, y = pos
    return 0 <= x < n and 0 <= y < m
  def get_adj(pos):
    x, y = pos
    return [(x+1,y), (x,y+1), (x-1,y), (x,y-1)]
  def get_neighbors(node):
    return [Node((u,v), matrix, node) for u, v in get_adj(node.pos) if in_bounds((u, v))]
  def get_distance(node):
    x, y = node.pos
    return 

  pq = []
  home = Node((0,0), matrix)
  home.k = removal
  heapq.heappush(pq, home)
  visited = set()
  while pq:
    cur = heapq.heappop(pq)
    if cur.pos == (n-1, m-1):
      return cur.steps
    for neighbor in get_neighbors(cur):
      if neighbor.k < 0:
        continue
      # worst case is now n*m*k memory to support this..
      # is there some better solution?
      # maybe some kinda percolation solution..

      # uhh, thought: could you just do bfs with this instead?
      grp = (neighbor.pos, neighbor.k)
      if grp in visited:
        continue
      visited.add(grp)
      heapq.heappush(pq, neighbor)
  return -1

map = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
  ]
print(minimum_steps_with_wall_removal(map, 2))
print(minimum_steps_with_wall_removal(map, 1))
print(minimum_steps_with_wall_removal(map, 0))

map = [
    [0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
  ]
print(minimum_steps_with_wall_removal(map, 0))
print(minimum_steps_with_wall_removal(map, 1))
print(minimum_steps_with_wall_removal(map, 2))
print(minimum_steps_with_wall_removal(map, 3))
print(minimum_steps_with_wall_removal(map, 4))
