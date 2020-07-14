"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph: 

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]



    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # STEPS
        # 1. Create a Queue
        # 2. enqueue our starting node
        # 3. make a set to track if we've been there before
        # 4. while our queue is not empty
        # 5. dequeue whatever's at the front of our line,, this is our current_node
        # 6. if we haven't visited this node 
        # 7. mark as visited
        # 8. get it's neighboors
        # 9. for each of the neighboors 
        # 10. add to the queue


        
        # create a queue
        queue = Queue()

        # initialize queue with starting node
        queue.enqueue(starting_vertex)

        # create a set to keep track of visited nodes
        visited = set()

        while queue.size() > 0:

            # get next node in line
            current_node = queue.dequeue()

            # process current node if it hasn't been visited yet
            if current_node not in visited:
                # TODO: print the current_node
                print(current_node)

                # mark current node as visited
                visited.add(current_node)

                # add all neighbors to queue
                for neighbor in self.get_neighbors(current_node):
                    queue.enqueue(neighbor)



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # STEPS
        # 1. Create a Stack
        # 2. push on our starting node
        # 3. make a set to track if we've been there before
        # 4. while our stack is not empty
        # 5. pop off whatever's on top, this is our current_node
        # 6. if we haven't visited this node 
        # 7. mark as visited
        # 8. get it's neighboors
        # 9. for each of the neighboors 
        # 10. add to the stack


        # create a stack
        stack = Stack()

        # initialize stack with starting node
        stack.push(starting_vertex)

        # create a set to keep track of visited nodes
        visited = set()
        
        while stack.size() > 0:

            # get next node in line
            current_node = stack.pop()

            # process current node if it hasn't been visited yet
            if current_node not in visited:
                print(current_node)

                # mark current node as visited
                visited.add(current_node)

                # add all neighbors to stack
                for neighbor in self.get_neighbors(current_node):
                    stack.push(neighbor)




    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        def dft_helper(starting_node):

            if starting_node not in visited:
                print(starting_node)

                # mark current node as visited
                visited.add(starting_node)

                # process all neighboors recursively
                for neighboor in self.get_neighbors(starting_node):
                    dft_helper(neighboor)
        
        visited = set()

        dft_helper(starting_node)




    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO




    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO




    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
