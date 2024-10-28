import json

def calcular_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)

    faturamento = [dia['valor'] for dia in dados['faturamento'] if dia['valor'] > 0]

    if not faturamento:
        return None, None, 0

    menor_valor = min(faturamento)
    maior_valor = max(faturamento)
    media = sum(faturamento) / len(faturamento)
    
    dias_acima_da_media = sum(1 for valor in faturamento if valor > media)

    return menor_valor, maior_valor, dias_acima_da_media

def main():
    arquivo_json = 'faturamento.json'
    
    menor_valor, maior_valor, dias_acima_da_media = calcular_faturamento(arquivo_json)
    
    if menor_valor is not None and maior_valor is not None:
        print(f"Menor valor de faturamento: {menor_valor}")
        print(f"Maior valor de faturamento: {maior_valor}")
        print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
    else:
        print("Não há dados de faturamento disponíveis.")

if __name__ == "__main__":
    main()
