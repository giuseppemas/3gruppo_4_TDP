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

print("Greedy vertex cover: ")
listGVC = graph1.greedy_vertex_cover()
for elem in listGVC:
    print(elem, end=", ")
print("\n\n")
print("Min vertex cover: ")
listMVC = graph1.min_vertex_cover()
for elem in listMVC:
    print(elem, end=", ")
print("\n\n\n")


print("SECONDO ESEMPIO: Grafo non diretto non pesato con 34 vertici e 78 archi")
graph2 = MyGraph()
vert = []
for i in range (1,35):
    vert.append(graph2.insert_vertex(i))
print("Vertici: [")
for v in graph2.vertices():
    print(v, end=", ")
print("]\n\n")

in_file = open("zachary_club.txt","r")              #lettura da file
testo = in_file.read()
in_file.close()
lettura = testo.splitlines()
lettura = list(lettura)
lenLettura = len(lettura)
i = 2
while i < lenLettura:
    endpoints = lettura[i].split(" ")               #inserisce i 2 estremi in un array di 2 elementi
    j = 0
    while vert[j]._element != int(endpoints[0]):
        j = j+1
    z = 0
    while vert[z]._element != int(endpoints[1]):
        z = z + 1
    graph2.insert_edge(vert[j],vert[z])
    i = i+1
print("Archi: [")
for e in graph2.edges():
    print(e, end=", ")
print("]\n\n")

print("Greedy vertex cover: ")
listGVC2 = graph2.greedy_vertex_cover()
for elem in listGVC2:
    print(elem, end=", ")
print("\n\n")
print("Min vertex cover: ")
listMVC2 = graph2.min_vertex_cover()
for elem in listMVC2:
    print(elem, end=", ")
print("\n\n\n")

print("TERZO ESEMPIO: Grafo non diretto non pesato con 12 vertici e 17 archi")
graph3 = MyGraph()
vertex1 = graph3.insert_vertex(1)
vertex2 = graph3.insert_vertex(2)
vertex3 = graph3.insert_vertex(3)
vertex4 = graph3.insert_vertex(4)
vertex5 = graph3.insert_vertex(5)
vertex6 = graph3.insert_vertex(6)
vertex7 = graph3.insert_vertex(7)
vertex8 = graph3.insert_vertex(8)
vertex9 = graph3.insert_vertex(9)
vertex10 = graph3.insert_vertex(10)
vertex11 = graph3.insert_vertex(11)
vertex12 = graph3.insert_vertex(12)
print("VERTICI: [")
for v in graph1.vertices():
    print(v, end=", ")
print("\n]\n\n")

graph3.insert_edge(vertex1, vertex2)
graph3.insert_edge(vertex2, vertex3)
graph3.insert_edge(vertex3, vertex4)
graph3.insert_edge(vertex4, vertex5)
graph3.insert_edge(vertex5, vertex6)
graph3.insert_edge(vertex6, vertex7)
graph3.insert_edge(vertex7, vertex1)
graph3.insert_edge(vertex7, vertex8)
graph3.insert_edge(vertex8, vertex12)
graph3.insert_edge(vertex12, vertex9)
graph3.insert_edge(vertex9, vertex5)
graph3.insert_edge(vertex9, vertex4)
graph3.insert_edge(vertex12, vertex10)
graph3.insert_edge(vertex10, vertex11)
graph3.insert_edge(vertex10, vertex3)
graph3.insert_edge(vertex11, vertex2)
graph3.insert_edge(vertex6, vertex8)

print("ARCHI: [")
for e in graph3.edges():
    print (e, end="\n")
print("]\n\n")

print("Greedy vertex cover: ")
listGVC3 = graph3.greedy_vertex_cover()
for elem in listGVC3:
    print(elem, end=", ")
print("\n\n")
print("Min vertex cover: ")
listMVC3 = graph3.min_vertex_cover()
for elem in listMVC3:
    print(elem, end=", ")
print("\n\n\n")