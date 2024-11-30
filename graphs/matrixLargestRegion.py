'''
/**
 * Given a 2D binary matrix where each cell contains either a '0' or a '1', with '1' representing
 * a filled cell, find the size of the largest region formed by connected filled cells.
 * Cells are considered connected if they are adjacent horizontally, vertically, or diagonally.
 *
 * For example, the matrix below:
 * [
 *   [1, 1, 0, 0],
 *   [0, 1, 1, 0],
 *   [0, 0, 1, 0],
 *   [1, 0, 0, 0]
 * ]
 * The largest region has 5 filled cells.
 */
function matrixLargestRegion(matrix) {
  // Your code goes here.
}

module.exports = {
  matrixLargestRegion,
}
'''



def matrix_largest_region(matrix):
  if not matrix or not matrix[0]:
    return 0

  visited = set()
  n, m = len(matrix[0]), len(matrix)
  def in_bounds(pos):
    x, y = pos
    return 0 <= x < n and 0 <= y < m
  
  def helper(pos):
    nonlocal size
    if not in_bounds(pos):
      return
    if pos in visited:
      return
    visited.add(pos)
    x, y = pos
    if matrix[y][x] == 0:
      return
    size += 1
    for adj in [(x+1,y), (x-1, y), (x,y-1), (x,y+1)]:
      helper(adj)

  ans = 0
  for j in range(m):
    for i in range(n):
      if (i, j) in visited:
        continue
      if matrix[j][i] == 1:
        size = 0
        helper((i, j))
        ans = max(size, ans)
      visited.add((i, j))
  return ans

t1 =  [
   [1, 1, 0, 0, 0],
   [0, 1, 0, 0, 1],
   [0, 0, 0, 1, 1],
   [1, 0, 0, 0, 1],
   [1, 1, 1, 1, 1]
 ]
print(matrix_largest_region(t1))