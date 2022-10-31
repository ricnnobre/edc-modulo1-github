import boto3
import os

print("Ok2")

def download_dir(client, resource, dist, local='/tmp', bucket='your_bucket'):
    print("Ok1")
    paginator = client.get_paginator('list_objects')
    print(paginator)
    for result in paginator.paginate(Bucket=bucket, Delimiter='/', Prefix=dist):
        if result.get('CommonPrefixes') is not None:
            for subdir in result.get('CommonPrefixes'):
                download_dir(client, resource, subdir.get('Prefix'), local, bucket)
        for file in result.get('Contents', []):
            dest_pathname = os.path.join(local, file.get('Key'))
            print(dest_pathname)
            if not os.path.exists(os.path.dirname(dest_pathname)):
                os.makedirs(os.path.dirname(dest_pathname))
            if not file.get('Key').endswith('/'):
                resource.meta.client.download_file(bucket, file.get('Key'), dest_pathname)
            else:
                print("File exists")


print("OK")
client = boto3.client('s3')
resource = boto3.resource('s3')
download_dir(client, resource, 'data/', '/Users/Familia/Documents/Cientista de Dados/XPEducação/Engenheiro de Dados/', bucket='datalake-igti-m1')