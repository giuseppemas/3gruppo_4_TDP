from pkg_1.MyGraph import MyGraph


print("PRIMO ESEMPIO: Grafo non diretto non pesato con 8 vertici e 10 archi")
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

listGVC = graph1.greedy_vertex_cover()
for elem in listGVC:
    print(elem, end=", ")
print("\n\n\n")


print("SECONDO ESEMPIO: Grafo non diretto non pesato con 34 vertici e 78 archi")
graph2 = MyGraph()
for i in range (1,35):
    graph2.insert_vertex(i)
print("Vertici: [")
for v in graph2.vertices():
    print(v, end=", ")
print("]\n\n")