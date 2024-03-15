import sys
import numpy as np

class Grafo(): 
    #método construtor da classe
    def __init__(self, vertices): 
        self.V = vertices 
        self.grafo = [[0 for coluna in range(vertices)]  
                    for linha in range(vertices)] 
    #imprime a árvore geradora mínima no formato “Aresta - Distância”.
    def imprimirArvore(self, pai, nomes): 
        print("Aresta\t -\tDistância")
        for i in range(1, self.V): 
            print(nomes[pai[i]], "-", nomes[i], "\t", self.grafo[i][ pai[i] ])
    #Este método retorna o vértice com o valor de chave mínimo do conjunto de vértices ainda não incluídos
    def chaveMinima(self, chave, conjuntoMst): 
        minimo = sys.maxsize
        for v in range(self.V): 
            if chave[v] < minimo and conjuntoMst[v] == False: 
                minimo = chave[v] 
                indice_minimo = v 
        return indice_minimo 
    #É o principal método que implementa o algoritmo de Prim
    def prim(self, nomes): 
        chave = [sys.maxsize] * self.V 
        pai = [None] * self.V 
        chave[0] = 0 
        conjuntoMst = [False] * self.V 
        pai[0] = -1 
        for contador in range(self.V):  
            u = self.chaveMinima(chave, conjuntoMst)  
            conjuntoMst[u] = True
            for v in range(self.V):  
                if self.grafo[u][v] > 0 and conjuntoMst[v] == False and chave[v] > self.grafo[u][v]: 
                        chave[v] = self.grafo[u][v] 
                        pai[v] = u 
        self.imprimirArvore(pai, nomes)
# Exemplo de uso:
dicionario_grafo = {
    'Corrente': {'Teresina': 10, 'Parnaiba': 15, 'Luis Correia': 20},
    'Teresina': {'Corrente': 10, 'Parnaiba': 35, 'Luis Correia': 25},
    'Parnaiba': {'Corrente': 15, 'Teresina': 35, 'Luis Correia': 30},
    'Luis Correia': {'Corrente': 20, 'Teresina': 25, 'Parnaiba': 30},
}
#representa um grafo onde as chaves são os nomes dos vértices e os valores são dicionários 
#que representam os vértices conectados e suas distâncias
nomes = list(dicionario_grafo.keys())
matriz = np.zeros((len(nomes), len(nomes)))

for i, origem in enumerate(nomes):
    for j, destino in enumerate(nomes):
        if destino in dicionario_grafo[origem]:
            matriz[i, j] = dicionario_grafo[origem][destino]

g = Grafo(len(nomes)) 
#converte este dicionário em uma matriz 2D
g.grafo = matriz
#é usada para criar uma instância da classe e o algoritmo de Prim é executado
g.prim(nomes)


