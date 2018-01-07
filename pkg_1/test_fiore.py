from pkg_1.MyGraph import MyGraph
import time

print("Fiore: Grafo non diretto non pesato con 26 vertici e 73 archi")
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