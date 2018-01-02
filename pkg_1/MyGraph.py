from TdP_collections.graphs.graph import Graph

class MyGraph (Graph):

    def __init__(self):
        super(MyGraph, self).__init__()


    def min_vertex_cover(self):
        pass


    def greedy_vertex_cover(self):
        vertexCover = {}
        E = set()
        for e in self.edges():
            E.add(e)
        while E != 0:
            e = E.pop()
            u, v = e.endpoints()                    #assegno ad u e v i due estremi dell'arco
            vertexCover[u] = {}
            vertexCover[v] = {}
            for elem in vertexCover:
                print(elem, end="\n")
            self.remove_incident_edges(u)
            self.remove_incident_edges(v)
        return vertexCover


    def remove_edges(self, e):
        w,z = e.endpoints()
        self._validate_vertex(w)
        self._validate_vertex(z)
        del self._outgoing[w][z]
        del self._incoming[z][w]


    def remove_incident_edges(self, u):
        incident = self.degree(u)
        while incident != 0:
            self.remove_edges(edge)



graph1 = MyGraph()
vertex1 = graph1.insert_vertex("A")
vertex2 = graph1.insert_vertex("B")
vertex3 = graph1.insert_vertex("C")
vertex4 = graph1.insert_vertex("D")
vertex5 = graph1.insert_vertex("E")
vertex6 = graph1.insert_vertex("F")
vertex7 = graph1.insert_vertex("G")
vertex8 = graph1.insert_vertex("H")
print("VERTICI: [")
for v in graph1.vertices():
    print(v, end=", ")
print("\n]\n\n")

graph1.insert_edge(vertex1, vertex2)
graph1.insert_edge(vertex1, vertex3)
graph1.insert_edge(vertex2, vertex3)
graph1.insert_edge(vertex3, vertex5)
graph1.insert_edge(vertex3, vertex4)
graph1.insert_edge(vertex4, vertex6)
graph1.insert_edge(vertex4, vertex8)
graph1.insert_edge(vertex4, vertex7)
graph1.insert_edge(vertex5, vertex6)
graph1.insert_edge(vertex8, vertex7)

print("ARCHI: [")
for e in graph1.edges():
    print (e, end="\n")
print("]\n\n")

for v in graph1.incident_edges(vertex1):
    print(v, end=", ")

graph1.greedy_vertex_cover()