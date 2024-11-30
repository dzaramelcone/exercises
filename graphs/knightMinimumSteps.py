'''
/**
 * Given a square chessboard of N x N size, find the minimum number of steps a Knight will take
 * to reach from a given starting position to a target position. The positions are given as
 * (x, y) coordinates on the chessboard.
 */
function knightMinimumSteps(chessboardSize, startPos, targetPos) {
  // Your code goes here.
}

module.exports = {
  knightMinimumSteps,
}
'''
from collections import deque
def knight_min_steps(size, startPos, targetPos):
  def in_bounds(pos):
    x, y = pos
    return 0 <= x < size and 0 <= y <= size
  def get_moves(pos):
    x, y = pos
    return [
        (x+1,y+2), (x+1,y-2),
        (x-1,y+2), (x-1,y-2),
        (x+2,y+1), (x+2,y-1),
        (x-2,y+1), (x-2,y-1)]

  queue = deque()
  visited = set()
  if startPos:
    queue.append(startPos)
    visited.add(startPos)

  dist = 0
  while queue:
    size = len(queue)
    for _ in range(size):
      cur = queue.popleft()
        # a slight optimization could be to return this in the get_moves loop instead.
        # but if the start is the target then we need to check for that.
      if cur == targetPos:
        return dist
      for loc in get_moves(cur):
        if loc in visited or not in_bounds(loc):
          continue
        queue.append(loc)
        visited.add(loc)
    dist += 1
  return -1



