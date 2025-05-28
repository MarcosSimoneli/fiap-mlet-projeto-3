import pickle
from Services.S3_service import get_json_from_s3, put_json_to_s3
from Data.DataTreatment import tratar_dados
from datetime import datetime

def lambda_handler(event, context):
    now = datetime.now()
    object_key = f"bestseller/{now.year}/{now.month}/{now.day}/{now.hour}/file.json"
    
    data = get_json_from_s3('fiap-mlet-fase3', object_key)

    with open('modelo_bestseller.pkl', 'rb') as f:
        model = pickle.load(f)

    predicoes = tratar_dados(data, model)
    print("Resultado da predição:", predicoes)

    put_json_to_s3(predicoes)

    return {
        'statusCode': 200,
        'body': 'Modelo carregado e predição realizada com sucesso!'
    }