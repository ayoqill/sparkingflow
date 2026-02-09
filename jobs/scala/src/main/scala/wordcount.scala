import org.apache.spark.sql.SparkSession

object WordCount {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("Word Count")
      .getOrCreate()  // Remove .master() - it will be set by Airflow
    
    val sc = spark.sparkContext

    val textData = sc.parallelize(List("Hello World", "Hello Docker", "Hello Aqil", "Hello Scala"))

    val counts = textData
      .flatMap(line => line.split(" "))
      .map(word => (word, 1))
      .reduceByKey(_ + _)

    println("=== Word Count Results ===")
    counts.collect().foreach { case (word, count) =>
      println(s"$word: $count")
    }

    spark.stop()
  }
}