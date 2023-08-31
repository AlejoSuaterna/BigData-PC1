# import json

# import boto3
# import urllib.request
# from datetime import datetime

# def lambda_handler(event, context):
#     s3 = boto3.client('s3')
    
#     # Obtener la fecha actual en el formato 'yyy-mm-dd'
#     today = datetime.utcnow().strftime('%Y-%m-%d')
    
    
#     # Obtener el contenido de la página
#     req = urllib.request.Request('https://www.eltiempo.com/')
#     with urllib.request.urlopen(req) as response:
#         page_content = response.read()
    
#     # Nombre del archivo en S3
#     s3_filename = f'{today}.html'
    
#     # Subir el contenido a S3
#     s3.put_object(Bucket='alejo1', Key=s3_filename, Body=page_content)
#     print("Página descargada y guardada como en S3 como: ", s3_filename)
    
#     return {
#         'statusCode': 200,
#         'body': f'Página descargada y guardada como {s3_filename} en S3.'
#     }


import os
import boto3
import urllib.request
from datetime import datetime

def lambda_handler(event, context):
    s3_bucket_name = 'alejo2'
    s3_base_path = 'news/raw'

    newspapers = ['eltiempo', 'elespectador']  # Lista de periódicos

    for newspaper in newspapers:
        url = f'https://www.{newspaper}.com'
        response = urllib.request.get(url)

        if response.status_code == 200:
            content = response.content

            # Generar la ruta en S3
            now = datetime.now()
            s3_path = f'{s3_base_path}/{newspaper}/{now.strftime("%Y-%m-%d")}.html'

            # Subir el contenido a S3
            s3_client = boto3.client('s3')
            s3_client.put_object(Body=content, Bucket=s3_bucket_name, Key=s3_path)

            print(f'Página de {newspaper} descargada y almacenada en S3: {s3_path}')
        else:
            print(f'Error al descargar la página de {newspaper}: {response.status_code}')

    return {
        'statusCode': 200,
        'body': 'Páginas descargadas y almacenadas en S3'
    }
