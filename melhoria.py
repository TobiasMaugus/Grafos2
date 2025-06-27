import parte2_grafos as p2

def aplicar_2opt_em_rota(rota, tarefas, depot_node, matriz_predecessores, matriz_distancias, max_sem_melhoria=15):
    tarefas_seq = rota['tarefas'][:]
    melhor_seq = tarefas_seq[:]
    melhor_rota_completa = p2.construir_rota_completa(tarefas, melhor_seq, depot_node, matriz_predecessores)
    melhor_custo = calcular_custo_rota_completa(melhor_rota_completa, matriz_distancias)

    sem_melhoria_count = 0
    while sem_melhoria_count < max_sem_melhoria:
        melhoria_feita = False
        n = len(melhor_seq)
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                if j - i == 1:
                    continue  # Ignora adjacentes

                nova_seq = melhor_seq[:i] + melhor_seq[i:j][::-1] + melhor_seq[j:]
                nova_rota_completa = p2.construir_rota_completa(tarefas, nova_seq, depot_node, matriz_predecessores)
                novo_custo = calcular_custo_rota_completa(nova_rota_completa, matriz_distancias)

                if novo_custo < melhor_custo:
                    melhor_seq = nova_seq
                    melhor_rota_completa = nova_rota_completa
                    melhor_custo = novo_custo
                    melhoria_feita = True
                    break  # First improvement
            if melhoria_feita:
                break

        if melhoria_feita:
            sem_melhoria_count = 0
        else:
            sem_melhoria_count += 1

    rota['tarefas'] = melhor_seq
    rota['rota_completa'] = melhor_rota_completa
    return rota



def calcular_custo_rota_completa(rota_completa, matriz_distancias):
    custo = 0
    for i in range(len(rota_completa) - 1):
        custo += matriz_distancias[rota_completa[i]][rota_completa[i+1]]
    return custo

def melhorar_rotas_2opt(rotas, tarefas, depot_node, matriz_predecessores, matriz_distancias):
    rotas_melhoradas = []
    for rota in rotas:
        rota_copia = rota.copy()
        rota_copia['tarefas'] = rota['tarefas'][:]
        rota_copia['rota_completa'] = rota['rota_completa'][:]
        rota_melhorada = aplicar_2opt_em_rota(rota_copia, tarefas, depot_node, matriz_predecessores, matriz_distancias)
        rotas_melhoradas.append(rota_melhorada)
    return rotas_melhoradas
