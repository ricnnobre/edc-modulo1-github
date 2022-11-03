from pyspark.sql import SparkSession
from pyspark.sql.functions import col, min, max

# Cria objeto da Spark Session
spark = (SparkSession.builder.appName("DeltaExercise")
    .config("spark.jars.packages", "io.delta:delta-core_2.12:1.0.0")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .getOrCreate()
)

# Importa o modulo das tabelas delta
from delta.tables import *

# Leitura de dados
#enem = (
 #   spark.read.format("csv")
  #  .option("inferSchema", True)
   # .option("header", True)
   # .option("delimiter", ";")
   # .load("s3://datalake-igti-m1-terraform-producao-945696890928/raw-data/enem/2020")
#)
enem = (
    spark.read.format("parquet")
    .load("s3://datalake-ricardonn-945696890928/staging/enem")
)


# Escreve a tabela em staging em formato delta
print("Writing delta table...")
(
    enem
    .write
    .mode("overwrite")
    .format("delta")
    .partitionBy("year")
    .save("datalake-igti-m1-terraform-producao-945696890928/staging/enem/2020")
)