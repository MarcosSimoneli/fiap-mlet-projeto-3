import pandas as pd
import json

def tratar_dados(data, model):
    produtos = data['data']['best_sellers']

    # Cria o DataFrame
    df = pd.DataFrame(produtos)

    # Trata as colunas numéricas
    df['product_price'] = df['product_price'].replace('[$,]', '', regex=True).astype(float)
    df['product_star_rating'] = df['product_star_rating'].astype(float)
    df['product_num_ratings'] = df['product_num_ratings'].astype(int)

    # Seleciona as features usadas no modelo
    X = df[['product_price', 'product_star_rating']]

    # Faz a predição para todas as linhas
    predictions = model.predict(X)

    # Adiciona a predição ao DataFrame
    df['predicted_num_ratings'] = predictions

    # Converte para lista de dicionários
    produtos_com_pred = df.to_dict(orient='records')

    # Estruture o JSON com uma chave
    dados_estruturados = {"best_sellers": produtos_com_pred}

    # Retorna como JSON serializável
    return dados_estruturados