## TRABALHO PRÁTICO DE ALGORITMOS EM GRAFOS

- **Disciplina:** Algoritmos em Grafos (GCC-218)
- **Professor:** Mayron Cesar de Oliveira
- **Instituição:** UFLA (2025-1)
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
- É importante afirmar que todas as métricas utilizam o **"t_cost"**, ou seja, custo de transporte como peso para arestas e arcos.

## Formato do Arquivo .dat
- XX representa um valor inteiro qualquer e todo XX deve estar separado de outro por exatamente uma tabulação(TAB).  
- N, E e A são letras (caracteres).  
- Não se pode ter nada após o último arco.  
- Todos os arquivos .dat deste repositório estão em formato adequado para teste.  
- Segue o formato adequado de arquivo:  

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
NXX  XX  XX  

ReE.  From N.  To N.  T. COST  DEMAND  S. COST  
EXX  XX  XX  XX  XX  XX  

EDGE  FROM N.  TO N.  T. COST  
EXX  XX  XX  XX  

ReA.  FROM N.  TO N.  T. COST  DEMAND  S. COST  
AXX  XX  XX  XX  XX  XX  

ARC  FROM N.  TO N.  T. COST  
AXX  XX  XX  XX  

## Como Usar

- &emsp; Existem 2 arquivos no projeto (`Metrics.py` e `Metrics.ipynb`). Eles são basicamente o mesmo arquivo, com  
&emsp;&emsp;a diferença sendo majoritariamente as suas saídas, de modo que o arquivo `Metrics.py` consegue mostrar todas as  
&emsp;&emsp;métricas de um único arquivo (informado pelo usuário) via terminal.  

- &emsp; Já o arquivo `Metrics.ipynb` lê, por padrão, todos os arquivos que estão dentro da pasta `Testes`.  
&emsp;&emsp;`Testes` = (coleção de 20 arquivos das instâncias teste passadas pelo professor).  
&emsp;&emsp;Com isso, as métricas de todos os arquivos são lidas e mostradas na saída do Jupyter Notebook.  

- &emsp; Além disso, o arquivo `Metrics.ipynb` gera uma tabela de Excel com as principais métricas dos arquivos lidos.  
&emsp;&emsp;(Nessa tabela, os únicos graus mostrados são os totais e ela não possui as intermediações dos vértices, pois a  
&emsp;&emsp;leitura ficaria muito prejudicada. Então, caso queira ver os outros tipos de graus e a intermediação, vá até a  
&emsp;&emsp;saída do Jupyter Notebook, onde tais métricas são mostradas normalmente.)

**1 - Caso queira rodar Metrics.ipynb**  
&emsp;**1.1** Um kernel python válido instalado para executar o arquivo Metrics.ipynb em Jupyter Notebook.  
&emsp;**1.2** Ter as biliotecas pandas, pathlib, heapq e o pacote openpyxl instalados.  
&emsp;**1.3** Execute o arquivo e as métricas dos arquivos aparecerão no Jupyter Notebook  
&emsp;e a tabela do Excel será baixada.

**2 - Caso queira rodar Metrycs.py**  
&emsp;**2.1** Ter Python 3.11 instalado.  
&emsp;**2.2** Execute o programa passando o endereço/nome do arquivo .dat como input no terminal.  
&emsp;**2.3** O programa irá processar o arquivo e exibir as métricas calculadas como saída.  

## Autores
- Tobias Maugus Bueno Cougo
- João Gabriel Salomão Baldim
