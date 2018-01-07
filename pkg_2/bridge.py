from TdP_collections.graphs.dfs import DFS_complete
from TdP_collections.graphs.graph import Graph
import random

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

        bridge = bridge.difference(noBridge)

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

#---------------------------------------TESTING------------------------------------------------

N = 100
n = 50
m = 70
errori = 0
successi = 0
connessi = 0
while connessi < N:
    g1 = randomGraph(n, m)
    g_temp = g1

    if connected(g_temp):
        print("GENERAZIONE GRAFO RANDOM: ", connessi + 1, "\n")
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

        connessi  += 1
        for i in b:

            g_temp.remove_edge(i.endpoints()[0], i.endpoints()[1])
            if connected(g_temp) is False:
                print("Test verificato.")
                successi += 1
            else:
                print("TEST FALLITO !!")
                errori += 1
            g_temp.insert_edge(i.endpoints()[0], i.endpoints()[1])

print("La funzione ha trovato con successo ", successi,"bridge, sbagliando ", errori," volte. \nGrafi connessi:", connessi)