from TdP_collections.graphs.graph import Graph
from TdP_collections.graphs.shortest_paths import *
import random as rand


"""Il servizio di volanti della polizia prevede che una serie di pattuglie siano continuamente
in giro sul territorio per poter intervenire in casi di emergenza. Quando giunge una
richiesta di intervento, la centrale operativa individua le volanti che in quel momento
possono intervenire nel minor tempo possibile e le allerta via radio.
Il ministro ha deciso di dotare le centrali operative di tutte le città di un sistema
automatico, in funzione 24 ore al giorno, che registra le richieste di intervento, valuta il
tipo di emergenza, decide quante volanti far intervenire ed individua le volanti che si
trovano nella migliore posizione.
Implementare la funzione emergency_call(G, pos, v, k) che, preso in input un grafo
diretto e connesso G che rappresenta la rete stradale cittadina (i vertici sono gli incroci e
gli archi sono le strade), un dizionario pos che contiene la posizione delle volanti, il luogo
v dove intervenire ed il numero k di volanti richieste per l’intervento, individua le volanti
che devono essere allertate. Per semplicità si assuma che le volanti siano numerate da 1
a N, che stazionino sempre negli incroci e che il luogo dell’intervento sia un incrocio.
"""


class CityGraph(Graph):
    def __init__(self, direct):
        super().__init__(direct)

    def  invert_edges(self):
        self._outgoing, self._incoming = self._incoming , self._outgoing

    def emergency_call(self, pos, v, k):
        #appunti: provare ad invertire gli archi
        self.invert_edges()

        cloud = shortest_path_lengths(self, v)
        sol= []
        j=1
        #print("CLOUD",len(cloud))
        for vertex in cloud:
            if j > k:
                break
            #print(vertex, cloud[vertex])
            if vertex in pos:
                sol+=[[pos[vertex], vertex._element, cloud[vertex]], ]
                j+=1

        return sol


    def calling911(self, v):
        vertexlist = list(self.vertices())
        n_car = len(vertexlist)//3
        pos = {}
        for i in range(1,n_car+1):
            randvertex = vertexlist[rand.randint(0,len(vertexlist)-1)]
            pos[randvertex] = i
            vertexlist.remove(randvertex)
        print("Numero volanti disponibili", n_car)
        """
        for i in pos:
            print(i, pos[i])
        """
        typeEmergency = rand.randint(1,n_car)
        print("TypeEmergcency", typeEmergency)
        return self.emergency_call(pos,v,typeEmergency)


    def readFile(self, filename, node):
        vert = []
        for i in range(1, node+1):
            vert.append(self.insert_vertex(i))

        in_file = open(filename, "r")  # lettura da file
        testo = in_file.read()
        in_file.close()
        lettura = testo.splitlines()

        lenLettura = len(lettura)
        i = 2
        while i < lenLettura:
            endpoints = lettura[i].split(" ")  # inserisce i 2 estremi in un array di 2 elementi
            j = 0
            while vert[j]._element != int(endpoints[0]):
                j = j + 1
            z = 0
            while vert[z]._element != int(endpoints[1]):
                z = z + 1
            self.insert_edge(vert[j], vert[z], int(endpoints[2]))
            i = i + 1


###############
print("\n###### City 1 - 70 Incroci - 366 Strade ######")
city1 = CityGraph(True)
city1.readFile("city_map.txt", 70)
lista = list(city1.vertices())
pointEmergency = lista[rand.randint(0,len(lista)-1)]
solution = city1.calling911(pointEmergency)
print("\nCity 1")
print("\nRichiesta soccorso dall'incrocio: ",pointEmergency)
print("Volanti richieste:" , len(solution))

for elem in solution:
    print("\nInformazione volante:")
    print("Codice Volante:", elem[0], "\nPosizione di Partenza della volante:", elem[1], "\nDistanza della volante dal punto di emergenza:", elem[2])

print("\n###### City 2 - 6 Incroci - 7 Strade ######")
city2 = CityGraph(True)
city2.readFile("example.txt",6)
lista = list(city2.vertices())
pointEmergency = lista[rand.randint(0,len(lista)-1)]
solution = city2.calling911(pointEmergency)
print("\nCity 2")
print("\nRichiesta soccorso dall'incrocio: ",pointEmergency)
print("Volanti richieste:" , len(solution))

for elem in solution:
    print("\nInformazione volante:")
    print("Codice Volante:", elem[0], "\nPosizione di Partenza della volante:", elem[1], "\nDistanza della volante dal punto di emergenza:", elem[2])