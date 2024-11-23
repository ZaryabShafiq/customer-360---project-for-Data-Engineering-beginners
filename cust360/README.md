Customer 360-Degree View Project

Project Overview

The Customer 360-Degree View Project is designed to create a unified view of customer data by integrating and analyzing data from multiple sources: CRM, customer service, and sales. The project demonstrates ETL processes, data warehousing, and business intelligence reporting to provide valuable insights into customer profiles and behavior.
Core Tools & Technologies:
•	Data Warehouse: PostgreSQL
•	ETL Orchestration: Apache Airflow
•	Data Transformation: Custom ETL scripts
•	Business Intelligence: Tableau Public
•	Programming Language: Python

Project Architecture

This project is structured to showcase skills in data integration, data warehousing, ETL orchestration, data transformation, and BI reporting.
1.	Data Ingestion: Import datasets from CRM, customer service, and sales CSV files into PostgreSQL.
2.	Data Transformation: Perform data cleaning, transformations, and joins in SQL for structured analytics.
3.	ETL Orchestration: Schedule and automate ETL jobs using Apache Airflow.
4.	Analytics and Reporting: Visualize processed data in Tableau for a comprehensive customer overview.

Datasets

The project uses three primary datasets:
1.	CRM Dataset: Contains customer profiles including customer_id, first_name, email, and join_date.
2.	Customer Service Dataset: Logs interactions with customers, including interaction_id, customer_id, issue_type, and resolution_status.
3.	Sales Dataset: Records transactional data, including transaction_id, customer_id, product_id, and amount.

Project Structure

Customer_360_Project/
├── dags/
│   ├── etl_dag.py              # Main DAG script for Airflow ETL pipeline
├── sql/
│   ├── transformations.sql      # SQL scripts for data transformations
│   ├── joins.sql                # SQL scripts for joining tables
├── src/
│   ├── etl.py                   # Custom ETL functions for transformations
├── logs/
│   └── etl.log                  # Log files for ETL processes
├── data/
│   ├── crm.csv                  # CRM data source
│   ├── customer_service.csv     # Customer Service data source
│   ├── sales.csv                # Sales data source
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies

Getting Started

1.	Clone the repository:
git clone https://github.com/your_username/Customer_360_Project.git
cd Customer_360_Project
2.	Set up the environment: Install dependencies from requirements.txt:
		pip install -r requirements.txt
3.	Load Data into PostgreSQL:
o	Open a PostgreSQL client and load CSV files using SQL COPY commands or any preferred import method.
4.	Configure Airflow:
o	Start the Airflow web server and scheduler.
o	Upload etl_dag.py to the Airflow DAGs folder to run ETL jobs.
5.	Run ETL Pipeline:
o	Trigger the DAG in Airflow and monitor task execution for loading, transforming, and integrating data in PostgreSQL.
6.	Visualize in Tableau:
o	Connect Tableau to the PostgreSQL database and access the transformed tables for analytics and visualization.

Key Features

1. ETL Pipeline
•	The pipeline is orchestrated using Airflow, which performs data extraction, loading, and transformation in PostgreSQL.
2. Data Transformation
•	Data is transformed in SQL to clean and aggregate information, focusing on joins between CRM, Customer Service, and Sales tables.
3. Business Intelligence
•	Tableau Public is used to visualize and analyze customer data, providing actionable insights into customer behavior.

Sample Queries

Some example queries for transformations include:
1.	Customer Aggregation:
sql
Copy code
SELECT customer_id, COUNT(transaction_id) AS total_transactions, SUM(amount) AS total_spent
FROM sales
GROUP BY customer_id;
2.	CRM and Service Join:
sql
Copy code
SELECT crm.customer_id, crm.first_name, crm.join_date, cs.issue_type, cs.resolution_status
FROM crm
LEFT JOIN customer_service cs ON crm.customer_id = cs.customer_id;
3.	Customer Sales Summary:
sql
Copy code
SELECT crm.customer_id, crm.first_name, SUM(sales.amount) AS total_spent
FROM crm
INNER JOIN sales ON crm.customer_id = sales.customer_id
GROUP BY crm.customer_id;

Visualizations

In Tableau Public, this project provides visualizations for:
1.	Customer Transaction Summary: Showing each customer’s total transactions and spending.
2.	Customer Service Trends: Summarizing the most common issue types and resolution times.
3.	Sales Analytics: Analyzing customer purchase patterns and purchase amounts over time.

Future Enhancements
1.	Add Machine Learning: Use ML models for customer segmentation and predictive analytics.
2.	Enhance Data Sources: Incorporate additional data sources, such as web and mobile app activity.
3.	Automate Reporting: Integrate with tools like Slack or email for automated report distribution.


Conclusion
This project is a practical demonstration of data engineering skills, showcasing data integration, warehousing, ETL, and visualization for a real-world Customer 360 application.

