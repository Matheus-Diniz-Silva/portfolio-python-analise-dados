"""
Script para gerar visualizacoes do dataset Olist
Funcoes reutilizaveis para analise de dados
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def configurar_estilo():
    """Configura estilo padrao para visualizacoes"""
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    plt.rcParams['figure.figsize'] = (12, 6)

def distribuição_geografica(customers, salvar_imagem=False):
    """Gera grafico de distribuicao geografica de clientes"""
    estado_distribuicao = customers['customer_state'].value_counts()
    
    plt.figure(figsize=(14, 8))
    bars = estado_distribuicao.plot(kind='bar', color='lightcoral', edgecolor='black')
    
    plt.title('Distribuição de Clientes por Estado - E-commerce Olist', fontsize=16, fontweight='bold')
    plt.xlabel('Estado', fontsize=12)
    plt.ylabel('Número de Clientes', fontsize=12)
    plt.xticks(rotation=45)
    
    for i, v in enumerate(estado_distribuicao):
        plt.text(i, v + 500, str(v), ha='center', va='bottom', fontweight='bold')
    
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    
    if salvar_imagem:
        plt.savefig('../images/distribuicao_geografica.png', dpi=300, bbox_inches='tight')
    
    plt.show()
    
    return estado_distribuicao

def evolucao_temporal(orders, salvar_imagem=False):
    """Gera grafico de evolucao temporal de pedidos"""
    orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
    orders['mes_ano'] = orders['order_purchase_timestamp'].dt.to_period('M')
    pedidos_por_mes = orders.groupby('mes_ano').size()
    
    plt.figure(figsize=(14, 8))
    plt.plot(pedidos_por_mes.index.astype(str), pedidos_por_mes.values, 
             marker='o', linewidth=2, markersize=6, color='steelblue')
    
    plt.title('Evolução Mensal de Pedidos - E-commerce Olist', fontsize=16, fontweight='bold')
    plt.xlabel('Mês/Ano', fontsize=12)
    plt.ylabel('Número de Pedidos', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    for i, v in enumerate(pedidos_por_mes.values):
        plt.text(i, v + 100, str(v), ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    
    if salvar_imagem:
        plt.savefig('../images/evolucao_temporal.png', dpi=300, bbox_inches='tight')
    
    plt.show()
    
    return pedidos_por_mes

if __name__ == "__main__":
    print("Script de visualizacoes - Projeto 02")
