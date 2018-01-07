from pkg_1.MyGraph import randomGraph
from pkg_1.MyGraph import connected
import time

N = 40
n = 20
m = 60
connessi = 0
while connessi < N:
    g1 = randomGraph(n, m)

    if connected(g1):
        connessi += 1
        print("GENERAZIONE GRAFO RANDOM: ", connessi + 1, "\n")
        print("Numero dei vertici: ", n)
        print("Archi: ", m)
        for e in g1.edges():
            print(e, end=", ")
        print("\n")

        print("Greedy vertex cover: ")
        inizio_GVC = time.clock()
        listGVC = g1.greedy_vertex_cover()
        fine_GVC = time.clock()
        t_GVC = fine_GVC - inizio_GVC
        for elem in listGVC:
            print(elem, end=", ")
        print("\nMin vertex cover: ")
        inizio_MVC = time.clock()
        listMVC = g1.min_vertex_cover()
        fine_MVC = time.clock()
        t_MVC = fine_MVC - inizio_MVC
        for elem in listMVC:
            print(elem, end=", ")
        print("\n\nGREEDY --> Dim =", len(listGVC), ", Time =", t_GVC, "s\n")
        print("MIN --> Dim =", len(listMVC), ", Time =", t_MVC, "s\n")
        print("La dimensione dell'algoritmo Greedy è di", len(listGVC) - len(listMVC),
              "vertici in più rispetto all'algoritmo Min.\n")
        print("L'algoritmo Greedy è", t_MVC / t_GVC, "volte piu' veloce di quello Min.\n")
        print("L'algoritmo Greedy impiega", t_MVC - t_GVC, "secondi in meno rispetto a quello Min.\n")
        print("\n\n")