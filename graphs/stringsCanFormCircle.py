'''
/**
 * Given an array of strings, write a function to check if the strings can be chained
 * to form a circle. A string X can be chained together with another string Y if the
 * last character of X is the same as the first character of Y.
 *
 * For example, ["bear", "radish"] can be chained because the last letter of "bear" is
 * 'r' and the first letter of "radish" is also 'r'. This function should return true
 * if all the strings in the array can be chained in such a way that they form a circle.
 */
function stringsCanFormCircle(strings) {
  // Your code goes here.
}

module.exports = {
  stringsCanFormCircle,
}
'''
from collections import deque

def can_form_circle(strings):
  strings = [string for string in strings if string]
  if not strings:
    return False

  adj = {}
  for string in strings:
    if string[0] not in adj:
      adj[string[0]] = []
    adj[string[0]].append(string[-1])

  visited = set()
  queue = deque()
  seen_cycle = False
  if strings[0]:
    queue.append(strings[0][0])
    visited.add(strings[0][0])
  
  while queue:
    cur = queue.popleft()
    if cur not in adj:
      continue
    for edge in adj[cur]:
        if edge in visited:
          seen_cycle = True
        else:
          queue.append(edge)
          visited.add(edge)

  # if "all the strings in the array can be chained".
  # it is not necessarily clear to me whether the question is asking:
  #    a) each string must be visited exactly once before a cycle is found?
  #    b) each string must be visited at least once and a cycle must exist?
  #    c) a cycle must exist, but there is no requirement on which strings are visited?

  # if a, return len(strings) == len(visited) when the first edge in visited is in adj[cur] on line 39
  # if b, create a bool and mark it true when the first edge in visited is in adj[cur] on line 39, then return whether its true and len(strings) == len(visited)
  # if c, simply return seen_cycle on line 58.

  # I implemented b here.
  return seen_cycle and len(strings) == len(visited)


print(can_form_circle(["ab", "bc", "ca"]))
print(can_form_circle(["ab", "bc", "cb"]))
print(can_form_circle(["ab", "bc", "cz"]))
print(can_form_circle(["ab", "bc", "d"]))
print(can_form_circle(["d"]))