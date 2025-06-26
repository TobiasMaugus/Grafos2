from pathlib import Path
import parte1_grafos as p1
import parte2_grafos as p2
import leitura_escrita as le
import time
import psutil
import melhoria

folder = Path('./Testes')          # pasta com os arquivos .dat de entrada
saida = Path('./Resultados')       # pasta para arquivos de saída
saida_melhorada = Path('./G9')  # pasta para arquivos de saída da melhoria
folder.mkdir(exist_ok=True)
saida.mkdir(exist_ok=True)

dados_metricas = dict()
freq_mhz = psutil.cpu_freq().current  # Frequência atual em MHz
freq_hz = freq_mhz * 1_000_000        # Converte para Hz

arquivos = []
custos = []
custos_melhorados = []
i=0

for file in folder.iterdir():
    if file.is_file() and file.suffix == '.dat':
        clock_inicio_total = time.perf_counter_ns()
        nomedoarquivo = Path(file).stem
        print(f"\nArquivo processando -> {file.name}")
        # Leitura e preparação
        vertices, edges, arcs, required_vertices, required_edges, required_arcs, num_veicles, capacity, depot_node, optimal_value, IdsReq, IdsReqEA = le.read_file(file)
        matriz_distancias = p1.matriz_menores_distancias(vertices, edges, arcs)
        matriz_pred = p1.matriz_predecessores(vertices, edges, arcs)
        # Deterministico
        rotas_deterministicas, tarefas = p2.orquestrar_clarke_wright(
            required_edges=required_edges,
            required_arcs=required_arcs,
            required_vertices=required_vertices,
            depot_node=depot_node,
            num_vehicles=num_veicles,
            capacity=capacity,
            matriz_distancias=matriz_distancias,
            matriz_predecessores=matriz_pred,
            seed=None,
            shuffle=False
        )
        clock_fim_det = time.perf_counter_ns()
        custo_deterministico = p2.custo_total_rotas(rotas_deterministicas, tarefas, matriz_distancias)

        total_tarefas = len(required_vertices) + len(required_edges) + len(required_arcs)
        if total_tarefas <= 33:
            num_exec = 30
        elif total_tarefas <= 70:
            num_exec = 20
        else:
            num_exec = 10

        #  Aleatorio
        rotas_aleatorias, melhor_seed, custo_aleatorio, clock_melhor_aleatorio = p2.rodar_varias_vezes(
            required_edges=required_edges,
            required_arcs=required_arcs,
            required_vertices=required_vertices,
            depot_node=depot_node,
            num_vehicles=num_veicles,
            capacity=capacity,
            matriz_distancias=matriz_distancias,
            matriz_predecessores=matriz_pred,
            clockInit=clock_inicio_total,
            num_execucoes= 0 #num_exec
        )

       

        #  Escolher melhor
        if custo_aleatorio < custo_deterministico:
            melhor_rotas = rotas_aleatorias
            melhor_custo = custo_aleatorio
            clock_melhor_solucao = clock_melhor_aleatorio
            dados_metricas[file.name] = melhor_seed
        else:
            melhor_rotas = rotas_deterministicas
            melhor_custo = custo_deterministico
            clock_melhor_solucao = clock_fim_det - clock_inicio_total
            dados_metricas[file.name] = -1

        melhor_tarefas = p2.extrair_tarefas(required_edges, required_arcs, required_vertices)

        #  Exportar solução
        nome_base = file.stem
        caminho_antigo = saida / f"sol-{nome_base}.dat"
        if caminho_antigo.exists():
            caminho_antigo.unlink()  # Apaga o arquivo

        # Salva o novo com o sufixo da melhor versão
        nome_saida = saida / f"sol-{nome_base}.dat"

        clock_fim_total = time.perf_counter_ns()
        clock_total = clock_fim_total - clock_inicio_total
        ciclos_estimados_total = int(clock_total * (freq_hz / 1_000_000_000))
        ciclos_estimados_melhor_sol = int(clock_melhor_solucao * (freq_hz / 1_000_000_000))

        le.export_dat(
            rotas=melhor_rotas,
            tarefas=melhor_tarefas,
            matriz_distancias=matriz_distancias,
            custo_total=melhor_custo,
            total_clock_referencia=ciclos_estimados_total,
            total_clock_local=ciclos_estimados_melhor_sol,
            nome_arquivo=nome_saida,
            IdsReq=IdsReq,
            IdsReqEA=IdsReqEA
        )
        #mostrar caminhos
        # p2.mostrar_caminho(
        #     rotas=melhor_rotas,
        #     tarefas=melhor_tarefas,
        #     matriz_distancias=matriz_distancias
        # )


    
    rotas_melhoradas = melhoria.melhorar_rotas_2opt(melhor_rotas, melhor_tarefas, depot_node, matriz_pred, matriz_distancias)
    clock_fim_melhoria = time.perf_counter_ns()
    clock_melhor_solucao_melhorado = clock_fim_melhoria - clock_inicio_total

    nome_saida_melhorada = saida_melhorada / f"sol-{nome_base}_melhorada.dat"
    clock_fim_total_melhorado = time.perf_counter_ns()
    clock_total_melhorado = clock_fim_total_melhorado - clock_inicio_total
    ciclos_estimados_total_melhorado = int(clock_total_melhorado * (freq_hz / 1_000_000_000))
    ciclos_estimados_melhor_sol_melhorado = int(clock_melhor_solucao_melhorado * (freq_hz / 1_000_000_000))
    le.export_dat(
        rotas=rotas_melhoradas,
        tarefas=melhor_tarefas,
        matriz_distancias=matriz_distancias,
        custo_total=p2.custo_total_rotas(rotas_melhoradas, melhor_tarefas, matriz_distancias),
        total_clock_referencia=ciclos_estimados_total_melhorado,
        total_clock_local=ciclos_estimados_melhor_sol_melhorado,
        nome_arquivo=nome_saida_melhorada,
        IdsReq=IdsReq,
        IdsReqEA=IdsReqEA
    )
    # p2.mostrar_caminho(
    #     rotas=rotas_melhoradas,
    #     tarefas=melhor_tarefas,
    #     matriz_distancias=matriz_distancias
    # )
    arquivos.append(file.name)
    custos.append(melhor_custo)
    custos_melhorados.append(p2.custo_total_rotas(rotas_melhoradas, melhor_tarefas, matriz_distancias))
    i+=1
    

media = (le.escrita_comparacao(arquivos, custos, custos_melhorados) * 100)
print (f'{media:.2f}%')
le.escrita_seeds(dados_metricas)
le.func_teste()