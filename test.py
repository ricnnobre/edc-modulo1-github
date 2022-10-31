import sys
from pyspark.context import SparkContext
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job


## @params: ['JOB_NAME']
args = getResolvedOptions(sys.argv,['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'),args)

#A partir daaqui exatamente o mesmo código executado no AWS EMR

#Lendo os dados do Enem 2020

enem = (
    spark.read
    .format("csv")
    .option("header", True)
    .option("InferSchema",True)
    .option("delimiter", ';')
    .load('s3://datalake-ricardonn-945696890928/raw-data/enem/2020')
)


#Criando o arquivo parquet
#(
#    enem
#    .write
#    .mode("overwrite")
#    .format("parquet")
#    .partitionBy("NU_ANO")
#    .save("s3://datalake-ricardonn-945696890928/staging/enem-glue")    
#)