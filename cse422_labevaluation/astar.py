# Student ID:
# Name: 

#INPUTS
graph = {'A': {'B': 75, 'C': 118, 'E': 140},
         'B': {'A': 75},
         'C': {'A': 118,'D': 111},
         'D': {'C': 111},
         'E': {'A': 140, 'G': 80, 'F': 99},
         'F': {'E': 99, 'I': 211},
         'G': {'E':80, 'H': 97},
         'H': {'G': 97, 'I': 101}}
heuristics = {'A': 366, 'B': 374, 'C': 329, 'D': 244, 'E': 253, 'F': 178, 'G': 193, 'H': 98, 'I': 0}


#Main Function
import heapq
def A_star_search(graph, heuristics, start, goal):
  open = [] #priority queue
  visited = []

  heapq.heappush(open, (0 + heuristics[start], 0, start, [start]))

  while open:
    fn, gn, current, path = heapq.heappop(open)
    if current in visited:
      continue
    visited.append(current)

    if current == goal:
      return path, gn
 
    if current in graph:
        for neigh, cost in graph[current].items():
            if neigh not in visited:
                gnew = gn+ cost
                fnew= gnew+ heuristics[current]
                heapq.heappush(open,(fnew ,gnew, neigh, path+[neigh]))
                              
  return None, None

#Driver Code
path, cost = A_star_search(graph, heuristics, 'A', 'I')
print(path, cost) #This will print ['A', 'E', 'G', 'H', 'I'] 418