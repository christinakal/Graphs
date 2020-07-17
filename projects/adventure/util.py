class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


# Find the opposite direction

def opp_dir(direction):
    if direction == 'n':
        return 's'
    elif direction == 's':
        return 'n'
    elif direction == 'w':
        return 'e'
    elif direction == 'e':
        return 'w'
    else:
        print('===== An unexpected error has occurred with opp_dir(). =====')


def bfs(self, starting_vertex, destination_vertex):
    """
    Return a list containing the shortest path from
    starting_vertex to destination_vertex in
    breath-first order.
    """
        # create a queue to hold vertices to traverse
    queue = Queue()

    # initialize queue with starting vertex
    queue.enqueue(starting_vertex)

    # use a dictionary to keep track of visited vertices and their path from the starting node
    paths_to_vertices = dict()
    paths_to_vertices[starting_vertex] = []

    # use a set to keep track of visited vertices
    visited_nodes = set()

    while queue.size() > 0:

        # get next vertex in line
        current_vertex = queue.dequeue()

        # process current vertex if it hasn't been visited yet
        if current_vertex not in visited_nodes:

            # mark current vertex as visited and store its path at the same time
            visited_nodes.add(current_vertex)
            
            # inspect all the neighbors of the current vertex
            for neighbor in self.get_neighbors(current_vertex):

                # if the target vertex is one of the neighbors, the search is done
                # right now paths_to_vertices[current_vertex] only contains all the vertices up to and including the parent vertex
                # to return the full path, add both the current vertex and the target vertex first.
                if neighbor == destination_vertex:
                    final_path = paths_to_vertices[current_vertex][:]
                    final_path.append(current_vertex)
                    final_path.append(neighbor)
                    return final_path

                # add all the other neighbors to the queue
                queue.enqueue(neighbor)

                # store a copy of the current path for each of the neighbors
                # take the path leading to current_vertex and add current_vertex to it
                # make a copy in order to not modify the original
                copy_of_path_to_parent = paths_to_vertices[current_vertex][:]
                copy_of_path_to_parent.append(current_vertex)

                # store path in dictionary
                paths_to_vertices[neighbor] = copy_of_path_to_parent
    
    # target not found
    print("Vertex", destination_vertex, "was not found.")
    return