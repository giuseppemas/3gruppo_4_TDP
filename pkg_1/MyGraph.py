from TdP_collections.graphs.graph import Graph

'''
Valutare sperimentalmente le prestazioni dei due metodi su un campione di almeno k grafi (con k > 50)
con n vertici (n > 50) scelti a caso. Per ciascun grafo fornire le dimensioni dei vertex cover
restituiti dai due metodi ed i relativi tempi di esecuzione. Calcolare di quanto in media l’algoritmo
greedy è più veloce rispetto all’algoritmo ottimo e di quanto il vertex cover restituito è più grande.
'''

class MyGraph (Graph):

    def __init__(self):
        super(MyGraph, self).__init__()


    def min_vertex_cover(self):
        n = self.vertex_count()
        previousSol = {}
        for v in self.vertices():
            previousSol[v] = {}
        previousCount = n
        vertexCover = {}
        E = list()

        for i in range(1, n):
            lastCount = 0
            for e in self.edges():
                E.append(e)

            while len(E) != 0:
                if len(E) > i:
                    e = E.pop(i)                    #l'arco viene già eliminato
                else:
                    e = E.pop()
                u, v = e.endpoints()
                deg_u = self.degree(u)
                deg_v = self.degree(v)
                if (deg_u > 1 and deg_u > deg_v) or deg_v == 1:
                    vertexCover[u] = {}             #u copre almeno due archi quindi lo inserisce nella soluzione
                    lastCount = lastCount + 1
                    for e in E.copy():
                        if e._origin == u or e._destination == u:
                            E.remove(e)
                else:                               #v copre almeno due archi
                    vertexCover[v] = {}             #lo inserisce nella soluzione
                    lastCount = lastCount + 1
                    for e in E.copy():
                        if e._origin == v or e._destination == v:
                            E.remove(e)

            if lastCount < previousCount:
                previousCount = lastCount
                del(previousSol)
                previousSol = {}
                for v in vertexCover.keys():
                    previousSol[v] = {}
            del(vertexCover)
            vertexCover = {}

        return previousSol


    def greedy_vertex_cover(self):
        vertexCover = {}
        E = set()
        for e in self.edges():
            E.add(e)
        while len(E) != 0:
            e = E.pop()
            u, v = e.endpoints()                    #assegno ad u e v i due estremi dell'arco
            vertexCover[u] = {}
            vertexCover[v] = {}
            for e in E.copy():                      #se in E sono presenti archi incidenti di u o di v
                if e._origin == u or e._origin == v or e._destination == u or e._destination == v:
                    E.remove(e)                     #li rimuove
        return vertexCover

    def insert_edge(self, u, v, x=None):
        """Insert and return a new Edge from u to v with auxiliary element x.

        Raise a ValueError if u and v are not vertices of the graph.
        """
        if self.get_edge(u, v) is None:  # without error checking
            e = self.Edge(u, v, x)
            self._outgoing[u][v] = e
            self._incoming[v][u] = e