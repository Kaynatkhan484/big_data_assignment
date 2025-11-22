This repository contains my Big Data Assignment, showcasing ingestion, processing, and API layer development using PySpark and FastAPI.

Project Structure
big_data_assignment/
│
├── api/                # FastAPI layer to fetch processed data
├── ingestion/          # PySpark ingestion scripts
├── architecture/       # Architecture explanation & scaling strategy
├── scaling/            # Performance optimization notes
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── venv/               # Python virtual environment

Features Implemented

✅ Environment Setup: Python virtual environment and required dependencies installed

✅ Ingestion Pipeline: PySpark script to generate/process data and save as Parquet files

✅ API Layer: FastAPI endpoints to query/filter data efficiently

✅ Architecture & Scaling: Documented architecture using Spark, HDFS, Parquet, and partitioning strategies

✅ Proof of Skills: Ready to run scripts showing data processing and API fetching

Optional Advanced Features (Not Implemented)

Credit-limit middleware

Complex filtering API

Parallel ingestion

Dockerfile

Notes

This assignment is connected to my Final Year Project:

Project: Sentiment Analysis of Twitter Data using Hadoop Framework

Utilized Hadoop HDFS for distributed storage

Built Spark-based ingestion pipeline to process large datasets efficiently

Designed Spark & HDFS architecture for performance and scalability

Implemented data processing, filtering, and saving to Parquet format

How to Run

Clone the repository:

git clone https://github.com/Kaynatkhan484/big_data_assignment.git
cd big_data_assignment


Create and activate Python virtual environment:

python -m venv venv
venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Run ingestion script:

cd ingestion
python ingestion_script.py


Run API server:

cd ../api
uvicorn main:app --reload


Access API: http://127.0.0.1:8000/docs
