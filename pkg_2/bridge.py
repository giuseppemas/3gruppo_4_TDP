from pkg_1.MyGraph import MyGraph
from TdP_collections.graphs.dfs import DFS_complete
from TdP_collections.graphs.graph import Graph

"""
Preso in input un oggetto MyGraph G, restituisce un bridge di G oppure None se il grafo è biconnesso
"""
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

    for v in g.vertices():
        print("FORESTA: ",foresta[v], v)
    for i in ordine:
        print("ORDINE: ", i)

    # Salviamo in una lista tutti gli archi DISCOVERY, i quali sono tutti potenziali BRIDGE
    for v in g.vertices():
        if foresta[v] is not None:
            discovery.add(foresta[v])
            bridge.add(foresta[v])

    # Tutti gli archi che non sono DISCOVERY sono BACK
    for e in g.edges():
        if e not in discovery:
            back.append(e)

    for i in back:
        print("BACK: ", i)
    for i in discovery:
        print("DISCOVERY: ",i)
    for i in bridge:
        print("BRIDGE: ", i)

    for e in back:
        v1 = e.endpoints()[0]
        v2 = e.endpoints()[1]
        start = None
        end = None
        noBridge = set()
        trovato = False

        for d in ordine:
            if d.endpoints()[0] == v1:
                start = v1
                end = v2
                noBridge.clear()
            if d.endpoints()[0] == v2:
                start = v2
                end = v1

            if start is not None and not(trovato):
                print("Condizione: ", d, start, end)
                if d.endpoints()[1] == end:
                    trovato = True
                d = g.get_edge(d.endpoints()[0], d.endpoints()[1])
                noBridge.add(d)


        for i in noBridge:
            print("NOBRIDGE: ", i)
        for i in bridge:
            print("BRIDGE: ", i)
        bridge = bridge.difference(noBridge)

    return bridge

def randomGraph(n,m):
    pass

#---------------------------------------TESTING------------------------------------------------
g = MyGraph()
for i in range(6):
    g.insert_vertex(i+1)

vertici = list(g.vertices())

print("Questi sono i vertici:")
for i in range(len(vertici)):
    print(vertici[i], type(vertici[i]), end = "\n")

print("\n")

g.insert_edge(vertici[5],vertici[0])
g.insert_edge(vertici[0],vertici[3])
g.insert_edge(vertici[3],vertici[2])
g.insert_edge(vertici[1],vertici[3])
g.insert_edge(vertici[3],vertici[4])
g.insert_edge(vertici[5],vertici[4])

archi = list(g.edges())
print("Questi sono gli archi:")
for i in range(len(archi)):
    u,v = archi[i].endpoints()

    print(archi[i], type(archi[i]), type(u), type(v))

print("\nDEBUG:")
foresta = DFS_complete(g)
discovery = list()
for i in range(4):
    print(foresta[vertici[i]])
    discovery.append(foresta[vertici[i]])

print("Chiamata a funzione BRIDGE:")
b = bridge(g)
print("Questi sono i BRIDGE:")
for i in b:
    print(i)

