# Projeto 01: Análise Exploratória do E-commerce Olist com Pandas

## Objetivo
Demonstrar habilidades fundamentais em manipulação e análise de dados usando Pandas através da análise exploratória do dataset Brazilian E-commerce by Olist, complementando as análises SQL realizadas anteriormente.

## Dataset
**Brazilian E-commerce by Olist**
- Mesmo dataset utilizado no Projeto 02 do portfólio SQL
- 8 tabelas relacionadas com dados de e-commerce real
- Período: 2016-2018
- +99k pedidos, +96k clientes únicos

## Habilidades Demonstradas
- Carregamento de múltiplos arquivos CSV
- Exploração inicial de DataFrames
- Detecção e tratamento de valores missing
- Análise estatística descritiva
- Agregações e operações groupby
- Merge e join de DataFrames
- Análise de qualidade dos dados

## Estrutura do Projeto
- `data/` - Arquivos CSV do dataset Olist
- `notebooks/` - Jupyter Notebooks com análise exploratória
- `scripts/` - Scripts Python para processos específicos
- `README.md` - Documentação do projeto

## Tecnologias
- Python 3.x
- Pandas
- NumPy
- Jupyter Notebook

## Análises Realizadas

### 1. Exploração Inicial dos Dados
- Carregamento de 4 datasets principais: Customers, Orders, Order Items, Products
- Análise de dimensões e estrutura dos DataFrames
- Verificação de tipos de dados e valores missing

### 2. Análise de Clientes (Customers)
- 99,441 registros de clientes
- 96,096 clientes únicos (3,345 repetidos)
- Distribuição geográfica: 27 estados, 4,119 cidades
- Concentração: SP (42%), RJ (13%), MG (12%)

### 3. Análise de Pedidos (Orders)
- 99,441 pedidos realizados
- Status: 96,478 entregues (97.1%), 1,107 enviados, 625 cancelados
- Período: Set/2016 a Out/2018
- Crescimento: de 4 para 4,026 pedidos/mês

### 4. Análise de Itens de Pedido (Order Items)
- 112,650 itens vendidos
- Preço médio: R$ 120.65
- Frete médio: R$ 19.99
- Média de 1.14 itens por pedido
- Produtos mais vendidos e mais lucrativos identificados

## Principais Descobertas

### Qualidade dos Dados
- Dados excepcionalmente limpos (poucos valores missing)
- Estrutura consistente entre tabelas
- Tipos de dados apropriados

### Insights de Negócio
- Alta taxa de sucesso em entregas (97.1%)
- Forte concentração no estado de São Paulo
- Crescimento orgânico ao longo do tempo
- Produtos com diferentes estratégias de preço e volume

### Performance Comercial
- Cliente médio faz 1.03 pedidos
- Ticket médio de R$ 120.65
- Operação predominantemente B2C (1 item por pedido)

## Arquivos Principais
- `notebooks/01_exploracao_inicial_olist.ipynb` - Análise exploratória completa
- `data/` - 8 datasets CSV do Olist

## Como Reproduzir a Análise
1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute o Jupyter Notebook: `jupyter notebook`
4. Abra `notebooks/01_exploracao_inicial_olist.ipynb`

## Próximas Etapas
- Análise detalhada de produtos e categorias
- Visualizações avançadas com Matplotlib/Seaborn
- Análise de sazonalidade temporal
- Integração entre múltiplas tabelas
- Análise de correlações e tendências

---
*Status: Concluído - Análise exploratória inicial realizada*

**Repositório SQL Complementar:** [portfolio-sql-analise-dados](https://github.com/Matheus-Diniz-Silva/portfolio-sql-analise-dados)
