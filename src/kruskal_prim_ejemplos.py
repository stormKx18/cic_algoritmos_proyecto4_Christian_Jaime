import datetime
import time
start_time = time.time()

x = datetime.datetime.now()
print(x)
'''
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

'''

'''
#******************************************************************************
from grafoGilbert import grafoGilbert
#******************************************************************************
#grafoGilbert - Pocos nodos
gfGilbert = grafoGilbert(n=20, p=0.1, dirigido=False, auto=False)
gfGilbert.display()
gfGilbert.graphviz()

#Kruskal directo
KruskalD=gfGilbert.KruskalD()
KruskalD.display()
KruskalD.graphviz()

#Kruskal Inverso
KruskalI=gfGilbert.KruskalI()
KruskalI.display()
KruskalI.graphviz()

#Prim
prim=gfGilbert.Prim()
prim.display()
prim.graphviz()


#grafoGilbert - Muchos nodos
gfGilbert = grafoGilbert(n=100, p=0.1, dirigido=False, auto=False)
gfGilbert.display()
gfGilbert.graphviz()

#Kruskal directo
KruskalD=gfGilbert.KruskalD()
KruskalD.display()
KruskalD.graphviz()

#Kruskal Inverso
KruskalI=gfGilbert.KruskalI()
KruskalI.display()
KruskalI.graphviz()

#Prim
prim=gfGilbert.Prim()
prim.display()
prim.graphviz()
'''

#******************************************************************************
from grafoGeografico import grafoGeografico
#******************************************************************************
#grafoGeografico - Pocos nodos
gfGeografico = grafoGeografico(n=30, r=0.3, dirigido=False, auto=False)
gfGeografico.display()
gfGeografico.graphviz()

#Kruskal directo
KruskalD=gfGeografico.KruskalD()
KruskalD.display()
KruskalD.graphviz()

#Kruskal Inverso
KruskalI=gfGeografico.KruskalI()
KruskalI.display()
KruskalI.graphviz()

#Prim
prim=gfGeografico.Prim()
prim.display()
prim.graphviz()

#grafoGeografico - Muchos nodos
gfGeografico = grafoGeografico(n=100, r=0.3, dirigido=False, auto=False)
gfGeografico.display()
gfGeografico.graphviz()

#Kruskal directo
KruskalD=gfGeografico.KruskalD()
KruskalD.display()
KruskalD.graphviz()

#Kruskal Inverso
KruskalI=gfGeografico.KruskalI()
KruskalI.display()
KruskalI.graphviz()

#Prim
prim=gfGeografico.Prim()
prim.display()
prim.graphviz()
#******************************************************************************
print("Execution time --- %s seconds ---" % round((time.time() - start_time),2))
