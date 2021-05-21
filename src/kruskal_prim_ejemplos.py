import datetime
import time
start_time = time.time()

x = datetime.datetime.now()
print(x)

#******************************************************************************
from grafoMalla import grafoMalla
#******************************************************************************
#grafoMalla - Pocos nodos
gfMalla = grafoMalla(4,4,dirigido=False) #3,3
gfMalla.display()
gfMalla.graphviz()

#Kruskal directo
KruskalD=gfMalla.KruskalD()
KruskalD.display()
KruskalD.graphviz()

#Kruskal Inverso
KruskalI=gfMalla.KruskalI()
KruskalI.display()
KruskalI.graphviz()

#Prim
prim=gfMalla.Prim()
prim.display()
prim.graphviz()

#grafoMalla - Muchos nodos
gfMalla = grafoMalla(20,10,dirigido=False) #3,3
gfMalla.display()
gfMalla.graphviz()

#Kruskal directo
KruskalD=gfMalla.KruskalD()
KruskalD.display()
KruskalD.graphviz()

#Kruskal Inverso
KruskalI=gfMalla.KruskalI()
KruskalI.display()
KruskalI.graphviz()

#Prim
prim=gfMalla.Prim()
prim.display()
prim.graphviz()

'''

#******************************************************************************
from grafoErdosRenyi import grafoErdosRenyi
#******************************************************************************
#grafoErdosRenyi - Pocos nodos
gfErdosReny = grafoErdosRenyi(n=16, m=30, dirigido=False, auto=False)
gfErdosReny.display()
gfErdosReny.graphviz()

#Kruskal directo
KruskalD=gfErdosReny.KruskalD()
KruskalD.display()
KruskalD.graphviz()

#Kruskal Inverso
KruskalI=gfErdosReny.KruskalI()
KruskalI.display()
KruskalI.graphviz()

#Prim
prim=gfErdosReny.Prim()
prim.display()
prim.graphviz()

#grafoErdosRenyi - Muchos nodos
gfErdosReny = grafoErdosRenyi(n=100, m=500, dirigido=False, auto=False)
gfErdosReny.display()
gfErdosReny.graphviz()

#Kruskal directo
KruskalD=gfErdosReny.KruskalD()
KruskalD.display()
KruskalD.graphviz()

#Kruskal Inverso
KruskalI=gfErdosReny.KruskalI()
KruskalI.display()
KruskalI.graphviz()

#Prim
prim=gfErdosReny.Prim()
prim.display()
prim.graphviz()

#******************************************************************************
'''
print("Execution time --- %s seconds ---" % round((time.time() - start_time),2))
