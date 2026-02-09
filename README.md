# sparkingflow = Spark and Airflow 

Simple Architecture Explanation
Think of this like a data processing factory with different departments:

🏭 The Components:
1. Airflow Webserver (Port 8081)
What: The dashboard/control panel
Simple analogy: Like the factory's control room where you see all machines and schedules
You use it to: View, trigger, and monitor your data pipelines (DAGs)

2. Airflow Scheduler ⭐
What: The brain that decides WHEN to run tasks
Simple analogy: Like a factory manager with a schedule board
It does:
Checks every few seconds: "Is it time to run any tasks?"
Reads your DAGs (data pipelines)
Sends tasks to workers when it's time
Example: "Run this data processing job every day at 2 AM"

3. Postgres Database
What: Memory/storage for Airflow
Simple analogy: Filing cabinets storing all records
Stores: Task history, DAG runs, user accounts, logs

4. Spark Master (Port 9090)
What: The boss of data processing workers
Simple analogy: Construction site foreman assigning tasks to workers
It does: Coordinates big data processing jobs

5. Spark Worker
What: Does the actual heavy data processing
Simple analogy: Construction workers doing the actual work
It does: Processes large datasets in parallel
📊 How They Work Together:
Example workflow:

You create a DAG saying "Process sales data every morning at 9 AM"
Scheduler wakes up at 9 AM and says "Time to run!"
Scheduler tells Spark Master "Process this data"
Spark Master tells Spark Worker "Here's the data, process it"
Results are saved, Postgres records what happened
You check the Webserver to see if it worked

In short: Scheduler = automatic timer that runs your data jobs on schedule! ⏰



# Creating job with Python

Docker container
<img width="1567" height="887" alt="dockersparkingflowContainer" src="https://github.com/user-attachments/assets/68162a88-c624-4aaa-a0ee-8d791aad67af" />

Setup task/ spark job in airflow
<img width="1915" height="932" alt="setup job spark" src="https://github.com/user-attachments/assets/1b0a2edd-6704-450d-a68c-3e7c7c6e2045" />

Sparkmaster UI
<img width="1918" height="937" alt="sparkmaster" src="https://github.com/user-attachments/assets/51d0cbd3-60e9-4fa3-b4ba-2df3d1612679" />

Result in airflow log

<img width="518" height="76" alt="result in airflow log" src="https://github.com/user-attachments/assets/5cac922a-9755-4192-9778-5dcbf1b9c4e6" />

Notes !!!
In real-world industry practice, viewing results in Airflow logs is NOT the standard approach. Here are the common methods:

Industry Best Practices for Spark Output:
1. Write to Data Storage (Most Common) ⭐
   Store results in databases or data lakes
2. Cloud Storage (Production Standard) ⭐⭐⭐ (write parquet)
   AWS S3, Azure Blob storage, Google Cloud Storage
3. Data Warehouse (Analytics) ⭐⭐
   Snowflake, Redshift, BigQuery
4. Task Metadata/XComs (Small Results Only)
  For small outputs, use Airflow XComs

# Creating job with Scala
