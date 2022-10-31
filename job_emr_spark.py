from pyspark.sql.functions import mean,max,min,col,count
from pyspark.sql import SparkSession

#Criando a sessão no Spark
spark = (
    SparkSession.builder.appName("SparkEnem")
    .getOrCreate()
)

#Leitura do dataframe do Spark 
enem = (
    spark.read
    .format("csv")
    .option("header", True)
    .option("InferSchema",True)
    .option("delimiter", ';')
    .load('s3://datalake-ricardonn-945696890928/raw-data/enem/2020/')
)

print(enem.columns)

#Criando o arquivo parquet
(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("NU_ANO")
    .save("s3://datalake-ricardonn-945696890928/staging/enem/")    
)