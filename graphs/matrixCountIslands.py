'''
/**
 * Given a 2D binary matrix, find the number of islands. An island is surrounded by water
 * and is formed by connecting adjacent lands horizontally or vertically. You may assume
 * all four edges of the matrix are surrounded by water.
 *
 * For example, the matrix below contains 4 islands:
 * [
 *   [1, 1, 0, 0, 0],
 *   [0, 1, 0, 0, 1],
 *   [0, 0, 0, 1, 1],
 *   [1, 0, 0, 0, 0],
 *   [1, 0, 1, 1, 1]
 * ]
 *
 */
function matrixCountIslands(matrix) {
  // Your code goes here.
}

module.exports = {
  matrixCountIslands,
}
'''
def matrix_count_islands(matrix):
  if not matrix or not matrix[0]:
    return 0

  visited = set()
  n, m = len(matrix[0]), len(matrix)
  def in_bounds(pos):
    x, y = pos
    return 0 <= x < n and 0 <= y < m
  
  def helper(pos):
    if not in_bounds(pos):
      return
    if pos in visited:
      return
    visited.add(pos)
    x, y = pos
    if matrix[y][x] == 0:
      return
    for adj in [(x+1,y), (x-1, y), (x,y-1), (x,y+1)]:
      helper(adj)

  ans = 0
  for j in range(m):
    for i in range(n):
      if (i, j) in visited:
        continue
      if matrix[j][i] == 1:
        ans += 1
        helper((i, j))
      visited.add((i, j))
  return ans

t1 =  [
   [1, 1, 0, 0, 0],
   [0, 1, 0, 0, 1],
   [0, 0, 0, 1, 1],
   [1, 0, 0, 0, 0],
   [1, 0, 1, 1, 1]
 ]
print(matrix_count_islands(t1))