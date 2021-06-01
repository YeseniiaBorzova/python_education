"""Module contains  class representing undirected unweighted graph"""


class Vertex:
    """Class that represent vertex of graph"""
    def __init__(self, name, connected_to=None):
        """Constructor"""
        if connected_to is None:
            connected_to = set()
        self.connected_to = set(connected_to)
        for vertex in connected_to:
            vertex.append_neighbour(self)
        self.name = name

    def __str__(self):
        """to string magic method"""
        s = ''
        if self.connected_to:
            for connection in self.connected_to:
                s += f"{self.name} -> {connection.get_name()} "
            return s
        return str(self.name)

    def get_name(self):
        """:return name of vertex"""
        return self.name

    def append_neighbour(self, neighbour):
        """add neighbour to the vertex"""
        self.connected_to.add(neighbour)
        neighbour.connected_to.add(self)

    def append_neighbours(self, neighbours_list):
        """add neighbours to the vertex"""
        for neighbour in neighbours_list:
            self.append_neighbour(neighbour)

    def delete_neighbour(self, neighbour_name):
        """delete neighbour from the vertex"""
        for neighbour in self.connected_to:
            if neighbour.name == neighbour_name:
                self.connected_to.remove(neighbour)
                return
        return "Not in neighbours list"

    def show_neighbours(self):
        """shows neighbours og the vertex"""
        if self.connected_to:
            s = ""
            for connection in self.connected_to:
                s += f"{connection.get_name()} "
            return s
        return "No neighbours"

    def get_neighbours(self):
        """:return neighbour-vertex objects"""
        if len(self.connected_to):
            return self.connected_to
        return None


class Graph:
    """Class representing undirected
    unweighted graph"""
    def __init__(self, name, vertices=None):
        """Constructor"""
        if vertices is None:
            vertices = set()
        self.vertices = set(vertices)
        self.name = name

    def __str__(self):
        """to string magic method"""
        s = ''
        for vertex in self.vertices:
            s += vertex.__str__()
            s += "\n"
        return s

    def add_vertex(self, vertex):
        """adds vertex too the graph"""
        if isinstance(vertex, Vertex):
            self.vertices.add(vertex)
            return
        raise TypeError('Is not vertex instance!')

    def add_vertices(self, vertices_list):
        """adds vertices too the graph"""
        for vertex in vertices_list:
            self.add_vertex(vertex)

    def find_vertex(self, vertex_name):
        """:return vertex from graph by name"""
        for vertex in self.vertices:
            if vertex.name == vertex_name:
                return vertex
        return 'Vertex is not in graph'

    def delete_vertex(self, vertex_name):
        """delete vertex from graph"""
        for vertex in self.vertices.copy():
            if vertex.name == vertex_name:
                self.vertices.remove(vertex)
        for vertex in self.vertices:
            vertex.delete_neighbour(vertex_name)


if __name__ == "__main__":
    a = Vertex('A')
    b = Vertex('B')
    c = Vertex('C')
    d = Vertex('D')
    e = Vertex('E')
    f = Vertex('F')
    g = Vertex('G')
    h = Vertex('H', [d, a, f, c])
    a.append_neighbours([b, c, g])
    g.append_neighbours([e, f])
    graph = Graph("G")
    graph.add_vertices([a, b, c, d, e, f, g, h])
    print(graph)
    some_vertex = graph.find_vertex("A")
    graph.delete_vertex('A')
    print(graph)

