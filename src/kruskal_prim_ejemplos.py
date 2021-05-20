import datetime
import time
start_time = time.time()

x = datetime.datetime.now()
print(x)

#******************************************************************************
from grafoMalla import grafoMalla
#******************************************************************************
#grafoMalla - Pocos nodos
gfMalla = grafoMalla(20,10,dirigido=False) #3,3
gfMalla.display()
gfMalla.graphviz()

KruskalD=gfMalla.KruskalD()
KruskalD.display()
KruskalD.graphviz()

KruskalI=gfMalla.KruskalI()
KruskalI.display()
KruskalI.graphviz()

prim=gfMalla.Prim()
prim.display()
prim.graphviz()

'''
#******************************************************************************
from grafoErdosRenyi import grafoErdosRenyi
#******************************************************************************
#grafoErdosRenyi - Pocos nodos
gfErdosReny = grafoErdosRenyi(n=20, m=30, dirigido=False, auto=False)
gfErdosReny.display()
gfErdosReny.graphviz()

KruskalD=gfErdosReny.KruskalD()
KruskalD.display()
KruskalD.graphviz()

KruskalI=gfErdosReny.KruskalI()
KruskalI.display()
KruskalI.graphviz()

prim=gfErdosReny.Prim()
prim.display()
prim.graphviz()


#******************************************************************************
'''
print("Execution time --- %s seconds ---" % round((time.time() - start_time),2))
