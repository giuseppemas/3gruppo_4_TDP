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


def DFS_bridge(g, u, discovered, ordineVisita):

  for e in g.incident_edges(u):    # for every outgoing edge from u
    v = e.opposite(u)

    if v not in discovered:        # v is an unvisited vertex
      newEdge = Graph.Edge(u, v, None)
      ordineVisita.append(newEdge)
      discovered[v] = e            # e is the tree edge that discovered v
      DFS_bridge(g, v, discovered, ordineVisita)        # recursively explore from v

def DFS_complete_bridge(g):

  forest = {}
  ordineVisita = list()
  for u in g.vertices():
    if u not in forest:
      forest[u] = None             # u will be the root of a tree
      DFS_bridge(g, u, forest, ordineVisita)
  return forest, ordineVisita

def bridge(g):

    discovery = set()     # lista degli archi discovery
    back = list()          # lista di archi back
    bridge = set()        # lista degli archi che sono BRIDGE

    foresta, ordine = DFS_complete_bridge(g)

    # Salviamo in una lista tutti gli archi DISCOVERY, i quali sono tutti potenziali BRIDGE
    for v in g.vertices():
        if foresta[v] is not None:
            discovery.add(foresta[v])
            bridge.add(foresta[v])

    # Tutti gli archi che non sono DISCOVERY sono BACK
    for e in g.edges():
        if e not in discovery:
            back.append(e)

    for e in back:
        #print("BACK IN CICLO: ", e)
        v1 = e.endpoints()[0]
        v2 = e.endpoints()[1]
        start = None
        end = None
        noBridge = set()
        trovato = False

        for d in ordine:
            if trovato is True:
                continue
            #print("STATO: ", start, end, trovato, d)
            if d.endpoints()[0] == v1:
                start = v1
                end = v2
                noBridge.clear()
            elif d.endpoints()[0] == v2:
                start = v2
                end = v1


            if start is not None and not(trovato):
                if d.endpoints()[1] == end:
                    trovato = True
                rim = g.get_edge(d.endpoints()[0], d.endpoints()[1])
                noBridge.add(rim)

        bridge = bridge.difference(noBridge)  # O(len(m1) + len(m2))


    for i in ordine:
        print("ORDINE: ", i)
    for i in back:
        print("BACK: ", i)
    for i in bridge:
        print("BRIDGE: ", i)


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

    print("\n TEST SU N GRAFI RANDOM-------------------")
    inizio_tot = time.clock()
    N = 1
    n = 5
    m = 7
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

            b = bridge(g1)
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
    print("Tempo di esecuzione totale: ", fine_tot-inizio_tot,"secondi")
    print("Tempo di esecuzione medio della funzione: ", tempo_tot/N, "secondi")

