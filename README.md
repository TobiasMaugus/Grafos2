# Trabalho Prático – Algoritmos em Grafos (GCC-218)

> **Instituição:** Universidade Federal de Lavras – UFLA  
> **Período:** 2025/1  
> **Professor:** Mayron Cesar de Oliveira  
> **Alunos:** Tobias Maugus Bueno Cougo e João Gabriel Salomão Baldim  
> **Linguagem:** Python 3.11  

---

## Descrição do Projeto

> Este projeto tem como objetivo a leitura e análise de instâncias de grafos representadas em arquivos `.dat`. Com base nessas instâncias, são calculadas rotas otimizadas que atendem a tarefas de serviço sobre vértices, arestas e arcos, utilizando o algoritmo de **Clarke-Wright Savings**.

---

##  Estrutura dos Arquivos

> - `main_grafos.py`: Executa a lógica principal do projeto, processando todos os arquivos da pasta `Testes`.
> - `leitura_escrita.py`: Funções auxiliares para ler os arquivos `.dat` e exportar soluções geradas.
> - `parte1_grafos.py`: Implementação de Dijkstra, matrizes de distâncias e predecessores.
> - `parte2_grafos.py`: Algoritmo de Savings, geração de rotas, e escolha da melhor solução.
> - `Testes/`: Contém os arquivos `.dat` com instâncias do problema.
> - `Resultados/`: Armazena os arquivos de saída gerados com as melhores soluções.
> - `seeds.dat`: Armazena oas seeds de melhor solução aleatória para cada instância.

---

## Como Executar?

> ### 1. Pré-requisitos
>>1. Python 3.11
>>2. Instalar as biblioteca `psutil` e `time` para calculo do clock de processador
>>3. Instalar a biblioteca `pathlib` para leitura

> ### 2. Rodar o Projeto
>>1. Coloque os arquivos `.dat` na pasta `Testes`.
>>2. Execute o script principal:
>>3. A saída com as melhores soluções será salva automaticamente na pasta `Resultados/`.
---

## Funcionalidades

>- Leitura completa de arquivos `.dat` estruturados.
>- Geração de matrizes de menor distância entre pares (via Dijkstra).
>- Execução do algoritmo **Clarke-Wright Savings**:
  >>- **Determinístico** (sem embaralhamento)
  >>- **Aleatório** (várias execuções com diferentes seeds, não esta sendo utilizado)
>- Geração de rotas otimizadas com base nas soluções encontradas.
>- Comparação entre soluções e exportação da melhor.
>- Melhoria de desempenho com o uso do algoritmo de 2opt
>- Cálculo de métricas de tempo em ciclos de CPU.
>- Exportação de seeds utilizadas em `seeds.dat`
---

## Formato do Arquivo .dat (leitura)
>- XX representa um valor inteiro qualquer e todo XX deve estar separado de outro por exatamente uma **tabulação(TAB).**  
>- N, E e A são letras (caracteres).  
>- Não se pode ter nada após o último arco.  
>- Todos os arquivos .dat deste repositório estão em formato adequado para teste.  
>>### Formato adequado de arquivo:
>```
>Name:           XX  
>Optimal value:  XX  
>#Vehicles:      XX  
>Capacity:       XX  
>Depot Node:     XX  
>#Nodes:         XX  
>#Edges:         XX  
>#Arcs:          XX  
>#Required N:    XX  
>#Required E:    XX  
>#Required A:    XX 
>
>ReN.  DEMAND  S. COST  
>NXX  XX  XX  
>
>ReE.  From N.  To N.  T. COST  DEMAND  S. COST  
>EXX  XX  XX  XX  XX  XX  
>
>EDGE  FROM N.  TO N.  T. COST  
>EXX  XX  XX  XX  
>
>ReA.  FROM N.  TO N.  T. COST  DEMAND  S. COST  
>AXX  XX  XX  XX  XX  XX  
>
>ARC  FROM N.  TO N.  T. COST  
>AXX  XX  XX  XX  

---

## Formato do Arquivo .dat (escrita)

> ### Cabeçalho:
>>- Custo total da solução
>>- Total de rotas
>>- Total de clocks para a execução do algoritmo
>>- Total de clocks para encontrar a solução
>### Em cada linha:
 >>- ` Índice_do_depósito(sempre zero)`
 >>- `dia_da_roteirização(no nosso caso, sempre 1)`
 >>- `identificador_da_rota(começando por 1)`
 >>- `demanda_total_da_rota custo_total_da_rota total_de_visitas(quantidade de visitas ao depósito + quantidade de visitas aos serviços)`
 >>- `(X i,j,k) ...`

### Explicação de (X i,j,k) 
>-  Na tripla `(X,i,j,k)` temos X como o tipo de vértice:
>>    - Se a rota está no vértice depósito, então tem-se:
>>         - (`D 0,1,1`)
>>- Se a rota está em um serviço, então tem-se:
>>  - (`S id_serviço,exterminadade_serviço,outra_extermidade_do_servico`).


> - Já para  `x,y,z` temos:
>>  - o serviço 14 do arquivo BHW1.dat corresponde à aresta requerida "E7	7	8	8	1	9". Logo, essa tripla na rota deve ser impressa assim:
>>    - ```(S 14,7,8)```, se o deslocamento tiver sendo feito do nó 7 para o nó 8

---

>## Exemplo de Saída (BHW1.dat)
>```
>337
>6
>14561498
>64474
>0 1 1 5 61  7 (D 0,1,1) (S 21,1,7) (S 14,7,8) (S 28,8,10) (S 3,10,10) (S 17,10,9) (D 0,1,1)
>0 1 2 5 65  7 (D 0,1,1) (S 22,1,10) (S 18,10,11) (S 5,11,11) (S 12,11,5) (S 6,12,12) (D 0,1,1)
>0 1 3 4 33  6 (D 0,1,1) (S 23,1,12) (S 15,12,7) (S 7,7,7) (S 26,7,6) (D 0,1,1)
>0 1 4 5 56  7 (D 0,1,1) (S 27,12,6) (S 11,6,5) (S 25,5,3) (S 24,3,4) (S 1,4,4) (D 0,1,1)
>0 1 5 5 58  7 (D 0,1,1) (S 19,1,2) (S 4,2,2) (S 10,2,9) (S 29,9,11) (S 16,11,8) (D 0,1,1)
>0 1 6 5 64  7 (D 0,1,1) (S 20,1,4) (S 9,4,2) (S 8,2,3) (S 2,3,3) (S 13,5,12) (D 0,1,1)


---

>## Créditos
>
>Projeto desenvolvido por:
>
>- **Tobias Maugus Bueno Cougo**
>- **João Gabriel Salomão Baldim**
>```
>Curso de Ciência da Computação – UFLA  
>2025/1
