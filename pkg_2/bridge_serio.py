from TdP_collections.graphs.dfs import DFS_complete
from TdP_collections.graphs.graph import Graph
import random
import time

"""
Preso in input un oggetto MyGraph G, restituisce un bridge di G oppure None se il grafo è biconnesso
"""
class MyGraph (Graph):

    def remove_edge(self, u, v, x=None):
        if self.get_edge(u, v) is None:  # includes error checking
            return
        del self._outgoing[u][v]
        del self._outgoing[v][u]


def DFS_bridge_serio(g, bridge, vertici, archi, ordine, v):

    vertici[v] = "VISITED"
    ordine.append(v)
    #print("ORDINE: ",v)
    for e in g.incident_edges(v):
        if archi[e] == "UNEXPLORED":
            w = e.opposite(v)

            if vertici[w] == "UNEXPLORED":
                archi[e] = "DISCOVERY"
                ordine.append(e)
                #print("ORDINE: ", e)
                DFS_bridge_serio(g,bridge,vertici,archi,ordine,w)
                ordine.remove(e)

            else:
                archi[e] = "BACK"
                bridge.remove(e)
                origine, destinazione = e.endpoints()
                if origine != ordine[-1]:
                    vertice_finale = origine
                else:
                    vertice_finale = destinazione

                i = -2
                walk = ordine[i]
                next = ordine[i-1]
                while walk != vertice_finale:
                    #print("CICLO WHILE:", origine, destinazione, walk, next, vertice_finale)
                    if type(walk) == Graph.Edge:
                        #print("DOVREI RIMUOVERE ", walk)
                        if walk in bridge:
                            #print("HO RIMOSSO ", walk)
                            bridge.remove(walk)
                    i -= 1
                    walk = ordine[i]
                    if (i-1) >= (-1)*len(ordine):
                        next = ordine[i-1]

    ordine.remove(v)


def DFS_complete_bridge_serio(g):

    vertici = {}
    archi = {}
    ordine = []
    bridge = []

    for v in g.vertices():
        vertici[v] = "UNEXPLORED"
    for e in g.edges():
        bridge.append(e)
        archi[e] = "UNEXPLORED"

    for v in g.vertices():
        if vertici[v] == "UNEXPLORED":
            DFS_bridge_serio(g, bridge, vertici, archi, ordine, v)

    for b in bridge:
        print("BRIDGE: ", b)

    return bridge

def randomGraph(n,m):

    if m < n-1:
        raise Exception("Non può essere un grafo connesso")
    g = MyGraph()
    for i in range(n):

        g.insert_vertex(i + 1)

    vertici = list(g.vertices())

    # Primo Arco
    r1 = random.randint(0,n-1)
    r2 = random.randint(0,n-1)
    while r2 == r1:

        r2 = random.randint(0,n-1)
    g.insert_edge(vertici[r1], vertici[r2])

    k = g.edge_count()
    while k < m:

        r1 = random.randint(0, n - 1)
        r2 = random.randint(0, n - 1)
        while r2 == r1:
            r2 = random.randint(0, n - 1)

        if g.get_edge(vertici[r1], vertici[r2]) is None:
            g.insert_edge(vertici[r1], vertici[r2], None)
            k += 1

    return g

def connected(g):
    foresta = DFS_complete(g)
    count = 0
    for v in g.vertices():
        if foresta[v] is None:
            count += 1

    return count == 1


#---------------------------------------------------------------------------------------

if __name__ == "__main__":


    g_bridge = MyGraph()
    alfabeto = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L",
                13: "M",
                14: "N", 15: "O", 16: "P", 17: "Q"}
    for i in range(17):
        g_bridge.insert_vertex(alfabeto[i+1])

    ver = list(g_bridge.vertices())

    n = len(g_bridge.vertices())
    print("TEST GRAFO BRIDGE.TXT-------------------------\n")
    print("Numero dei vertici: ", n)

    g_bridge.insert_edge(ver[0], ver[1])  # A B
    g_bridge.insert_edge(ver[0], ver[4])  # A E
    g_bridge.insert_edge(ver[0], ver[5])  # A F
    g_bridge.insert_edge(ver[1], ver[2])  # B C
    g_bridge.insert_edge(ver[1], ver[5])  # B F
    g_bridge.insert_edge(ver[2], ver[3])  # C D
    g_bridge.insert_edge(ver[2], ver[6])  # C G
    g_bridge.insert_edge(ver[3], ver[6])  # D G
    g_bridge.insert_edge(ver[3], ver[7])  # D H
    g_bridge.insert_edge(ver[4], ver[5])  # E F
    g_bridge.insert_edge(ver[4], ver[8])  # E I
    g_bridge.insert_edge(ver[5], ver[8])  # F I
    g_bridge.insert_edge(ver[6], ver[9])  # G J
    g_bridge.insert_edge(ver[6], ver[10])  # G K
    g_bridge.insert_edge(ver[6], ver[11])  # G L
    g_bridge.insert_edge(ver[7], ver[11])  # H L
    g_bridge.insert_edge(ver[8], ver[9])  # I J
    g_bridge.insert_edge(ver[6], ver[8])  # G I
    g_bridge.insert_edge(ver[13], ver[14])  # N O
    g_bridge.insert_edge(ver[9], ver[10])  # J K
    g_bridge.insert_edge(ver[10], ver[13])  # K N
    g_bridge.insert_edge(ver[14], ver[15])  # O P
    g_bridge.insert_edge(ver[12], ver[13])  # M N
    g_bridge.insert_edge(ver[13], ver[16])  # N Q
    g_bridge.insert_edge(ver[15], ver[16])  # P Q

    m = g_bridge.edge_count()
    print("\nArchi", m, ":")
    for e in g_bridge.edges():
        print(e)

    b = DFS_complete_bridge_serio(g_bridge)
    print("\nQuesti sono i BRIDGE:")
    if len(b) == 0:
        print("Nessuno")
    for i in b:
        print(i)

    for i in b:

        g_bridge.remove_edge(i.endpoints()[0], i.endpoints()[1])
        if connected(g_bridge) is False:
            print("Test verificato.")

        else:
            print("TEST FALLITO !!")

        g_bridge.insert_edge(i.endpoints()[0], i.endpoints()[1])

    print("\n TEST SU N GRAFI RANDOM-------------------")
    inizio_tot = time.clock()
    N = 1000
    n = 17
    m = 25
    errori = 0
    successi = 0
    connessi = 0
    tempo_tot = 0
    while connessi < N:
        g1 = randomGraph(n, m)
        g_temp = g1

        if connected(g_temp):
            inizio = time.clock()
            connessi += 1
            print("GENERAZIONE GRAFO RANDOM: ", connessi, "\n")
            print("Numero dei vertici: ", n)
            print("Archi", m, ":")
            for e in g1.edges():
                print(e)

            b = DFS_complete_bridge_serio(g1)
            print("\nQuesti sono i BRIDGE:")
            if len(b) == 0:
                print("Nessuno")
            for i in b:
                print(i)

            for i in b:

                g_temp.remove_edge(i.endpoints()[0], i.endpoints()[1])
                if connected(g_temp) is False:
                    print("Test verificato.")
                    successi += 1
                else:
                    print("TEST FALLITO !!")
                    errori += 1
                g_temp.insert_edge(i.endpoints()[0], i.endpoints()[1])

            fine = time.clock()
            tempo_tot = tempo_tot + fine - inizio
            print("Tempo di esecuzione: ", fine - inizio, "secondi")

    print("\nLa funzione ha trovato con successo ", successi, "bridge, sbagliando ", errori, " volte. \nGrafi testati:",
          connessi)
    fine_tot = time.clock()
    print("Tempo di esecuzione totale: ", fine_tot - inizio_tot, "secondi")
    print("Tempo di esecuzione medio della funzione: ", tempo_tot / N, "secondi")

