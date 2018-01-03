from TdP_collections.graphs.graph import Graph
from array import array

class MyGraph (Graph):

    def __init__(self):
        super(MyGraph, self).__init__()


    def min_vertex_cover(self):
        n = self.vertex_count()
        sol = array('i')
        vertexCover = {}
        E = set()
        for e in self.edges():
            E.add(e)
        for i in range(1, n):
            while len(E) != 0:
                count = 0
                e = E.pop()                         #l'arco viene già eliminato
                u, v = e.endpoints()
                print (u, v)
                deg_u = self.degree(u)
                deg_v = self.degree(v)
                print ("deg_u: ", deg_u, ", deg_v", deg_v)
                if (deg_u > 1 and deg_u > deg_v) or deg_v == 1:
                    vertexCover[u] = {}             #u copre almeno due archi quindi lo inserisce nella soluzione
                    count = count + 1
                    for e in E.copy():
                        if e._origin == u or e._destination == u:
                            print (e)
                            E.remove(e)
                else:                               #v copre almeno due archi
                    vertexCover[v] = {}             #lo inserisce nella soluzione
                    count = count + 1
                    for e in E.copy():
                        if e._origin == v or e._destination == v:
                            E.remove(e)
            sol[i].append(count)
            sol[i].append(vertexCover)
        i = 0
        min = sol[i]
        for i in range (1, n-1):
            if min[0]>sol[i][0]:
                min = sol[i]
        return min[1]


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
