from graph import Graph, Queue, Stack

def earliest_ancestor(ancestors, starting_node):
    # create a graph to represent the data
    family_tree = Graph()

    # take a list of all nodes used in the graph
    known_nodes = set()

    # create a dictionary to store paths to each node
    paths_to_ancestors = dict()

    for parent_child_pair in ancestors:
        parent, child = parent_child_pair

        if parent not in known_nodes:
            known_nodes.add(parent)
        
        if child not in known_nodes:
            known_nodes.add(child)

    # add each node to the graph
    # also initialize paths_to_ancestors
    for node in known_nodes:
        family_tree.add_vertex(node)
        paths_to_ancestors[node] = []

    # add edges to graph. Child nodes point to parent nodes.
    for parent_child_pair in ancestors:
        parent, child = parent_child_pair
        family_tree.add_edge(child, parent)

    # create a queue to hold vertices to traverse
    queue = Queue()

    # initialize queue with starting vertex
    queue.enqueue(starting_node)

    while queue.size() > 0:

        # get next vertex in line
        current_vertex = queue.dequeue()

        # find all parents to the starting node
        for parent in family_tree.get_neighbors(current_vertex):

            # update path from child to parent
            copy_of_path_from_child = paths_to_ancestors[current_vertex][:]
            copy_of_path_from_child.append(current_vertex)
            
            # store path in dictionary
            paths_to_ancestors[parent] = copy_of_path_from_child

            # add parent to queue for later processing
            queue.enqueue(parent)

        # no more children: add current vertex to end of path to finish the path
        final_path = paths_to_ancestors[current_vertex][:]
        final_path.append(current_vertex)
        paths_to_ancestors[current_vertex] = final_path

    # search for the longest path
    longest_path = []

    for node in paths_to_ancestors:

        current_path = paths_to_ancestors[node]

        # update longest path if a longer one is found
        if len(current_path) > len(longest_path):
            longest_path = current_path

    # if the length is 1, that means the node has no parents. Return -1.
    if len(longest_path) == 1:
        return -1

    # otherwise, return the last item in the path, which will be the furthest ancestor
    return longest_path[-1]
