from pkg_1.MyGraph import MyGraph
import time

print("Miserabili: Grafo non diretto non pesato con 77 vertici e 254 archi")
graph4 = MyGraph()
vert2 = []
for i in range (1,78):
    vert2.append(graph4.insert_vertex(i))
print("Vertici: [")
for v in graph4.vertices():
    print(v, end=", ")
print("]\n\n")

in_file = open("miserabili.txt","r")                 #lettura da file
testo2 = in_file.read()
in_file.close()
lettura2 = testo2.splitlines()
lettura2 = list(lettura2)
lenLettura2 = len(lettura2)
i = 2
while i < 150:
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