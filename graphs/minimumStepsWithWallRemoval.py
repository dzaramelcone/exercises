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
from collections import deque

def minimum_steps_with_wall_removal(matrix, removal):
  n, m = len(matrix[0]), len(matrix)
  ex, ey = n-1, m-1
  dirs = [(1,0), (0,1), (-1,0), (0,-1)]
  queue = deque()
  visited = set()

  if removal >= m + n - 3:
      return m + n - 2

  queue.append((0,0,removal))
  dist = 0
  while queue:
    sz = len(queue)
    for _ in range(sz):
      u, v, w = queue.popleft()
      if u == ex and v == ey:
        return dist
      for x, y in dirs:
        p, q = u+x, v+y
        if not (0 <= p < n and 0 <= q < m):
          continue
        if (r := w - matrix[q][p]) < 0:
          continue
        if (loc := (p, q, r)) in visited:
          continue
        visited.add(loc)
        queue.append(loc)
    dist += 1
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
