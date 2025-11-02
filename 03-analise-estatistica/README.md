# Projeto 03: Análise Estatística do E-commerce Olist

## Objetivo
Demonstrar habilidades em análise estatística aplicada usando Python para realizar testes de hipóteses, análise de correlações e inferências estatísticas sobre o dataset Brazilian E-commerce.

## Dataset
Brazilian E-commerce by Olist (mesmo dataset dos projetos anteriores)

## Habilidades Demonstradas
- Estatística descritiva avançada
- Testes de hipóteses paramétricos e não-paramétricos
- Análise de correlações (Pearson, Spearman, Kendall)
- Intervalos de confiança
- Testes de normalidade (Shapiro-Wilk, Kolmogorov-Smirnov)
- Tamanho do efeito (Cohen's d)
- Significância estatística
- Interpretação de resultados

## Tecnologias
- Python 3.x
- SciPy
- StatsModels
- NumPy
- Pandas
- Matplotlib/Seaborn

## Estrutura do Projeto

### `notebooks/`
- `03_analise_estatistica_olist.ipynb` - Notebook principal com análise estatística completa

### `scripts/`
- `analise_estatistica.py` - Funções reutilizáveis para análise estatística

### `data/`
- Links para datasets (usar mesmo dos projetos anteriores)

## Análises Estatísticas Realizadas

### 1. Análise de Distribuição dos Preços
- **Assimetria**: 7.923 (forte assimetria positiva)
- **Curtose**: 120.828 (distribuição leptocúrtica)
- **Teste de normalidade**: Dados não normais (p ≈ 0)
- **Intervalo de confiança 95%**: R$ 119.58 - R$ 121.73

### 2. Análise de Correlações
- **Preço vs Frete**: 
  - Pearson: 0.414 (p ≈ 0)
  - Spearman: 0.434 (p ≈ 0)
  - Kendall: 0.301 (p ≈ 0)
- **Todas as correlações estatisticamente significativas**

### 3. Testes de Hipóteses (SP vs RJ)
- **Teste t de Welch**: t = -8.922, p ≈ 0
- **Teste Mann-Whitney**: U = 315,629,730, p ≈ 0
- **Diferença**: RJ tem preços 14% maiores que SP
- **Tamanho do efeito**: Cohen's d = -0.091 (muito pequeno)

### 4. Significância Estatística
- Todas as diferenças e correlações são altamente significativas
- Grande tamanho amostral confere alta confiança estatística

## Scripts Reutilizáveis

### `analise_estatistica.py`
Contém funções modularizadas para:
- `analise_distribuicao()` - Estatísticas descritivas avançadas
- `teste_correlacoes()` - Múltiplos tipos de correlação
- `teste_hipoteses_duas_amostras()` - Testes paramétricos e não-paramétricos
- `interpretar_resultados()` - Interpretação automática

## Como Usar os Scripts

```python
from scripts.analise_estatistica import analise_distribuicao, teste_hipoteses_duas_amostras

# Análise de distribuição
resultados_dist = analise_distribuicao(precos)
print(f"Assimetria: {resultados_dist['assimetria']:.3f}")

# Teste de hipóteses
resultados_hip = teste_hipoteses_duas_amostras(precos_sp, precos_rj, "SP", "RJ")
interpretacao = interpretar_resultados(resultados_hip)
