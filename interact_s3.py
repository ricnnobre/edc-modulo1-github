import boto3
import pandas as pd
from zipfile import ZipFile


with ZipFile('C:/Users/Familia/Downloads/microdados_enem_2020.zip', 'r') as zipObject:
   listOfFileNames = zipObject.namelist()
   for fileName in listOfFileNames:
       if fileName.endswith('.csv'):
           # Extract a single file from zip
           print('Arquivo ' + fileName + ' extraido!')
           zipObject.extract(fileName, 'data')
print("Extração Finalizada!")
           
# Criar um cliente para interagit com o AWS S3
s3 = boto3.resource('s3')

s3_client = boto3.client('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
    if bucket.name.find("ricardonn") != -1:
        print("Datalake no S3:  "+ bucket.name)
        s3_client.upload_file("data/dados/microdados_enem_2020.csv",
                            bucket.name,
                            "raw-data/enem/2020/microdados_enem_2020.csv")
    
    #s3_client.download_file (bucket.name,
     #                        "data/CRAS_Freq_2021_05.txt",
      #                       "CRAS_Freq_2021_05.txt")

#df = pd.read_csv("CRAS_Freq_2021_05.txt", sep='#')
#print(df)

#s3_client.upload_file("DadosCRAs.csv", 
 #                     "datalake-igti-m1", 
  #                    "data/DadosCRAs.csv")


