from pkg_1.MyGraph import MyGraph
import time

print("Zachary Club: Grafo non diretto non pesato con 34 vertici e 78 archi")
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
print("\nGreedy Min vertex cover: ")
inizio_GMVC = time.clock()
listGMVC = graph2.greedy_min_vertex_cover()
fine_GMVC = time.clock()
t_GMVC = fine_GMVC - inizio_GMVC
for elem in listGMVC:
    print(elem, end=", ")
print("\n\nGREEDY --> Dim =", len(listGVC), ", Time =", t_GVC, "s\n")
print("MIN --> Dim =", len(listMVC), ", Time =", t_MVC, "s\n")
print("GREEDY MIN --> Dim =", len(listGMVC), ", Time =", t_GMVC, "s\n")
print("La dimensione dell'algoritmo Greedy è di", len(listGVC)-len(listMVC), "vertici in più rispetto all'algoritmo Min.\n")
print("L'algoritmo Greedy è", int(t_MVC/t_GVC), "volte piu' veloce di quello Min.\n")
print("\n\n")