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


    '''Funzione Greedy per il calcolo del vertex cover'''
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


    '''Funzione usata per i test'''
    def insert_edge(self, u, v, x=None):
        """Insert and return a new Edge from u to v with auxiliary element x.

        Raise a ValueError if u and v are not vertices of the graph.
        """
        if self.get_edge(u, v) is None:  # without error checking
            e = self.Edge(u, v, x)
            self._outgoing[u][v] = e
            self._incoming[v][u] = e


    '''Funzioni di Ricerca Esaustiva per il calcolo del min vertex cover'''

    def min_vertex_cover(self):
        E = set()
        for e in self.edges():
            E.add(e)
        return self.recursive_vertex_cover(E)


    def recursive_vertex_cover(self, E):
        if len(E) == 0:
            return {}
        uv = E.pop()
        u, v = uv.endpoints()
        E1 = E.copy()
        for e in E:
            if e._origin == u or e._destination == u:
                E1.remove(e)
        first = self.recursive_vertex_cover(E1)
        E2 = E.copy()
        for e in E:
            if e._origin == v or e._destination == v:
                E2.remove(e)
        second = self.recursive_vertex_cover(E2)
        if len(first) > len(second):
            second[v] = {}
            return second
        else:
            first[u] = {}
            return first