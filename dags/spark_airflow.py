import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

dag = DAG(
    dag_id='sparkingflow',
    default_args={
        'owner': 'Aqil Aiman',
        'start_date': airflow.utils.dates.days_ago(1)
    },
    schedule_interval='@daily'
)

start = PythonOperator(
    task_id='start_task',
    python_callable=lambda: print("Jobs started or Starting the Spark Airflow DAG"),
    dag=dag
)

python_job = SparkSubmitOperator(
    task_id='spark_job',
    application='jobs/python/wordcountjob.py',
    conn_id='spark_conn',
    conf={
        'spark.master': 'spark://sparkingflow-spark-master-1:7077',
        'spark.pyspark.python': 'python3.8',
        'spark.pyspark.driver.python': 'python3.8'
    },
    env_vars={
        'PYSPARK_PYTHON': 'python3.8',
        'PYSPARK_DRIVER_PYTHON': 'python3.8'
    },
    dag=dag
)


scala_job = SparkSubmitOperator(
    task_id='spark_scala_job',
    application='jobs/scala/target/scala-2.12/wordcount_2.12-0.1.jar',
    java_class='WordCount',
    name='scala-word-count',
    conn_id='spark_conn',
    conf={
        'spark.master': 'spark://sparkingflow-spark-master-1:7077'
    },
    dag=dag
)

end = PythonOperator(
    task_id='end_task',
    python_callable=lambda: print("Jobs completed successfully"),
    dag=dag
)

start >> python_job >> scala_job >> end