import pandas as pd

data = {
    'Nome': ['Joao', 'Maria', 'Pedro', 'Ana', 'Lucas'],
    'Idade': [20, 22, 19, 21, 23],
    'Cidade': ['Sao Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Fortaleza']
}

df = pd.DataFrame(data)

print(df[['Nome', 'Idade','Cidade']].head())