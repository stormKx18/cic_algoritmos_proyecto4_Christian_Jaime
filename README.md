# Proyecto 4 - Algoritmos Kruskal y Prim

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

**INSTITUTO POLITÉCNICO NACIONAL**

**Centro de Investigación en Computación**

**PRESENTA** Victor Christian Jaime Tamayo

**BOLETA** A210232

**ASIGNATURA** Diseño y Análisis de Algoritmos

**PROFESOR** Dr. Rolando Quintero Téllez

**SEMESTRE** A21

**FECHA** 02 de Junio de 2021

---

## Instrucciones

Algoritmos de árbol de expansión mínima
Utilizando la biblioteca de grafos desarrollada en el proyecto 1, implementar los algoritmos de Kruskal (directo e inverso) y Prim de tal forma que calculen el árbol de expansión mínima; es decir, desarrollar los métodos en la clase Grafo:

- def KruskalD(self):
- def KruskalI(self):
- def Prim(self):

Entregables:
1. Repositorio GIT.
2. Archivos de grafos generados. Dos por cada generador (uno con "pocos" y otro con "muchos" nodos).
3. Archivos de grafos calculados.
4. Imágenes de la visualización de cada grafo (generados y calculados)
5. Capturas de pantalla donde se muestre el valor del MST

---

## Resultados

- **Archivos GV generados:** [graphviz](/graphviz)

- **Código fuente:** [src](/src)

- **Imágenes:** [img](/img)

- Se utilizó el siguiente script para generar todos los grafos de este proyecto: [kruskal_prim_ejemplos.py](/src/kruskal_prim_ejemplos.py)

---

## Modelo Gm,n de malla
- m: número de columnas
- n: número de filas
- dirigido: el grafo es dirigido

##

### Pocos nodos (Modelo Gm,n de malla)  [graphviz](/graphviz/grafoMalla_m_4_n_4.gv)
**m = 4, n = 4, dirigido = False**

<img src="/img/grafoMalla_m_4_n_4.png" width="500" />

> 16 Nodos y 24 Aristas

##

### Pocos nodos - Kruskal Directo (Modelo Gm,n de malla) [graphviz](/graphviz/grafoMalla_m_4_n_4_KruskalD.gv)
**m = 4, n = 4, dirigido = False**, nodo_raiz= 1

<img src="/img/grafoMalla_m_4_n_4_KruskalD.png" width="500" />

> 16 Nodos y 15 Aristas

##

### Muchos nodos (Modelo Gm,n de malla)  [graphviz](/graphviz/grafoMalla_m_25_n_4_labels.gv)
**m = 20, n = 10, dirigido = False**

<img src="/img/grafoMalla_m_25_n_4_labels.png" width="500" />

> 100 Nodos y 171 Aristas

##

### Muchos nodos - Dijkstra (Modelo Gm,n de malla) [graphviz](/graphviz/grafoMalla_m_25_n_4_Dijkstra__source_1_labels.gv)
**m = 20, n = 10, dirigido = False**, nodo_raiz= 1

<img src="/img/grafoMalla_m_25_n_4_Dijkstra__source_1_labels.png" width="500" />

> 100 Nodos y 99 Aristas

---

## Modelo Gn,m de Erdös y Rényi
- n: número de nodos (> 0)
- m: número de aristas (>= n-1)
- dirigido: el grafo es dirigido?
- auto: permitir auto-ciclos?

##

### Pocos nodos (Modelo Gn,m de Erdös y Rényi)  [graphviz](/graphviz/grafoErdosRenyi_n_20_m_30_labels.gv)
**n = 20, m = 30, dirigido = False, auto=False**

<img src="/img/grafoErdosRenyi_n_20_m_30_labels.png" width="500" />

> 20 Nodos y 30 Aristas

##

### Pocos nodos - Dijkstra (Modelo Gn,m de Erdös y Rényi) [graphviz](/graphviz/grafoErdosRenyi_n_20_m_30_Dijkstra__source_1_labels.gv)
**n = 20, m = 30, dirigido = False, auto=False**, nodo_raiz= 1

<img src="/img/grafoErdosRenyi_n_20_m_30_Dijkstra__source_1_labels.png" width="500" />

> 20 Nodos y 19 Aristas

##

### Muchos nodos (Modelo Gn,m de Erdös y Rényi)  [graphviz](/graphviz/grafoErdosRenyi_n_100_m_100_labels.gv)
**n = 100, m = 100, dirigido = False, auto=False**

<img src="/img/grafoErdosRenyi_n_100_m_100_labels.png" width="500" />

> 100 Nodos y 100 Aristas

##

### Muchos nodos - Dijkstra (Modelo Gn,m de Erdös y Rényi) [graphviz](/graphviz/grafoErdosRenyi_n_100_m_100_Dijkstra__source_1_labels.gv)
**n = 100, m = 100, dirigido = False, auto=False**, nodo_raiz= 1

<img src="/img/grafoErdosRenyi_n_100_m_100_Dijkstra__source_1_labels.png" width="500" />

> 100 Nodos y 82 Aristas

---

## Modelo Gn,p de **Gilbert**
- n: número de nodos (> 0)
- p: probabilidad de crear una arista (0, 1)
- dirigido: el grafo es dirigido?
- auto: permitir auto-ciclos?

##

### Pocos nodos (Modelo Gn,p de Gilbert)  [graphviz](/graphviz/grafoGilbert_n_30_p_10_labels.gv)
**n = 30, p = 0.1, dirigido = False, auto=False**

<img src="/img/grafoGilbert_n_30_p_10_labels.png" width="500" />

> 30 Nodos y 93 Aristas

##

### Pocos nodos - Dijkstra (Modelo Gn,p de Gilbert) [graphviz](/graphviz/grafoGilbert_n_30_p_10_Dijkstra__source_1_labels.gv)
**n = 30, p = 0.1, dirigido = False, auto=False**, nodo_raiz= 1

<img src="/img/grafoGilbert_n_30_p_10_Dijkstra__source_1_labels.png" width="500" />

> 30 Nodos y 29 Aristas

##

### Muchos nodos (Modelo Gn,p de Gilbert)  [graphviz](/graphviz/grafoGilbert_n_100_p_10_labels.gv)
**n = 100, p = 0.1, dirigido = False, auto=False**

<img src="/img/grafoGilbert_n_100_p_10_labels.png" width="500" />

> 100 Nodos y 939 Aristas

##

### Muchos nodos - Dijkstra (Modelo Gn,p de Gilbert) [graphviz](/graphviz/grafoGilbert_n_100_p_10_Dijkstra__source_1_labels.gv)
**n = 100, p = 0.1, dirigido = False, auto=False**, nodo_raiz= 1

<img src="/img/grafoGilbert_n_100_p_10_Dijkstra__source_1_labels.png" width="500" />

> 100 Nodos y 99 Aristas

---

## Modelo Gn,r **geográfico simple**
- n: número de nodos (> 0)
- r: distancia máxima para crear un nodo (0, 1)
- dirigido: el grafo es dirigido?
- auto: permitir auto-ciclos?

##

### Pocos nodos (Modelo Gn,r Geográfico simple)  [graphviz](/graphviz/grafoGeografico_n_30_r_3_labels.gv)
**n = 30, r = 0.3, dirigido = False, auto=False**

<img src="/img/grafoGeografico_n_30_r_3_labels.png" width="500" />

> 30 Nodos y 103 Aristas

##

### Pocos nodos - Dijkstra (Modelo Gn,r Geográfico simple) [graphviz](/graphviz/grafoGeografico_n_30_r_3_Dijkstra__source_1_labels.gv)
**n = 30, r = 0.3, dirigido = False, auto=False**, nodo_raiz= 1

<img src="/img/grafoGeografico_n_30_r_3_Dijkstra__source_1_labels.png" width="500" />

> 30 Nodos y 29 Aristas

##

### Muchos nodos (Modelo Gn,r Geográfico simple)  [graphviz](/graphviz/grafoGeografico_n_100_r_3_labels.gv)
**n = 100, r = 0.3, dirigido = False, auto=False**

<img src="/img/grafoGeografico_n_100_r_3_labels.png" width="500" />

> 100 Nodos y 1,102 Aristas

##

### Muchos nodos - Dijkstra (Modelo Gn,r Geográfico simple) [graphviz](/graphviz/grafoGeografico_n_100_r_3_Dijkstra__source_1_labels.gv)
**n = 100, r = 0.3, dirigido = False, auto=False**, nodo_raiz= 1

<img src="/img/grafoGeografico_n_100_r_3_Dijkstra__source_1_labels.png" width="500" />

> 100 Nodos y 99 Aristas

---

## Variante del modelo Gn,d **Barabási-Albert**
- n: número de nodos (> 0)
- d: grado máximo esperado por cada nodo (> 1)
- dirigido: el grafo es dirigido?
- auto: permitir auto-ciclos?

##

### Pocos nodos (Variante del modelo Gn,d Barabási-Albert)  [graphviz](/graphviz/grafoBarabasiAlbert_n_30_d_4_labels.gv)
**n = 30, d = 4, dirigido = False, auto=False**

<img src="/img/grafoBarabasiAlbert_n_30_d_4_labels.png" width="500" />

> 30 Nodos y 59 Aristas

##

### Pocos nodos - Dijkstra (Variante del modelo Gn,d Barabási-Albert) [graphviz](/graphviz/grafoBarabasiAlbert_n_30_d_4_Dijkstra__source_1_labels.gv)
**n = 30, d = 4, dirigido = False, auto=False**, nodo_raiz= 1

<img src="/img/grafoBarabasiAlbert_n_30_d_4_Dijkstra__source_1_labels.png" width="500" />

> 30 Nodos y 29 Aristas

##

### Muchos nodos (Variante del modelo Gn,d Barabási-Albert)  [graphviz](/graphviz/grafoBarabasiAlbert_n_100_d_4_labels.gv)
**n = 100, d = 4, dirigido = False, auto=False**

<img src="/img/grafoBarabasiAlbert_n_100_d_4_labels.png" width="500" />

> 100 Nodos y 198 Aristas

##

### Muchos nodos - Dijkstra (Variante del modelo Gn,d Barabási-Albert) [graphviz](/graphviz/grafoBarabasiAlbert_n_100_d_4_Dijkstra__source_1_labels.gv)
**n = 100, d = 4, dirigido = False, auto=False**, nodo_raiz= 1

<img src="/img/grafoBarabasiAlbert_n_100_d_4_Dijkstra__source_1_labels.png" width="500" />

> 100 Nodos y 99 Aristas

---

## Modelo Gn **Dorogovtsev-Mendes**
- n: número de nodos (≥ 3)
- dirigido: el grafo es dirigido?

##

### Pocos nodos (Modelo Gn Dorogovtsev-Mendes)  [graphviz](/graphviz/grafoDorogovtsevMendes_n_30_labels.gv)
**n = 30, dirigido = False**

<img src="/img/grafoDorogovtsevMendes_n_30_labels.png" width="500" />

> 30 Nodos y 58 Aristas

##

### Pocos nodos - Dijkstra (Modelo Gn Dorogovtsev-Mendes) [graphviz](/graphviz/grafoDorogovtsevMendes_n_30_Dijkstra__source_1_labels.gv)
**n = 30, dirigido = False**, nodo_raiz= 1

<img src="/img/grafoDorogovtsevMendes_n_30_Dijkstra__source_1_labels.png" width="500" />

> 30 Nodos y 29 Aristas

##

### Muchos nodos (Modelo Gn Dorogovtsev-Mendes)  [graphviz](/graphviz/grafoDorogovtsevMendes_n_100_labels.gv)
**n = 100, dirigido = False**

<img src="/img/grafoDorogovtsevMendes_n_100_labels.png" width="500" />

> 100 Nodos y 197 Aristas

##

### Muchos nodos - Dijkstra (Modelo Gn Dorogovtsev-Mendes) [graphviz](/graphviz/grafoDorogovtsevMendes_n_100_Dijkstra__source_1_labels.gv)
**n = 100, dirigido = False**, nodo_raiz= 1

<img src="/img/grafoDorogovtsevMendes_n_100_Dijkstra__source_1_labels.png" width="500" />

> 100 Nodos y 99 Aristas

---
