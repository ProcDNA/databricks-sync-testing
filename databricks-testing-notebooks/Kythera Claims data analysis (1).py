# Databricks notebook source
# dbutils.fs.ls("dbfs:/mnt/Kythera")
dbutils.fs.ls("dbfs:/mnt/kythera/00_Raw/")

# COMMAND ----------

dbutils.fs.ls("dbfs:/mnt/kythera/00_Raw/01_Kythera_a1_Claimline_alopesia_attribute/_committed_590254753263965156")

# COMMAND ----------

df = spark.read.format("csv").load("dbfs:/mnt/kythera/00_Raw/01_Kythera_a1_Claimline_alopesia_attribute/_committed_590254753263965156.csv")

# COMMAND ----------


