"""
Script para análise estatística do dataset Olist
Funções reutilizáveis para testes estatísticos
"""

import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm

def analise_distribuicao(dados):
    """
    Analisa a distribuição de uma variável numérica
    Retorna: dicionário com estatísticas descritivas
    """
    resultados = {
        'n': len(dados),
        'media': dados.mean(),
        'mediana': dados.median(),
        'desvio_padrao': dados.std(),
        'assimetria': dados.skew(),
        'curtose': dados.kurtosis(),
        'coef_variacao': (dados.std() / dados.mean() * 100)
    }
    
    # Teste de normalidade (amostra de 5000 para performance)
    stat_sw, p_sw = stats.shapiro(dados.sample(min(5000, len(dados))))
    resultados['shapiro_wilk'] = {'estatistica': stat_sw, 'p_value': p_sw}
    
    # Intervalo de confiança 95%
    n = len(dados)
    mean = dados.mean()
    std_err = dados.std() / np.sqrt(n)
    h = std_err * stats.t.ppf(0.975, n - 1)
    resultados['intervalo_confianca'] = (mean - h, mean + h)
    
    return resultados

def teste_correlacoes(df, var1, var2):
    """
    Calcula diferentes tipos de correlação entre duas variáveis
    """
    x = df[var1]
    y = df[var2]
    
    correlacoes = {
        'pearson': stats.pearsonr(x, y),
        'spearman': stats.spearmanr(x, y),
        'kendall': stats.kendalltau(x, y)
    }
    
    return correlacoes

def teste_hipoteses_duas_amostras(amostra1, amostra2, nome_grupo1, nome_grupo2):
    """
    Realiza testes de hipóteses para duas amostras independentes
    """
    resultados = {}
    
    # Estatísticas descritivas
    resultados['descricao'] = {
        nome_grupo1: {'n': len(amostra1), 'media': amostra1.mean(), 'dp': amostra1.std()},
        nome_grupo2: {'n': len(amostra2), 'media': amostra2.mean(), 'dp': amostra2.std()}
    }
    
    # Teste t (Welch)
    t_stat, p_t = stats.ttest_ind(amostra1, amostra2, equal_var=False)
    resultados['teste_t'] = {'estatistica': t_stat, 'p_value': p_t}
    
    # Teste Mann-Whitney
    u_stat, p_mw = stats.mannwhitneyu(amostra1, amostra2, alternative='two-sided')
    resultados['mann_whitney'] = {'estatistica': u_stat, 'p_value': p_mw}
    
    # Tamanho do efeito (Cohen's d)
    def cohens_d(x, y):
        nx, ny = len(x), len(y)
        return (x.mean() - y.mean()) / np.sqrt(((nx-1)*x.std()**2 + (ny-1)*y.std()**2) / (nx + ny - 2))
    
    resultados['cohens_d'] = cohens_d(amostra1, amostra2)
    
    return resultados

def interpretar_resultados(resultados):
    """
    Interpreta automaticamente os resultados estatísticos
    """
    interpretacao = []
    
    # Interpretar teste t
    if resultados['teste_t']['p_value'] < 0.05:
        diff = resultados['descricao']['grupo1']['media'] - resultados['descricao']['grupo2']['media']
        if diff > 0:
            interpretacao.append("Grupo 1 tem média significativamente MAIOR que Grupo 2")
        else:
            interpretacao.append("Grupo 1 tem média significativamente MENOR que Grupo 2")
    else:
        interpretacao.append("Não há diferença significativa entre os grupos")
    
    # Interpretar tamanho do efeito
    d = abs(resultados['cohens_d'])
    if d < 0.2:
        interpretacao.append("Tamanho do efeito: Muito pequeno")
    elif d < 0.5:
        interpretacao.append("Tamanho do efeito: Pequeno")
    elif d < 0.8:
        interpretacao.append("Tamanho do efeito: Médio")
    else:
        interpretacao.append("Tamanho do efeito: Grande")
    
    return interpretacao

if __name__ == "__main__":
    print("Script de análise estatística - Projeto 03")
    print("Funções disponíveis:")
    print("- analise_distribuicao(dados)")
    print("- teste_correlacoes(df, var1, var2)")
    print("- teste_hipoteses_duas_amostras(amostra1, amostra2, nome1, nome2)")
    print("- interpretar_resultados(resultados)")
