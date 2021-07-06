# from graph.util import Stack, Queue  # These may come in handy
class AncestorGraph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}  # This is our adjacency list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2
        """
        # Check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vertex not found")
    
    def get_parents(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None
        
        

        
    def get_dist_parent(self, starting_vertex):
        
        """
        Gets the distant parent
        
        """
        # Create a stack and push starting vertex
        #ss = Stack()
        ss = []
        ss.append([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        paths = []
        len_path=[]
        dist_parent = -1
        
        # While stack is not empty:
        while len(ss) > 0:
            # pop the last added vertex
            path = ss.pop(0)
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                paths.append(path)
                len_path.append(len(path))
                # mark as visited
                visited.add(path[-1])
                # push all neightbors if exists
                if self.get_parents(path[-1]) is not None:
                    for next_vert in self.get_parents(path[-1]):
                        new_path = list(path)
                        new_path.append(next_vert)
                        ss.append(new_path)
        
        parents=[]
        max_len = max(len_path)
        if max_len == 1:
            dist_parent = -1
        else:
            for path in paths:
                if(len(path) == max_len):
                    parents.append(path[-1])
            dist_parent = min(parents)
#         print(paths)
        return dist_parent
def earliest_ancestor(ancestors, starting_node):
    ag = AncestorGraph()
    for parent, child in ancestors:
        ag.add_vertex(parent)
        ag.add_vertex(child)
        
    for parent,child in ancestors:
        ag.add_edge(child,parent)
        
    return ag.get_dist_parent(starting_node)
   