'''

/**
 * Simulate the flood fill algorithm used in graphic applications like MS-Paint. Given a 2D screen
 * represented by an MxN array where each number represents a different color, a start pixel, and
 * a new color, replace the color of the given pixel and all adjacent same colored pixels with the
 * new color.
 *
 * For example, on a screen with the following configuration, and start pixel (0, 1) and new color 3,
 * the screen should change as follows:
 * Initial Screen:
 * [
 *   [1, 1, 0],
 *   [1, 2, 1],
 *   [0, 1, 1]
 * ]
 * Resulting Screen:
 * [
 *   [3, 3, 0],
 *   [3, 2, 1],
 *   [0, 1, 1]
 * ]
 */
function floodFill(screen, startX, startY, newColor) {
  // Your code goes here.
}

module.exports = {
  floodFill,
}
'''
from collections import deque
def floodfill(screen, startX, startY, color):
  n, m = len(screen), len(screen[0])
  
  target = screen[startX][startY]

  queue = deque()
  visited = set()

  def is_neighbor(cur):
     u, v = cur
     return 0 <= u < n and 0 <= v < m and screen[u][v] == target
  queue.append((startX,startY))
  while queue:
    x, y = queue.popleft()
    for adj in [(x+1, y), (x-1,y), (x,y+1), (x,y-1)]:
      if adj not in visited and is_neighbor(adj):
        queue.append(adj)
        visited.add(adj)
    screen[x][y] = color
  return screen

print(floodfill([[1,1,1],[1,0,0],[1,1,2]], 1, 1, 3))
print(floodfill([[1,1,1],[1,0,0],[1,1,2]], 0, 0, 3))
print(floodfill([[1,1,1],[1,0,0],[1,1,2]], 2, 2, 3))