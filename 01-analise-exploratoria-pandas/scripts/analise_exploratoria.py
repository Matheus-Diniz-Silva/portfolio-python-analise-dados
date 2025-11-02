"""
Script para análise exploratória do dataset Olist
Funções reutilizáveis para análise de dados
"""

import pandas as pd
import numpy as np

def carregar_dados_olist():
    """
    Carrega todos os datasets principais do Olist
    Retorna: tuple (customers, orders, order_items, products)
    """
    customers = pd.read_csv('../data/olist_customers_dataset.csv')
    orders = pd.read_csv('../data/olist_orders_dataset.csv')
    order_items = pd.read_csv('../data/olist_order_items_dataset.csv')
    products = pd.read_csv('../data/olist_products_dataset.csv')
    
    print("Dados carregados com sucesso!")
    print(f"Customers: {customers.shape}")
    print(f"Orders: {orders.shape}")
    print(f"Order Items: {order_items.shape}")
    print(f"Products: {products.shape}")
    
    return customers, orders, order_items, products

def analise_exploratoria_basica(df, nome_df):
    """
    Realiza análise exploratória básica de um DataFrame
    """
    print(f"\n=== ANÁLISE EXPLORATÓRIA - {nome_df.upper()} ===")
    print(f"Dimensões: {df.shape}")
    print(f"\nPrimeiras 5 linhas:")
    print(df.head())
    print(f"\nInformações do DataFrame:")
    print(df.info())
    print(f"\nValores missing:")
    print(df.isnull().sum())
    print(f"\nEstatísticas descritivas:")
    print(df.describe(include='all'))

def analise_clientes(customers):
    """
    Análise específica do dataset de clientes
    """
    print("\n=== ANÁLISE DE CLIENTES ===")
    print(f"Total de clientes: {len(customers)}")
    print(f"Clientes únicos: {customers['customer_unique_id'].nunique()}")
    print(f"Estados: {customers['customer_state'].nunique()}")
    print(f"Cidades: {customers['customer_city'].nunique()}")
    
    distribuicao_estado = customers['customer_state'].value_counts()
    print(f"\nDistribuição por estado (Top 5):")
    print(distribuicao_estado.head())
    
    return distribuicao_estado

def analise_pedidos(orders):
    """
    Análise específica do dataset de pedidos
    """
    print("\n=== ANÁLISE DE PEDIDOS ===")
    print(f"Total de pedidos: {len(orders)}")
    
    # Converter datas
    orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
    print(f"Período: {orders['order_purchase_timestamp'].min()} a {orders['order_purchase_timestamp'].max()}")
    
    status_pedidos = orders['order_status'].value_counts()
    print(f"\nStatus dos pedidos:")
    for status, count in status_pedidos.items():
        percentual = (count / len(orders)) * 100
        print(f"  {status}: {count} ({percentual:.1f}%)")
    
    return status_pedidos

if __name__ == "__main__":
    print("Script de análise exploratória - Projeto 01")
    
    # Exemplo de uso
    customers, orders, order_items, products = carregar_dados_olist()
    analise_exploratoria_basica(customers, "CUSTOMERS")
    analise_clientes(customers)
    analise_pedidos(orders)
