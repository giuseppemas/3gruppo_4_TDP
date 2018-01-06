from pkg_1.MyGraph import MyGraph
import time
import random

'''
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
print("\n]\n")

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
    print (e, end=", ")
print("]\n")

print("Greedy vertex cover: ")
inizio_GVC = time.clock()
listGVC = graph1.greedy_vertex_cover()
fine_GVC = time.clock()
t_GVC = fine_GVC - inizio_GVC
for elem in listGVC:
    print(elem, end=", ")
print("\nMin vertex cover: ")
inizio_MVC = time.clock()
listMVC = graph1.min_vertex_cover()
fine_MVC = time.clock()
t_MVC = fine_MVC - inizio_MVC
for elem in listMVC:
    print(elem, end=", ")
print("\n\nGREEDY --> Dim =", len(listGVC), ", Time =", t_GVC, "s\n")
print("MIN --> Dim =", len(listMVC), ", Time =", t_MVC, "s\n")
print("La dimensione dell'algoritmo Greedy è di", len(listGVC)-len(listMVC), "vertici in più rispetto all'algoritmo Min.\n")
print("L'algoritmo Greedy è", int(t_MVC/t_GVC), "volte piu' veloce di quello Min.\n")
print("\n\n")

print("Exponential Min Vertex Cover: ")
inizio_EMVC = time.clock()
listEMVC = graph1.min_vertex_cover2()
print("type: ", type(listEMVC))
fine_EMVC = time.clock()
t_EMVC = fine_EMVC - inizio_EMVC
for elem in listEMVC:
    print(elem, end=", ")
print("EXP MIN --> Dim =", len(listEMVC), ", Time =", t_EMVC, "s\n")
print("La dimensione dell'algoritmo Greedy è di", len(listMVC)-len(listEMVC), "vertici in più rispetto all'algoritmo Min.\n")
print("L'algoritmo Greedy è", t_MVC/t_EMVC, "secondi piu' veloce di quello Min.\n")
print("\n\n")

print("SECONDO ESEMPIO: Grafo non diretto non pesato con 12 vertici e 17 archi")
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
for v in graph3.vertices():
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
graph3.insert_edge(vertex4, vertex9)
graph3.insert_edge(vertex12, vertex10)
graph3.insert_edge(vertex10, vertex11)
graph3.insert_edge(vertex10, vertex3)
graph3.insert_edge(vertex11, vertex2)
graph3.insert_edge(vertex6, vertex8)

print("ARCHI: [")
for e in graph3.edges():
    print (e, end=", ")
print("]\n\n")

print("Greedy vertex cover: ")
inizio_GVC = time.clock()
listGVC = graph3.greedy_vertex_cover()
fine_GVC = time.clock()
t_GVC = fine_GVC - inizio_GVC
for elem in listGVC:
    print(elem, end=", ")
print("\nMin vertex cover: ")
inizio_MVC = time.clock()
listMVC = graph3.min_vertex_cover()
fine_MVC = time.clock()
t_MVC = fine_MVC - inizio_MVC
for elem in listMVC:
    print(elem, end=", ")
print("\n\nGREEDY --> Dim =", len(listGVC), ", Time =", t_GVC, "s\n")
print("MIN --> Dim =", len(listMVC), ", Time =", t_MVC, "s\n")
print("La dimensione dell'algoritmo Greedy è di", len(listGVC)-len(listMVC), "vertici in più rispetto all'algoritmo Min.\n")
print("L'algoritmo Greedy è", int(t_MVC/t_GVC), "volte piu' veloce di quello Min.\n")
print("\n\n")

print("Exponential Min Vertex Cover: ")
inizio_EMVC = time.clock()
listEMVC = graph3.min_vertex_cover2()
print("type: ", type(listEMVC))
fine_EMVC = time.clock()
t_EMVC = fine_EMVC - inizio_EMVC
for elem in listEMVC:
    print(elem, end=", ")
print("EXP MIN --> Dim =", len(listEMVC), ", Time =", t_EMVC, "s\n")
print("La dimensione dell'algoritmo Greedy è di", len(listMVC)-len(listEMVC), "vertici in più rispetto all'algoritmo Min.\n")
print("L'algoritmo Greedy è", t_MVC/t_EMVC, "secondi piu' veloce di quello Min.\n")
print("\n\n")


print("TERZO ESEMPIO: Grafo non diretto non pesato con 15 vertici e 51 archi")
graph4 = MyGraph()
vert2 = []
for i in range (1,16):
    vert2.append(graph4.insert_vertex(i))
print("Vertici: [")
for v in graph4.vertices():
    print(v, end=", ")
print("]\n\n")

in_file = open("test1.txt","r")              #lettura da file
testo2 = in_file.read()
in_file.close()
lettura2 = testo2.splitlines()
lettura2 = list(lettura2)
lenLettura2 = len(lettura2)
i = 2
while i < lenLettura2:
    endpoints = lettura2[i].split(" ")               #inserisce i 2 estremi in un array di 2 elementi
    j = 0
    while vert2[j]._element != int(endpoints[0]):
        j = j+1
    z = 0
    while vert2[z]._element != int(endpoints[1]):
        z = z + 1
    graph4.insert_edge(vert2[j],vert2[z])
    i = i+1
print("Archi: [")
for e in graph4.edges():
    print(e, end=", ")
print("]\n\n")

print("Greedy vertex cover: ")
inizio_GVC = time.clock()
listGVC = graph4.greedy_vertex_cover()
fine_GVC = time.clock()
t_GVC = fine_GVC - inizio_GVC
for elem in listGVC:
    print(elem, end=", ")
print("\nMin vertex cover: ")
inizio_MVC = time.clock()
listMVC = graph4.min_vertex_cover()
fine_MVC = time.clock()
t_MVC = fine_MVC - inizio_MVC
for elem in listMVC:
    print(elem, end=", ")
print("\n\nGREEDY --> Dim =", len(listGVC), ", Time =", t_GVC, "s\n")
print("MIN --> Dim =", len(listMVC), ", Time =", t_MVC, "s\n")
print("La dimensione dell'algoritmo Greedy è di", len(listGVC)-len(listMVC), "vertici in più rispetto all'algoritmo Min.\n")
print("L'algoritmo Greedy è", int(t_MVC/t_GVC), "volte piu' veloce di quello Min.\n")
print("\n\n")

print("Exponential Min Vertex Cover: ")
inizio_EMVC = time.clock()
listEMVC = graph4.min_vertex_cover2()
print("type: ", type(listEMVC))
fine_EMVC = time.clock()
t_EMVC = fine_EMVC - inizio_EMVC
for elem in listEMVC:
    print(elem, end=", ")
print("EXP MIN --> Dim =", len(listEMVC), ", Time =", t_EMVC, "s\n")
print("La dimensione dell'algoritmo Greedy è di", len(listMVC)-len(listEMVC), "vertici in più rispetto all'algoritmo Min.\n")
print("L'algoritmo Greedy è", t_MVC/t_EMVC, "secondi piu' veloce di quello Min.\n")
print("\n\n")



print("QUARTO ESEMPIO: Grafo non diretto non pesato con 20 vertici e 51 archi")
graph5 = MyGraph()
vert5 = []
R = 20
for i in range(1, R+1):
    vert5.append(graph5.insert_vertex(i))
print("Vertici: [")
for v in graph5.vertices():
    print(v, end=", ")
print("]\n\n")

num_edges = random.randint(60,80)
i = 0
while i < num_edges:
    graph5.insert_edge(vert5[random.randint(1, R-1)], vert5[random.randint(1, R-1)])
    i = i + 1
print("Archi: [")
for e in graph5.edges():
    print(e, end=", ")
print("]\n\n")

print("Greedy vertex cover: ")
inizio_GVC = time.clock()
listGVC = graph5.greedy_vertex_cover()
fine_GVC = time.clock()
t_GVC = fine_GVC - inizio_GVC
for elem in listGVC:
    print(elem, end=", ")
print("\nMin vertex cover: ")
inizio_MVC = time.clock()
listMVC = graph5.min_vertex_cover()
fine_MVC = time.clock()
t_MVC = fine_MVC - inizio_MVC
for elem in listMVC:
    print(elem, end=", ")
print("\n\nGREEDY --> Dim =", len(listGVC), ", Time =", t_GVC, "s\n")
print("MIN --> Dim =", len(listMVC), ", Time =", t_MVC, "s\n")
print("La dimensione dell'algoritmo Greedy è di", len(listGVC)-len(listMVC), "vertici in più rispetto all'algoritmo Min.\n")
print("L'algoritmo Greedy è", int(t_MVC/t_GVC), "volte piu' veloce di quello Min.\n")
print("\n\n")



print("QUINTO ESEMPIO: Grafo non diretto non pesato con 34 vertici e 50 archi")
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
while i < 50:
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
inizio_GVC = time.clock()
listGVC = graph2.greedy_vertex_cover()
fine_GVC = time.clock()
t_GVC = fine_GVC - inizio_GVC
for elem in listGVC:
    print(elem, end=", ")
print("\nMin vertex cover: ")
inizio_MVC = time.clock()
listMVC = graph2.min_vertex_cover()
fine_MVC = time.clock()
t_MVC = fine_MVC - inizio_MVC
for elem in listMVC:
    print(elem, end=", ")
print("\n\nGREEDY --> Dim =", len(listGVC), ", Time =", t_GVC, "s\n")
print("MIN --> Dim =", len(listMVC), ", Time =", t_MVC, "s\n")
print("La dimensione dell'algoritmo Greedy è di", len(listGVC)-len(listMVC), "vertici in più rispetto all'algoritmo Min.\n")
print("L'algoritmo Greedy è", int(t_MVC/t_GVC), "volte piu' veloce di quello Min.\n")
print("\n\n")



print("QUINTO ESEMPIO: Grafo non diretto non pesato con 34 vertici e 60 archi")
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
while i < 60:
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
inizio_GVC = time.clock()
listGVC = graph2.greedy_vertex_cover()
fine_GVC = time.clock()
t_GVC = fine_GVC - inizio_GVC
for elem in listGVC:
    print(elem, end=", ")
print("\nMin vertex cover: ")
inizio_MVC = time.clock()
listMVC = graph2.min_vertex_cover()
fine_MVC = time.clock()
t_MVC = fine_MVC - inizio_MVC
for elem in listMVC:
    print(elem, end=", ")
print("\n\nGREEDY --> Dim =", len(listGVC), ", Time =", t_GVC, "s\n")
print("MIN --> Dim =", len(listMVC), ", Time =", t_MVC, "s\n")
print("La dimensione dell'algoritmo Greedy è di", len(listGVC)-len(listMVC), "vertici in più rispetto all'algoritmo Min.\n")
print("L'algoritmo Greedy è", int(t_MVC/t_GVC), "volte piu' veloce di quello Min.\n")
print("\n\n")



print("OTTAVO ESEMPIO: Grafo non diretto non pesato con 34 vertici e 78 archi")
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
inizio_GVC = time.clock()
listGVC = graph2.greedy_vertex_cover()
fine_GVC = time.clock()
t_GVC = fine_GVC - inizio_GVC
for elem in listGVC:
    print(elem, end=", ")
print("\nMin vertex cover: ")
inizio_MVC = time.clock()
listMVC = graph2.min_vertex_cover()
fine_MVC = time.clock()
t_MVC = fine_MVC - inizio_MVC
for elem in listMVC:
    print(elem, end=", ")
print("\n\nGREEDY --> Dim =", len(listGVC), ", Time =", t_GVC, "s\n")
print("MIN --> Dim =", len(listMVC), ", Time =", t_MVC, "s\n")
print("La dimensione dell'algoritmo Greedy è di", len(listGVC)-len(listMVC), "vertici in più rispetto all'algoritmo Min.\n")
print("L'algoritmo Greedy è", int(t_MVC/t_GVC), "volte piu' veloce di quello Min.\n")
print("\n\n")


print("NONO ESEMPIO: Grafo non diretto non pesato con 77 vertici e 254 archi")
graph4 = MyGraph()
vert2 = []
for i in range (1,78):
    vert2.append(graph4.insert_vertex(i))
print("Vertici: [")
for v in graph4.vertices():
    print(v, end=", ")
print("]\n\n")

in_file = open("miserabili.txt","r")              #lettura da file
testo2 = in_file.read()
in_file.close()
lettura2 = testo2.splitlines()
lettura2 = list(lettura2)
lenLettura2 = len(lettura2)
i = 2
while i < lenLettura2:
    endpoints = lettura2[i].split(" ")               #inserisce i 2 estremi in un array di 2 elementi
    j = 0
    while vert2[j]._element != int(endpoints[0]):
        j = j+1
    z = 0
    while vert2[z]._element != int(endpoints[1]):
        z = z + 1
    graph4.insert_edge(vert2[j],vert2[z])
    i = i+1
print("Archi: [")
for e in graph4.edges():
    print(e, end=", ")
print("]\n\n")

print("Greedy vertex cover: ")
inizio_GVC = time.clock()
listGVC = graph4.greedy_vertex_cover()
fine_GVC = time.clock()
t_GVC = fine_GVC - inizio_GVC
for elem in listGVC:
    print(elem, end=", ")
print("\nMin vertex cover: ")
inizio_MVC = time.clock()
listMVC = graph4.min_vertex_cover()
fine_MVC = time.clock()
t_MVC = fine_MVC - inizio_MVC
for elem in listMVC:
    print(elem, end=", ")
print("\n\nGREEDY --> Dim =", len(listGVC), ", Time =", t_GVC, "s\n")
print("MIN --> Dim =", len(listMVC), ", Time =", t_MVC, "s\n")
print("La dimensione dell'algoritmo Greedy è di", len(listGVC)-len(listMVC), "vertici in più rispetto all'algoritmo Min.\n")
print("L'algoritmo Greedy è", int(t_MVC/t_GVC), "volte piu' veloce di quello Min.\n")
print("\n\n")
'''

print("DECIMO ESEMPIO: Grafo non diretto non pesato con 26 vertici e 73 archi")
G = MyGraph()
V = []

V.append(G.insert_vertex('a'))
V.append(G.insert_vertex('b'))
V.append(G.insert_vertex('c'))
V.append(G.insert_vertex('d'))
V.append(G.insert_vertex('e'))
V.append(G.insert_vertex('f'))
V.append(G.insert_vertex('g'))
V.append(G.insert_vertex('h'))
V.append(G.insert_vertex('i'))
V.append(G.insert_vertex('j'))
V.append(G.insert_vertex('k'))
V.append(G.insert_vertex('l'))
V.append(G.insert_vertex('m'))
V.append(G.insert_vertex('n'))
V.append(G.insert_vertex('o'))
V.append(G.insert_vertex('p'))
V.append(G.insert_vertex('q'))
V.append(G.insert_vertex('r'))
V.append(G.insert_vertex('s'))
V.append(G.insert_vertex('t'))
V.append(G.insert_vertex('u'))
V.append(G.insert_vertex('v'))
V.append(G.insert_vertex('w'))
V.append(G.insert_vertex('x'))
V.append(G.insert_vertex('y'))
V.append(G.insert_vertex('z'))


for i in range(len(V)):
    if i != 0:
        G.insert_edge(V[0],V[i])

for i in range(len(V)):
    if i != 0 and i != len(V) - 1:
        G.insert_edge(V[i],V[i + 1])

G.insert_edge(V[-1], V[1])

for i in range(len(V)):
    if i != 0 and (i != len(V) - 2 and i != len(V) - 1):
        G.insert_edge(V[i],V[i + 2])

print("Greedy vertex cover: ")
inizio_GVC = time.clock()
listGVC = G.greedy_vertex_cover()
fine_GVC = time.clock()
t_GVC = fine_GVC - inizio_GVC
for elem in listGVC:
    print(elem, end=", ")
print("\nMin vertex cover: ")
inizio_MVC = time.clock()
listMVC = G.min_vertex_cover()
fine_MVC = time.clock()
t_MVC = fine_MVC - inizio_MVC
for elem in listMVC:
    print(elem, end=", ")
print("\n\nGREEDY --> Dim =", len(listGVC), ", Time =", t_GVC, "s\n")
print("MIN --> Dim =", len(listMVC), ", Time =", t_MVC, "s\n")
print("La dimensione dell'algoritmo Greedy è di", len(listGVC)-len(listMVC), "vertici in più rispetto all'algoritmo Min.\n")
print("L'algoritmo Greedy è", int(t_MVC/t_GVC), "volte piu' veloce di quello Min.\n")
print("\n\n")

print("Exponential Min Vertex Cover: ")
inizio_EMVC = time.clock()
listEMVC = G.min_vertex_cover2()
print("type: ", type(listEMVC))
fine_EMVC = time.clock()
t_EMVC = fine_EMVC - inizio_EMVC
for elem in listEMVC:
    print(elem, end=", ")
print("EXP MIN --> Dim =", len(listEMVC), ", Time =", t_EMVC, "s\n")
print("La dimensione dell'algoritmo Greedy è di", len(listMVC)-len(listEMVC), "vertici in più rispetto all'algoritmo Min.\n")
print("L'algoritmo Greedy è", t_MVC/t_EMVC, "secondi piu' veloce di quello Min.\n")
print("\n\n")