graph = {
    "S": {"A": 1, "C": 2},
    "A": {"B": 1},
    "B": {"D": 1, "E": 2},
    "C": {"D": 3, "A": 4},
    "D": {"E": 1},
    "E": {},
}


def dijkstra(data, start_node, end):
    node_paths = {}
    unvisited = data
    # predecessor set
    previous_node = {}
    # amount to equate to very long path
    infinity = 999999999
    # trace back the path to source ... optimal path
    track = []
    for node in unvisited:
        node_paths[node] = infinity
    node_paths[start_node] = 0

    while unvisited:
        min_path_node = None

        for node in unvisited:
            if min_path_node is None:
                min_path_node = node
            elif node_paths[node] < node_paths[min_path_node]:
                min_path_node = node

        path_options = data[min_path_node].items()


        for child_node, cost in path_options:
            if cost + node_paths[min_path_node] < node_paths[child_node]:
                node_paths[child_node] = cost + node_paths[min_path_node]
                previous_node[child_node] = min_path_node

        unvisited.pop(min_path_node)

    # tracing back
    current_node = end

    # error handling
    while current_node != start_node:
        try:
            track.insert(0, current_node)
            current_node = previous_node[current_node]

        except KeyError:
            print("path not found")
            break

    track.insert(0, start_node)

    if node_paths[end] != infinity:
        return node_paths[end], track


#

# user interaction

destination_node = input("Choose destination node ").upper()
start_node = input("Choose starting node: ").upper()

# formatting the return values of the traversal function
shortest_path, track = dijkstra(graph, start_node, destination_node)

print("The shortest path is")

for short_path in track:
    print(short_path)

print("the cost of the path between the nodes "+start_node +" and "+destination_node+" is " + str(shortest_path))
