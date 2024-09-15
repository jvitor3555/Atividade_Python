import json

# Abrindo o arquivo JSON em modo leitura
with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)  # Carrega o conteúdo do arquivo JSON para a variável dados

# Remove os dias com valor zero
dados_filtrados = [item for item in dados if item['valor'] > 0]

# Verifica se a lista filtrada está vazia
if not dados_filtrados:
    print("Nenhum valor positivo encontrado.")
else:
    # Encontrando o maior e o menor valor
    maior_valor = max(item['valor'] for item in dados_filtrados)
    menor_valor = min(item['valor'] for item in dados_filtrados)

    # Calculando a média dos valores
    total_valores = sum(item['valor'] for item in dados_filtrados)
    media_valores = total_valores / len(dados_filtrados)

    # Encontrando os dias que têm valores superiores à média
    dias_acima_da_media = [item['dia'] for item in dados_filtrados if item['valor'] > media_valores]

    # Exibindo os resultados
    print("Maior valor:", maior_valor)
    print("Menor valor:", menor_valor)
    print("Média dos valores:", media_valores)
    print("Dias que superam a média:", dias_acima_da_media)

        
    
