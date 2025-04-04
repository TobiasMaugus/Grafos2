## TRABALHO PRÁTICO DE ALGORITMOS EM GRAFOS

- **Disciplina:** Algoritmos em Grafos (GCC-218)
- **Professor:** Mayron Cesar de Oliveira
- **Instituição:** UFLA (2025)
- **Linguagem:** Python 3.11
- **Alunos:** Tobias Maugus Bueno Cougo e João Gabriel Salomão Baldim

## Descrição do Projeto
O programa foi desenvolvido para ler um arquivo (.dat) contendo informações sobre grafos e calcular as seguintes métricas:
- Quantidade de Vértices, arestas e arcos;
- Quantidade de Vértices, arestas e arcos requeridos;
- Densidade do Grafo (Order strenght): ((N. de arestas do grafo)+(N de arcos do grafo))/((N. max. de arestas que o grafo pode ter)+(N. max. de arcos que o grafo pode ter));
- Grau Min/Max dos vértices (quantidade de arestas/quantidade de arcos conectados aos vértices);
- Intermediação (Número de vezes que um Nó N aparece no caminho mais curto de um nó u qualquer para um nó v qualquer);
- Caminho Médio: (Somatório de todas as menores distâncias do grafo M)/(n × (n-1)), sendo n a quantidade de vértices no grafo M;
- Diâmetro: a "maior menor" distância presente no grafo.

## Formato do Arquivo .dat
- O arquivo de entrada deve seguir o seguinte formato (XX representa um valor inteiro qualquer
e todo XX deve estar separado de outro por exatamente uma tabulação(TAB)):

Name:           XX  
Optimal value:  XX  
#Vehicles:      XX  
Capacity:       XX  
Depot Node:     XX  
#Nodes:         XX  
#Edges:         XX  
#Arcs:          XX  
#Required N:    XX  
#Required E:    XX  
#Required A:    XX 

ReN.  DEMAND  S. COST  
XX  XX  XX  

ReE.  From N.  To N.  T. COST  DEMAND  S. COST  
XX  XX  XX  XX  XX  XX  

EDGE  FROM N.  TO N.  T. COST  
XX  XX  XX  XX  

ReA.  FROM N.  TO N.  T. COST  DEMAND  S. COST  
XX  XX  XX  XX  XX  XX  

ARC  FROM N.  TO N.  T. COST  
XX  XX  XX  XX  

## Como Usar
1. Python 3.11 instalado.
2. Execute o programa passando o endereço/nome do arquivo .dat como input no terminal.
3. O programa irá processar o arquivo e exibir as métricas calculadas como saída no terminal.

## Autores
- Tobias Maugus Bueno Cougo
- João Gabriel Salomão Baldim
