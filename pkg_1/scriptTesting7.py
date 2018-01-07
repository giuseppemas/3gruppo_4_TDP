'''Valutare sperimentalmente le prestazioni dei due metodi su un campione di almeno k grafi (con k > 50) con n vertici
(n > 50) con scelti a caso. Per ciascun grafo fornire le dimensioni dei vertex cover restituiti dai due metodi ed i
relativi tempi di esecuzione. Calcolare di quanto in media l’algoritmo greedy è più veloce rispetto all’algoritmo ottimo
e di quanto il vertex cover restituito è più grande.'''

from pkg_1.MyGraph import MyGraph
import time

print("Testing50 #1: Grafo non diretto non pesato con 51 vertici e 20 archi")
graph2 = MyGraph()
vert = []
for i in range (1,52):
    vert.append(graph2.insert_vertex(i))
print("Vertici: [")
for v in graph2.vertices():
    print(v, end=", ")
print("]\n\n")

in_file = open("test50.txt","r")              #lettura da file
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
    i = i+5
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
print("L'algoritmo Greedy è", t_MVC/t_GVC, "volte piu' veloce di quello Min.\n")
print("L'algoritmo Greedy impiega", t_MVC-t_GVC, "secondi in meno rispetto a quello Min.\n")
print("\n\n")

#---------------------------------------------------------------------------------------

print("Testing50 #2: Grafo non diretto non pesato con 51 vertici e 25 archi")
graph2 = MyGraph()
vert = []
for i in range (1,52):
    vert.append(graph2.insert_vertex(i))
print("Vertici: [")
for v in graph2.vertices():
    print(v, end=", ")
print("]\n\n")

in_file = open("test50.txt","r")              #lettura da file
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
    i = i+4
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
print("L'algoritmo Greedy è", t_MVC/t_GVC, "volte piu' veloce di quello Min.\n")
print("L'algoritmo Greedy impiega", t_MVC-t_GVC, "secondi in meno rispetto a quello Min.\n")
print("\n\n")

#---------------------------------------------------------------------------------------

print("Testing50 #3: Grafo non diretto non pesato con 51 vertici 34 archi")
graph2 = MyGraph()
vert = []
for i in range (1,52):
    vert.append(graph2.insert_vertex(i))
print("Vertici: [")
for v in graph2.vertices():
    print(v, end=", ")
print("]\n\n")

in_file = open("test50.txt","r")              #lettura da file
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
    i = i+3
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
print("L'algoritmo Greedy è", t_MVC/t_GVC, "volte piu' veloce di quello Min.\n")
print("L'algoritmo Greedy impiega", t_MVC-t_GVC, "secondi in meno rispetto a quello Min.\n")
print("\n\n")


#---------------------------------------------------------------------------------------

print("Testing50 #4: Fiore --> Grafo non diretto non pesato con 26 vertici e 73 archi")
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
print("L'algoritmo Greedy è", t_MVC/t_GVC, "volte piu' veloce di quello Min.\n")
print("\n\n")

#---------------------------------------------------------------------------------------

print("Testing50 #5: Tratto dai miserabili.txt: Grafo non diretto pesato con 77 vertici e 77 archi")
graph2 = MyGraph()
vert = []
for i in range (1,78):
    vert.append(graph2.insert_vertex(i))
print("Vertici: [")
for v in graph2.vertices():
    print(v, end=", ")
print("]\n\n")

in_file = open("miserabili.txt","r")              #lettura da file
testo = in_file.read()
in_file.close()
lettura = testo.splitlines()
lettura = list(lettura)
lenLettura = len(lettura)
i = 2
while i < 78:
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
print("L'algoritmo Greedy è", t_MVC/t_GVC, "volte piu' veloce di quello Min.\n")
print("L'algoritmo Greedy impiega", t_MVC-t_GVC, "secondi in meno rispetto a quello Min.\n")
print("\n\n")

#---------------------------------------------------------------------------------------

print("Testing50 #6: Tratto dai miserabili.txt: Grafo non diretto pesato con 77 vertici e 100 archi")
graph2 = MyGraph()
vert = []
for i in range (1,78):
    vert.append(graph2.insert_vertex(i))
print("Vertici: [")
for v in graph2.vertices():
    print(v, end=", ")
print("]\n\n")

in_file = open("miserabili.txt","r")              #lettura da file
testo = in_file.read()
in_file.close()
lettura = testo.splitlines()
lettura = list(lettura)
lenLettura = len(lettura)
i = 2
while i < 101:
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
print("L'algoritmo Greedy è", t_MVC/t_GVC, "volte piu' veloce di quello Min.\n")
print("L'algoritmo Greedy impiega", t_MVC-t_GVC, "secondi in meno rispetto a quello Min.\n")
print("\n\n")

#---------------------------------------------------------------------------------------

print("Testing50 #7: Tratto dai miserabili.txt: Grafo non diretto pesato con 77 vertici e 120 archi")
graph2 = MyGraph()
vert = []
for i in range (1,78):
    vert.append(graph2.insert_vertex(i))
print("Vertici: [")
for v in graph2.vertices():
    print(v, end=", ")
print("]\n\n")

in_file = open("miserabili.txt","r")              #lettura da file
testo = in_file.read()
in_file.close()
lettura = testo.splitlines()
lettura = list(lettura)
lenLettura = len(lettura)
i = 2
while i < 121:
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
print("L'algoritmo Greedy è", t_MVC/t_GVC, "volte piu' veloce di quello Min.\n")
print("L'algoritmo Greedy impiega", t_MVC-t_GVC, "secondi in meno rispetto a quello Min.\n")
print("\n\n")