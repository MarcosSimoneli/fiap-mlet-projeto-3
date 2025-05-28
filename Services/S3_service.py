import boto3
import json
from datetime import datetime

def get_json_from_s3(bucket_name, object_key):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    content = response['Body'].read().decode('utf-8')
    data = json.loads(content)
    return data

def put_json_to_s3(data):
    now = datetime.now()
    object_name = f"output-model/{now.year}/{now.month}/{now.day}/{now.hour}/data.json"

    s3 = boto3.client('s3')
    json_data = json.dumps(data)
    s3.put_object(Bucket="fiap-mlet-fase3", Key=object_name, Body=json_data, ContentType='application/json')

# Exemplo de uso:
# bucket = 'meu-bucket'
# key = 'caminho/do/arquivo.json'
# dados = get_json_from_s3(bucket, key)