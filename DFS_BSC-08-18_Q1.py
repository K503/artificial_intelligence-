# BSC-08-18 KENNEDY NKHATA
graph = {
    "S": ["C", "A"],
    "A": ["S", "B", "C"],
    "B": ["D", "E", "A"],
    "C": ["S", "D", "A"],
    "D": ["E", "B", "C"],
    "E": ["B", "D"],
}

def dfss(graph, start, target, path, visited = set()):
    path.append(start)
    visited.add(start)
    if start == target:
        return path
    for neighbour in graph[start]:
        if neighbour not in visited:
            result = dfss(graph, neighbour, target, path, visited)
            if result is not None:
                return result

        #print(visited)
        #path.pop()
        #print(path)

    return None

traversal_path = []
start = input("enter the start node: ").upper()
goal = input("enter the goal node: ").upper()
traversal_path = dfss(graph, start, goal, traversal_path)
print("The path for the node you have searched for is; ")
print(traversal_path)


