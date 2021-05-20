import datetime
x = datetime.datetime.now()
print(x)
#******************************************************************************
nodo_raiz=1
print('nodo_raiz: ',nodo_raiz)
#******************************************************************************
from grafoMalla import grafoMalla
#******************************************************************************
#grafoMalla - Pocos nodos
gfMalla = grafoMalla(3,3,dirigido=False)
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

prim=gfErdosReny.Prim()
prim.display()
prim.graphviz()


#******************************************************************************
'''
