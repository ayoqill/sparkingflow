FROM apache/airflow:2.7.1-python3.8

USER root
RUN apt-get update && apt-get install -y openjdk-11-jdk && apt-get clean

USER airflow
RUN pip install --no-cache-dir \
    apache-airflow==2.7.1 \
    apache-airflow-providers-apache-spark==4.1.3 \
    pyspark==3.4.1  # Compatible with Python 3.8

ENV SPARK_HOME=/home/airflow/.local/lib/python3.8/site-packages/pyspark