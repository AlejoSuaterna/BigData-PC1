import json

import boto3
import urllib.request
from datetime import datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # Obtener la fecha actual en el formato 'yyy-mm-dd'
    today = datetime.utcnow().strftime('%Y-%m-%d')
    
    
    # Obtener el contenido de la página
    req = urllib.request.Request('https://www.eltiempo.com/')
    with urllib.request.urlopen(req) as response:
        page_content = response.read()
    
    # Nombre del archivo en S3
    s3_filename = f'{today}.html'
    
    # Subir el contenido a S3
    s3.put_object(Bucket='alejo1', Key=s3_filename, Body=page_content)
    print("Página descargada y guardada como en S3 como: ", s3_filename)
    
    return {
        'statusCode': 200,
        'body': f'Página descargada y guardada como {s3_filename} en S3.'
    }