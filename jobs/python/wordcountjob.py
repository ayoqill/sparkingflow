from pyspark.sql import SparkSession

# basically a spark job that counts the occurrence of every word in a single sentence
spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()

text = "Hello world Hello Spark Hello Airflow"

words = spark.sparkContext.parallelize(text.split(" "))
word_counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

for word, count in word_counts.collect():
    print(f"{word}: {count}")

spark.stop()