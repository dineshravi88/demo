# Databricks notebook source
# MAGIC %md
# MAGIC # Creating an init script for 835 research group to install external libraries

# COMMAND ----------

# List of URLs for documentation

# COMMAND ----------

# https://github.com/voutcn/megahit
# https://github.com/tseemann/prokka
# https://github.com/weizhongli/cdhit
# https://github.com/bbuchfink/diamond

# COMMAND ----------

conda install -c conda-forge -c bioconda -c defaults prokka

# COMMAND ----------


init_file_content = """#!/bin/bash
set -ex
/databricks/python/bin/python -V
. /databricks/conda/etc/profile.d/conda.sh
conda activate /databricks/python
conda install -c bioconda megahit
conda install -c bioconda prokka
conda install -c bioconda cd-hit
conda install -c bioconda diamond
"""

# COMMAND ----------

# MAGIC %sh
# MAGIC conda install -c bioconda diamond

# COMMAND ----------

dbutils.fs.put("s3://tpc-aws-ted-dev-edpp-alyt-mitd835-us-east-1/cluster_init_v01.sh", init_file_content, True)

# COMMAND ----------

# Step 1: create the basch init script as text
# step 2: upload the script to a shared location
# step 3: configure the cluster to run the script on start up

# COMMAND ----------

dbutils.fs.ls("dbfs:/databricks/init/output/")

# COMMAND ----------

# MAGIC %sh
# MAGIC conda list

# COMMAND ----------

