# Projeto 02: Visualização de Dados do E-commerce Olist

## Objetivo
Demonstrar habilidades em visualização de dados usando Matplotlib e Seaborn para criar insights visuais e dashboards profissionais a partir do dataset Brazilian E-commerce.

## Dataset
Brazilian E-commerce by Olist (mesmo dataset do Projeto 01)

## Habilidades Demonstradas
- Visualizações com Matplotlib e Seaborn
- Gráficos para análise de negócio
- Visualizações geográficas
- Análise temporal com séries
- Criação de dashboards
- Storytelling com dados
- Organização de código em scripts reutilizáveis

## Tecnologias
- Python 3.x
- Matplotlib
- Seaborn
- Pandas

## Estrutura do Projeto

### `notebooks/`
- `02_visualizacoes_olist.ipynb` - Notebook principal com análise completa e 6 visualizações

### `scripts/`
- `gerar_visualizacoes.py` - Funções reutilizáveis para geração de gráficos

### `images/`
- Diretório para exportação de imagens dos gráficos gerados

## Visualizações Criadas

### 1. Distribuição Geográfica de Clientes
- Gráfico de barras mostrando concentração por estado
- SP concentra 42% dos clientes
- Top 5 estados representam 77.2% do total
- Técnica: Gráfico de barras com anotações

### 2. Evolução Temporal de Pedidos
- Série temporal mensal de pedidos
- Período: Set/2016 a Out/2018
- Mês de pico: Nov/2017 (7,544 pedidos)
- Técnica: Gráfico de linha temporal

### 3. Distribuição de Preços dos Produtos
- Histograma da distribuição de preços
- Preço médio: R$ 120.65
- Preço mediano: R$ 74.99
- Grande variação (R$ 0.85 a R$ 6,735.00)
- Técnica: Histograma com linhas de média e mediana

### 4. Status dos Pedidos
- Gráfico de pizza da distribuição
- 97% dos pedidos entregues com sucesso
- Baixíssimas taxas de cancelamento (0.6%)
- Técnica: Gráfico de pizza com cores diferenciadas

### 5. Relação Preço vs Frete
- Scatter plot da correlação
- Correlação moderada positiva: 0.414
- Produtos mais caros tendem a ter fretes mais altos
- Técnica: Scatter plot com cálculo de correlação

### 6. Top 10 Produtos Mais Vendidos
- Gráfico horizontal por quantidade
- Produto líder: 527 unidades vendidas
- Visualização clara dos produtos mais populares
- Técnica: Gráfico de barras horizontais

## Scripts Reutilizáveis

### `gerar_visualizacoes.py`
Contém funções modularizadas para:
- `configurar_estilo()` - Configurações padrão de visualização
- `distribuicao_geografica()` - Gera gráfico de distribuição por estado
- `evolucao_temporal()` - Gera série temporal de pedidos

## Arquivos Principais
- `notebooks/02_visualizacoes_olist.ipynb` - Análise completa com visualizações
- `scripts/gerar_visualizacoes.py` - Funções reutilizáveis para gráficos

## Insights Principais

### Desempenho Operacional
- Forte concentração geográfica em SP (42% dos clientes)
- Operação muito eficiente (97% de entregas bem-sucedidas)
- Baixo índice de cancelamentos (0.6%)

### Comportamento de Vendas
- Grande dispersão de preços com produtos premium (até R$ 6.735,00)
- Sazonalidade evidente com pico em Novembro (Black Friday)
- Correlação moderada entre preço e frete (0.414)

### Estratégia Comercial
- Produtos com diferentes estratégias de preço e volume
- Oportunidade de expansão para outros estados
- Base sólida para campanhas sazonais

## Como Reproduzir a Análise

### Opção 1: Notebook Interativo
1. Execute o Jupyter Notebook `02_visualizacoes_olist.ipynb`
2. Todas as visualizações são geradas automaticamente

### Opção 2: Scripts Modulares
1. Importe as funções do `gerar_visualizacoes.py`
2. Use as funções específicas conforme necessidade

```python
from scripts.gerar_visualizacoes import distribuicao_geografica, evolucao_temporal

# Carregar dados
customers = pd.read_csv('data/olist_customers_dataset.csv')
orders = pd.read_csv('data/olist_orders_dataset.csv')

# Gerar visualizações
distribuicao_geografica(customers)
evolucao_temporal(orders)
