# Investment Calculator

Simulador de investimento em renda fixa com aplicação de juros compostos e regras de negócio.

## 💻 Funcionalidades
- Cálculo de juros compostos mensais
- Penalidade para resgates antecipados (< 3 meses)
- Bônus para investimentos de longo prazo (>= 18 meses)
- Truncamento do valor final em duas casas decimais

## 📊 Fórmula utilizada
M = C * (1 + i)^t

## 🧠 Regras de negócio
- Menos de 3 meses: penalidade de 2%
- 18 meses ou mais: bônus de 0,5% antes dos juros
- Entre 3 e 17 meses: cálculo padrão

## 🚀 Como executar
```bash
python main.py
