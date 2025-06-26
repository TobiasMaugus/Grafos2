import random
import parte1_grafos as p1
import time


def extrair_tarefas(required_edges, required_arcs, required_vertices):
    tarefas = []

    # Adicionando tarefas de arestas requeridas (ER)
    for (u, v), (t_cost, demand, s_cost) in required_edges:
        tarefas.append(
            {'tipo': 'edge', 'origem': u, 'destino': v, 'demanda': demand, 'custo_servico': s_cost, 't_cost': t_cost})

    # Adicionando tarefas de arcos requeridos (AR)
    for (u, v), (t_cost, demand, s_cost) in required_arcs:
        tarefas.append(
            {'tipo': 'arc', 'origem': u, 'destino': v, 'demanda': demand, 'custo_servico': s_cost, 't_cost': t_cost})

    # Adicionando tarefas de vértices requeridos (ReN)
    for node, (demand, s_cost) in required_vertices:
        tarefas.append({'tipo': 'vertice', 'origem': node, 'destino': node, 'demanda': demand, 'custo_servico': s_cost,
                        't_cost': 0})

    return tarefas


def calcula_custos_entre_tarefas(tarefas, matriz_distancias):
    custos = {}
    for i, t1 in enumerate(tarefas):
        for j, t2 in enumerate(tarefas):
            if i == j:
                continue
            origem_t1 = t1['destino'] if t1['tipo'] != 'vertice' else t1['origem']
            destino_t2 = t2['origem']
            custo = matriz_distancias[origem_t1][destino_t2] + t1['custo_servico'] + t2['custo_servico']
            custos[(i, j)] = custo
    return custos


def construir_rota_completa(tarefas, tarefa_indices, depot_node, matriz_predecessores):
    rota = [depot_node]
    for i, idx in enumerate(tarefa_indices):
        tarefa = tarefas[idx]
        origem = tarefa['origem']

        if i == 0:
            # Caminho do depósito até o início da primeira tarefa
            rota += p1.caminho_mais_curto_com_matriz(matriz_predecessores, rota[-1], origem)[1:]
        else:
            # Caminho do final da tarefa anterior até início da atual
            anterior = tarefas[tarefa_indices[i - 1]]
            ultimo = anterior['destino'] if anterior['tipo'] != 'vertice' else anterior['origem']
            rota += p1.caminho_mais_curto_com_matriz(matriz_predecessores, ultimo, origem)[1:]

        # Adiciona o deslocamento da tarefa
        if tarefa['tipo'] == 'vertice':
            pass  # vértice não tem deslocamento
        else:
            rota.append(tarefa['destino'])

    # Caminho de volta ao depósito
    ultimo = tarefas[tarefa_indices[-1]]
    fim = ultimo['destino'] if ultimo['tipo'] != 'vertice' else ultimo['origem']
    rota += p1.caminho_mais_curto_com_matriz(matriz_predecessores, fim, depot_node)[1:]
    return rota


def ordenar_savings(savings, rng=None):
    if rng is not None:
        rng.shuffle(savings)
    else:
        savings = sorted(savings, key=lambda x: x[1], reverse=True)
    return savings


def calcula_savings(tarefas, custos_entre_tarefas, matriz_distancias, deposito, capacidade_max):
    savings = []
    for i, t1 in enumerate(tarefas):
        for j, t2 in enumerate(tarefas):
            if i >= j:
                continue

            if (t1['demanda'] + t2['demanda']) > capacidade_max:
                continue

            custo_i0 = matriz_distancias[deposito][t1['origem']]
            custo_0j = matriz_distancias[t2['destino']][deposito] if t2['tipo'] != 'vertice' else matriz_distancias[t2['origem']][deposito]
            saving = custo_i0 + custo_0j - custos_entre_tarefas[(i, j)]
            savings.append(((t1['id'], t2['id']), saving))

    return savings


def inicializa_rotas(tarefas, num_vehicles, depot_node, capacity, matriz_predecessores):
    rotas = []

    if num_vehicles == -1:
        for tarefa in tarefas:
            if tarefa['demanda'] > capacity:
                continue
            rota_completa = construir_rota_completa(tarefas, [tarefa['id']], depot_node, matriz_predecessores)
            rotas.append({
                'tarefas': [tarefa['id']],
                'demanda': tarefa['demanda'],
                'rota_completa': rota_completa
            })
    else:
        for i in range(num_vehicles):
            rotas.append({'tarefas': [], 'demanda': 0, 'rota_completa': [depot_node]})
        for idx, tarefa in enumerate(tarefas):
            if tarefa['demanda'] > capacity:
                continue
            rota = rotas[idx % num_vehicles]
            if rota['demanda'] + tarefa['demanda'] <= capacity:
                rota['tarefas'].append(tarefa['id'])
                rota['demanda'] += tarefa['demanda']
                rota['rota_completa'] = construir_rota_completa(tarefas, rota['tarefas'], depot_node, matriz_predecessores)

    return rotas


def pode_fundir_rotas(rota_i, rota_j, capacidade_max):
    return (rota_i['demanda'] + rota_j['demanda']) <= capacidade_max


def funde_rotas(rota_i, rota_j, tarefas_dict, depot_node, matriz_predecessores):
    nova_tarefas = rota_i['tarefas'] + rota_j['tarefas']
    nova_rota = {
        'tarefas': nova_tarefas,
        'demanda': rota_i['demanda'] + rota_j['demanda'],
        'rota_completa': construir_rota_completa(tarefas_dict, nova_tarefas, depot_node, matriz_predecessores)
    }
    return nova_rota


def aplica_savings(rotas, savings, capacidade_max, tarefas_dict, depot_node, matriz_predecessores):
    for (id_i, id_j), _ in savings:
        rota_i = next((r for r in rotas if r['tarefas'] and r['tarefas'][-1] == id_i), None)
        rota_j = next((r for r in rotas if r['tarefas'] and r['tarefas'][0] == id_j), None)

        if rota_i and rota_j and rota_i != rota_j:
            if pode_fundir_rotas(rota_i, rota_j, capacidade_max):
                nova_rota = funde_rotas(rota_i, rota_j, tarefas_dict, depot_node, matriz_predecessores)
                rotas.remove(rota_i)
                rotas.remove(rota_j)
                rotas.append(nova_rota)
    return rotas


def orquestrar_clarke_wright(required_edges, required_arcs, required_vertices, depot_node, num_vehicles, capacity, matriz_distancias, matriz_predecessores, seed=None, shuffle=False):
    rng = random.Random(seed) if seed is not None else None

    tarefas = extrair_tarefas(required_edges, required_arcs, required_vertices)
    for i, t in enumerate(tarefas):
        t['id'] = i

    if shuffle and rng:
        rng.shuffle(tarefas)

    tarefas_dict = {t['id']: t for t in tarefas}

    custos_entre_tarefas = calcula_custos_entre_tarefas(tarefas, matriz_distancias)
    rotas = inicializa_rotas(tarefas, num_vehicles, depot_node, capacity, matriz_predecessores)
    savings = calcula_savings(tarefas, custos_entre_tarefas, matriz_distancias, depot_node, capacidade_max=capacity)
    savings_ordenados = ordenar_savings(savings, rng=rng)

    rotas = aplica_savings(rotas, savings_ordenados, capacity, tarefas_dict, depot_node, matriz_predecessores)
    return rotas, tarefas


def mostrar_caminho(rotas, tarefas, matriz_distancias):
    for idx, rota in enumerate(rotas):
        print(f"\nRota {idx + 1}:")

        # Mostra a sequência de nós visitados
        print("  Caminho completo:", " -> ".join(str(no) for no in rota['rota_completa']))

        # Mostra as tarefas realizadas
        print("  Tarefas:")
        for tarefa_idx in rota['tarefas']:
            tarefa = tarefas[tarefa_idx]
            tipo = tarefa['tipo']
            if tipo == 'vertice':
                print(f"    - {tipo} em {tarefa['origem']}, demanda {tarefa['demanda']}")
            else:
                print(f"    - {tipo} de {tarefa['origem']} para {tarefa['destino']}, demanda {tarefa['demanda']}")

        # Mostra a demanda total da rota
        print(f"  Demanda total: {rota['demanda']}")
        print(f"  Custo total: {custo_rota_especifica(rota, tarefas, matriz_distancias)}")

def custo_total_rotas(rotas, tarefas, matriz_distancias):
    """
    Soma o custo de todas as rotas.
    """
    custo_total = 0
    for rota in rotas:
        custo_total += custo_rota_especifica(rota, tarefas, matriz_distancias)
    return custo_total

def custo_rota_especifica(rota, tarefas, matriz_distancias):
    """
    Calcula o custo total da rota no MCARP considerando:
    - Arcos e arestas requeridos: custo de serviço na 1ª vez, custo de transporte nas vezes seguintes
    - Vértices requeridos: custo de serviço sempre, custo de transporte normal
    - Caminhos entre tarefas: custo de transporte sempre
    """
    custo_total = 0
    rota_completa = rota['rota_completa']
    tarefas_ids = rota['tarefas']
    tarefas_atendidas = set()

    # Soma custo de serviço (só 1x por tarefa requerida)
    for tarefa_id in tarefas_ids:
        tarefa = tarefas[tarefa_id]
        if tarefa_id not in tarefas_atendidas:
            custo_total += tarefa['custo_servico']
            tarefas_atendidas.add(tarefa_id)

    # Prepara mapeamento de arcos/arestas requeridos
    tarefas_por_arco = {}
    for tid, t in enumerate(tarefas):
        if t['tipo'] == 'arco':
            tarefas_por_arco[(t['origem'], t['destino'])] = tid
        elif t['tipo'] == 'aresta':
            tarefas_por_arco[(t['origem'], t['destino'])] = tid
            tarefas_por_arco[(t['destino'], t['origem'])] = tid

    # Soma custo de deslocamento na rota
    for i in range(len(rota_completa) - 1):
        origem = rota_completa[i]
        destino = rota_completa[i + 1]

        tarefa_id = tarefas_por_arco.get((origem, destino))
        if tarefa_id is not None and tarefa_id in rota['tarefas']:
            if tarefa_id in tarefas_atendidas:
                # Já atendida: custo de transporte
                custo_total += matriz_distancias[origem][destino]
            else:
                # Primeira vez: já somou custo de serviço, ignora transporte
                tarefas_atendidas.add(tarefa_id)
                continue
        else:
            # Não é tarefa requerida: custo normal
            custo_total += matriz_distancias[origem][destino]

    return custo_total



def rodar_varias_vezes(required_edges, required_arcs, required_vertices,
                       depot_node, num_vehicles, capacity,
                       matriz_distancias, matriz_predecessores, clockInit,
                       num_execucoes=10, master_seed=None):
    rng = random.Random(master_seed)

    melhor_custo = float('inf')
    melhor_seed = None
    melhor_rotas = None
    melhor_tarefas = None
    melhor_clock_sol = None

    for _ in range(num_execucoes):
        seed = rng.randint(0, 1_000_000)
        rotas, tarefas = orquestrar_clarke_wright(
            required_edges, required_arcs, required_vertices,
            depot_node, num_vehicles, capacity,
            matriz_distancias, matriz_predecessores,
            seed=seed, shuffle=True
        )
        custo = custo_total_rotas(rotas, tarefas, matriz_distancias)
        clock_solucao = time.perf_counter_ns()
        clock_solucao = clock_solucao-clockInit
        if custo < melhor_custo:
            melhor_custo = custo
            melhor_seed = seed
            melhor_rotas = rotas
            melhor_tarefas = tarefas
            melhor_clock_sol = clock_solucao

    return melhor_rotas, melhor_seed, melhor_custo, melhor_clock_sol



