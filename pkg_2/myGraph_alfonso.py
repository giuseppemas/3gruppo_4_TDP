from pkg_1.MyGraph import MyGraph

g = MyGraph()

for i in range(4):
    g.insert_vertex(i+1)

print(g.vertices())
#g.insert_edge(g.vertices()[0],g.vertices()[1])
