from pkg_1.MyGraph import MyGraph
from TdP_collections.graphs.dfs import DFS_complete
from TdP_collections.graphs.graph import Graph

"""
Preso in input un oggetto MyGraph G, restituisce un bridge di G oppure None se il grafo è biconnesso
"""

def DFS_bridge(g,u,discovered, back):

    for e in g.incident_edges(u):  # for every outgoing edge from u
        v = e.opposite(u)
        print("DFS: ",e)
        if v in discovered:
            if e not in back:
                back.append(e)
        elif v not in discovered:  # v is an unvisited vertex
            discovered[v] = e  # e is the tree edge that discovered v
            DFS_bridge(g, v, discovered, back)  # recursively explore from v





def DFS_complete_bridge(g):
  """Perform DFS for entire graph and return forest as a dictionary.

  Result maps each vertex v to the edge that was used to discover it.
  (Vertices that are roots of a DFS tree are mapped to None.)
  """
  forest = {}
  back = list()
  for u in g.vertices():
    if u not in forest:
      forest[u] = None             # u will be the root of a tree
      DFS_bridge(g, u, forest, back)
  return forest, back


def bridge(g):

    discovery = list()     # lista degli archi discovery
    back = list()          # lista di archi back
    visitati  = {}         # dict chiave:vertice, value: intero che rappresenta l'ordine di visita (1,2,3..)
    bridge = list()        # lista degli archi che sono BRIDGE

    foresta = DFS_complete(g)
    count = 1
    primo = True

    # Salviamo in una lista tutti gli archi DISCOVERY, i quali sono tutti potenziali BRIDGE
    for v in g.vertices():
        #print("TYPE_VERT: ", type(v))
        #print("funzione: ", foresta[v])
        if foresta[v] is None:
            continue

        if primo:
            visitati[foresta[v].endpoints()[0]] = count
            visitati[foresta[v].endpoints()[1]] = count + 1
            primo = False
            count += 1

        visitati[foresta[v].endpoints()[1]] = count
        count += 1

        discovery.append(foresta[v])
        bridge.append(foresta[v])

    # Tutti gli archi che non sono DISCOVERY sono BACK
    for e in g.edges():
        if e not in discovery:
            if visitati[e.endpoints()[0]] < visitati[e.endpoints()[1]]:
                # Se l'origine è stata visitata prima della destinazione inverto i vertici
                #print("INVERSIONE:", type(e.endpoints()[0]))
                newEdge = Graph.Edge(e.endpoints()[1], e.endpoints()[0], None)
                back.append(newEdge)
            else:
                back.append(e)

    for e in back:
        #print("Eliminazione dei BACK:")

        current_edge = foresta[e.endpoints()[0]]
        last_edge = foresta[e.endpoints()[1]]
        #print("ARCHI LIMITE: ", last_edge, current_edge)

        while current_edge is not last_edge:
            #print("ARCHI WHILE: ", last_edge, current_edge)
            #print("CANCELLO: ", current_edge)
            bridge.remove(current_edge)
            current_edge = foresta[current_edge.endpoints()[0]]

    return bridge



#---------------------------------------TESTING------------------------------------------------
g = MyGraph()
for i in range(4):
    g.insert_vertex(i+1)

vertici = list(g.vertices())

print("Questi sono i vertici:")
for i in range(len(vertici)):
    print(vertici[i], type(vertici[i]), end = "\n")

print("\n")

g.insert_edge(vertici[0],vertici[1])
g.insert_edge(vertici[0],vertici[2])
g.insert_edge(vertici[1],vertici[2])
g.insert_edge(vertici[2],vertici[3])

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

