import numpy as np

# Dados fictícios das áreas marinhas
areas = [
    {'nome': 'Área 1', 'biodiversidade': 80, 'vulnerabilidade': 60, 'conectividade': 70, 'custo': 50},
    {'nome': 'Área 2', 'biodiversidade': 70, 'vulnerabilidade': 85, 'conectividade': 55, 'custo': 40},
    {'nome': 'Área 3', 'biodiversidade': 90, 'vulnerabilidade': 70, 'conectividade': 80, 'custo': 70},
    {'nome': 'Área 4', 'biodiversidade': 60, 'vulnerabilidade': 75, 'conectividade': 65, 'custo': 30},
    {'nome': 'Área 5', 'biodiversidade': 75, 'vulnerabilidade': 90, 'conectividade': 85, 'custo': 60}
]

# Recursos disponíveis
recursos = 150

def calcular_valor_area(area):
    # Combina os critérios em um valor único (aqui usamos uma média ponderada simples)
    valor = 0.4 * area['biodiversidade'] + 0.3 * area['vulnerabilidade'] + 0.3 * area['conectividade']
    return valor

def alocar_recursos(areas, recursos):
    # Obtém o número de áreas
    n = len(areas)
    # Cria uma matriz de zeros para armazenar os resultados intermediários
    dp = np.zeros((n + 1, recursos + 1))
    
    # Preenchendo a tabela dp
    for i in range(1, n + 1):
        for w in range(1, recursos + 1):
            # Verifica se o custo da área atual cabe nos recursos disponíveis
            if areas[i - 1]['custo'] <= w:
                # Se couber, atualiza o valor máximo considerando se incluímos ou não a área atual
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - areas[i - 1]['custo']] + calcular_valor_area(areas[i - 1]))
            else:
                # Se não couber, o valor máximo é o mesmo da linha anterior
                dp[i][w] = dp[i - 1][w]
    
    # Determinando as áreas selecionadas
    w = recursos
    areas_selecionadas = []
    for i in range(n, 0, -1):
        # Verifica se o valor mudou ao incluir a área atual
        if dp[i][w] != dp[i - 1][w]:
            # Se mudou, adiciona a área atual à lista de áreas selecionadas
            areas_selecionadas.append(areas[i - 1])
            # Atualiza os recursos disponíveis subtraindo o custo da área atual
            w -= areas[i - 1]['custo']
    
    # Retorna o valor total otimizado e as áreas selecionadas
    return dp[n][recursos], areas_selecionadas

# Chama a função para alocar recursos e obter o valor total otimizado e as áreas selecionadas
valor_total, areas_selecionadas = alocar_recursos(areas, recursos)

# Imprime os resultados
print(f"Valor total otimizado: {valor_total}")
print("Áreas selecionadas para conservação:")
for area in areas_selecionadas:
    print(f" - {area['nome']} (Custo: {area['custo']}, Valor: {calcular_valor_area(area)})")
