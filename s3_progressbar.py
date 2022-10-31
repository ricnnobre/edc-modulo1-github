
import os
import sys
import boto3
import threading
from boto3.s3.transfer import TransferConfig

def multi_part_upload_with_s3():
    # Multipart upload
    config = TransferConfig(multipart_threshold=1024 * 25, max_concurrency=10,
                            multipart_chunksize=1024 * 25, use_threads=True)
    file_path = "C:/Users/Familia/Documents/Cientista de Dados/XPEducação/Engenheiro de Dados/data/dados/microdados_enem_2020.csv"
    key_path = 'raw-data/enem/2020/microdados_enem_2020.csv'
    s3.meta.client.upload_file(file_path, 'datalake-ricardonn-945696890928', key_path,
                            ExtraArgs={'ACL': 'public-read', 'ContentType': 'text/pdf'},
                            Config=config,
                            Callback=ProgressPercentage(file_path)
                            )


class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify we'll assume this is hooked up
        # to a single filename.
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()

if __name__ == '__main__':
    s3 = boto3.resource('s3')
    multi_part_upload_with_s3()


#with ZipFile('C:/Users/Familia/Downloads/microdados_enem_2020.zip', 'r') as zipObject:
 #  listOfFileNames = zipObject.namelist()
  # for fileName in listOfFileNames:
   #    if fileName.endswith('.csv'):
    #       # Extract a single file from zip
     #      print('Arquivo ' + fileName + ' extraido!')
      #     zipObject.extract(fileName, 'data')
#print("Extração Finalizada!")
           
# Criar um cliente para interagit com o AWS S3
#s3 = boto3.resource('s3')

#s3_client = boto3.client('s3')
#for bucket in s3.buckets.all():
 #   print(bucket.name)
#    if bucket.name.find("ricardonn") != -1:
#        print("Datalake no S3:  "+ bucket.name)
#        s3_client.upload_file("data/dados/microdados_enem_2020.csv",
#                            bucket.name,
#                            "raw-data/enem/2020/microdados_enem_2020.csv")
    
    #s3_client.download_file (bucket.name,
     #                        "data/CRAS_Freq_2021_05.txt",
      #                       "CRAS_Freq_2021_05.txt")

#df = pd.read_csv("CRAS_Freq_2021_05.txt", sep='#')
#print(df)

#s3_client.upload_file("DadosCRAs.csv", 
 #                     "datalake-igti-m1", 
  #                    "data/DadosCRAs.csv")


