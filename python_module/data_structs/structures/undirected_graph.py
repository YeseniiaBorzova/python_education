"""Module contains  class representing undirected unweighted graph"""
from structures.doubly_linked_list import DoublyLinkedList


class Vertex:
    """Class that represent vertex of graph"""
    def __init__(self, name, connected_to=None):
        """Constructor"""
        self.connected_to = DoublyLinkedList()
        if connected_to is not None:
            for connection in connected_to:
                self.append_neighbour(connection)
        self.name = name

    def __str__(self):
        """to string magic method"""
        if self.connected_to.get_size() != 0:
            s = ''
            for connection in self.connected_to:
                s += f"{self.name} -> {connection.get_name()} "
            return s
        return self.name

    def get_name(self):
        """:return name of vertex"""
        return self.name

    def append_neighbour(self, neighbour):
        """add neighbour to the vertex"""
        self.connected_to.append(neighbour)
        neighbour.connected_to.append(self)

    def append_neighbours(self, neighbours_list):
        """add neighbours to the vertex"""
        for neighbour in neighbours_list:
            self.append_neighbour(neighbour)

    def delete_neighbour(self, neighbour_name):
        """delete neighbour from the vertex"""
        for neighbour in self.connected_to:
            if neighbour.name == neighbour_name:
                self.connected_to.remove_by_value(neighbour)
                return
        return "Not in neighbours list"

    def show_neighbours(self):
        """shows neighbours of the vertex"""
        if self.connected_to:
            s = ""
            for connection in self.connected_to:
                s += f"{connection.get_name()} "
            return s
        return "No neighbours"

    def get_neighbours(self):
        """:return neighbour-vertex objects"""
        if self.connected_to.get_size():
            return self.connected_to
        return None


class Graph:
    """Class representing undirected
    unweighted graph"""
    def __init__(self, name, vertices=None):
        """Constructor"""
        self.vertices = DoublyLinkedList()
        if vertices is not None:
            for vertex in vertices:
                self.vertices.append(vertex)
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
            self.vertices.append(vertex)
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
        for vertex in self.vertices:
            if vertex.name == vertex_name:
                self.vertices.remove_by_value(vertex)
        for vertex in self.vertices:
            vertex.delete_neighbour(vertex_name)

    def get_vertices(self):
        """return all graph vertices as linked list"""
        return self.vertices


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
    some_vertex = graph.find_vertex("A")
    print(graph)
    graph.delete_vertex("A")
    print('\n')
    print(graph)




