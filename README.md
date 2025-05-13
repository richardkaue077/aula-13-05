O objetivo desta atividade prática é explorar a manipulação de dados estruturados utilizando a biblioteca Pandas no Python. O Pandas é uma poderosa ferramenta para análise de dados, que permite a criação, manipulação e análise de estruturas de dados como Series e DataFrames. Neste exercício, foram trabalhadas atividades de criação de dados, manipulação e extração de informações de tabelas (DataFrames), além de obter estatísticas básicas sobre esses dados.


O foco da atividade foi entender os conceitos fundamentais de manipulação de dados estruturados, a partir da utilização das estruturas de dados Series e e DataFrame do Pandas. Através dessa atividade, foi possível compreender como realizar operações comuns como a criação de conjuntos de dados, a seleção de colunas, e a extração de informações relevantes para análise.


Criação de DataFrame:

Utilizar um dicionário de dados para criar um DataFrame.

data = {'Nome': ['Joao', 'Maria', 'Pedro', 'Ana', 'Lucas'], 'Idade': [20, 22, 19, 21, 23], 'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Fortaleza']}
df = pd.DataFrame(data)
Seleção de Colunas:

Selecionar colunas específicas.

df[['Nome', 'Idade']]
Exibição das Primeiras Linhas:

Mostrar as primeiras 5 linhas do DataFrame.

df[['Nome', 'Idade']].head()

Calcular a média da idade.

df['Idade'].mean()

A atividade permite entender a criação e manipulação de dados com Pandas, além de realizar operações simples de seleção e análise estatística.
