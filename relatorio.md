# Relatório das Funções de cada Arquivo
## main_grafos.py
`Script principal de execução. Orquestra a leitura dos dados, execução dos algoritmos, aplicação de melhorias e exportação dos resultados.`

### Principais etapas e funções utilizadas:
- **Leitura dos arquivos de entrada usando `le.read_file`**
- **Construção das matrizes de distâncias e predecessores com `p1.matriz_menores_distancias` e `p1.matriz_predecessores`**
- **Execução do algoritmo de Clarke-Wright (determinístico e aleatório) via `p2.orquestrar_clarke_wright` e `p2.rodar_varias_vezes`**
- **Exportação dos resultados com `le.export_dat`**
- **Aplicação de melhoria 2-opt nas rotas com `melhoria.melhorar_rotas_2opt`**
- **Geração de relatórios de comparação e seeds com `le.escrita_comparacao` e `le.escrita_seeds`**

## parte1_grafos.py
`Contém Algoritmos para cálculo de caminhos mínimos e construção de matrizes auxiliares.`

### Funções :
- dijkstra: 
> Implementa o algoritmo de Dijkstra para encontrar as menores distâncias e predecessores a partir de um nó inicial.

- matriz_menores_distancias:
> Gera uma matriz de menores distâncias entre todos os pares de vértices.

- matriz_predecessores:
> Gera uma matriz de predecessores para reconstrução dos caminhos mínimos.

- caminho_mais_curto_com_matriz:
> Reconstrói o caminho mais curto entre dois nós usando a matriz de predecessores.

## parte2_grafos.py
`Implementa o algoritmo de Clarke-Wright, funções auxiliares para manipulação de rotas e tarefas, e execução de múltiplas rodadas aleatórias.`

### Funções
- extrair_tarefas:
> Constrói a lista de tarefas a partir das arestas, arcos e vértices requeridos.

- calcula_custos_entre_tarefas:
> Calcula o custo de deslocamento entre todas as tarefas.

- construir_rota_completa:
> Gera a sequência completa de nós visitados em uma rota, incluindo caminhos mínimos entre tarefas.

- ordenar_savings:
> Ordena ou embaralha a lista de savings para o algoritmo de Clarke-Wright.

- calcula_savings:
> Calcula os savings (economias) para todos os pares de tarefas.

- inicializa_rotas:
> Inicializa as rotas, atribuindo tarefas aos veículos.

- pode_fundir_rotas:
> Verifica se duas rotas podem ser fundidas sem exceder a capacidade.

- funde_rotas:
> Funde duas rotas em uma única rota.

- aplica_savings:
> Aplica o algoritmo de savings para fundir rotas e reduzir custos.

- orquestrar_clarke_wright:
> Orquestra todo o processo do algoritmo de Clarke-Wright, retornando as rotas e tarefas.

- mostrar_caminho:
> Exibe no console as rotas, tarefas e custos.

- custo_total_rotas:
> Soma o custo de todas as rotas.

- custo_rota_especifica:
> Calcula o custo de uma rota específica.

- rodar_varias_vezes:
> Executa múltiplas rodadas do algoritmo com diferentes seeds para buscar melhores soluções.
## melhoria.py :
`Implementa heurísticas de melhoria local (2-opt) para rotas.`

### Funções:
- aplicar_2opt_em_rota:
> Aplica a heurística 2-opt em uma rota para tentar reduzir o custo total, invertendo segmentos da sequência de tarefas.

- calcular_custo_rota_completa:
>Calcula o custo total de uma rota completa, somando as distâncias entre os nós consecutivos.

- melhorar_rotas_2opt
> Aplica a melhoria 2-opt em todas as rotas de uma solução, retornando as rotas melhoradas.

## leitura_escrita.py :
`Responsável pela leitura dos arquivos de entrada, exportação dos resultados e geração de arquivos auxiliares.`

### Funções:
 - read_file: 
>  Lê um arquivo de instância e extrai informações como: vértices, arestas, arcos, tarefas requeridas, parâmetros do problema e dicionários de IDs, as retorna para utilização no código

- export_dat:
> Exporta a solução encontrada para um arquivo .dat no formato especificado, incluindo rotas, tarefas, custos e métricas de clock.

- escrita_seeds:
> Salva no arquivo "seeds.dat", caso a melhoria aleatória da heurística seja utilizada, as seeds utilizadas para cada arquivo de entrada, facilitando a reprodutibilidade dos resultados.

- escrita_comparacao :
> Gera um arquivo de comparação entre custos antes e depois da melhoria, calculando o percentual médio de melhoria.