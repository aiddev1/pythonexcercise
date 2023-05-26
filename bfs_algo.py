from collections import deque

def bfs(start , goal , neighbor_func):
    visited = set()
    queue = deque([(start,[start])])
    while queue:
        node , path = queue.popleft()
        if node == goal:
            return path
        visited.add(node)
        for nighbor in neighbor_func(node):
            if nighbor not in visited:
                queue.append((nighbor,path+[nighbor]))
    return None