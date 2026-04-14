def calcular_montante(capital, taxa, meses):
  if meses < 3: 
    penalidade = 0.02 * capital 
    montante = capital - penalidade 
    return montante
    
  elif meses >= 18: 
    bonus = 0.005 * capital
    capital += bonus
      
  montante = capital * ((1 + taxa) ** meses)
  return montante
    

def truncar_duas_casas(valor): 
  valor_truncado = int(valor * 100) / 100 
  return valor_truncado

capital_inicial = float(input('Capital principal inicial:')) 
taxa_juros = float(input('Taxa de juros mensal (em formato decimal):')) 
duracao_meses = int(input('Duração do investimento em meses:'))

montante = calcular_montante(capital_inicial, taxa_juros, duracao_meses)
print(f"Montante final: {truncar_duas_casas(montante)}")
