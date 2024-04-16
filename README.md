# Change-Data-Capture-CDC-Sales-Data-Processing

## Overview
This project aims to capture change data in sales transactions, process it, and analyze it for insights. The workflow involves generating mock sales data, storing it in DynamoDB, capturing data changes using DynamoDB Streams, transferring data to Kinesis Streams via EventBridge, transforming data with Lambda, storing it in an S3 bucket, cataloging metadata with Glue Crawler, and analyzing data with Athena.

## Architecture

![Alt Text](https://github.com/MrSachinGoyal/Change-Data-Capture-CDC-Sales-Data-Processing/blob/master/architecture.png)

## Prerequisites
- **Programming Language**: Python 3.1 or higher
- **Amazon Web Services (AWS) Account**:An active AWS account with the necessary permissions to create and manage services.
- **AWS Services**:
  - DynamoDB:
  - EventBridge:
  - Kinesis Streams:
  - Lambda:
  - Kinesis Firehose:
  - S3
  - Glue
  - Athena
- **Note**: Ensure that appropriate IAM roles and permissions are assigned to access and manage the AWS services mentioned above.

## Workflow of the Project
**Mock Data Generation**:
- The Mock Data Generator script generates random sales data.

**DynamoDB**
- Data records are inserted into the DynamoDB table.
- DynamoDB Stream captures data changes (insert, modify, remove).

**EventBridge Pipe and Kinesis Stream:**
- EventBridge transfers data from DynamoDB Stream to Kinesis Stream based on partition key.
- JSON path determines the partition key for the Kinesis Stream.
- Each data change is captured as a separate record.

**Kinesis Firehose and Lambda Transformation:**
- Kinesis Firehose batches data from the Kinesis Stream.
- Batches are sent to Lambda for transforming data into the desired format.
- Transformed data is returned to Kinesis Firehose.

**S3 Data Storage:**
- Kinesis Firehose sends transformed data to the destined S3 bucket.

**Glue Crawler:**
- Glue Crawler is run on the S3 bucket to retrieve metadata required for analysis.
- JSON classifier is defined while creating the crawler to interpret data schema.

**Data Analysis with Athena:**
- Athena is utilized for data analysis.

## Key Learnings
- **Change Data Capture (CDC) Implementation**: Understanding the process of capturing and processing change data in real-time from sales transactions.
- **AWS Service Integration**: Integrating various AWS services such as DynamoDB, Kinesis, Lambda, Glue, and Athena showcases the versatility and power of cloud-based data processing solutions.
- **End-to-End Data Pipeline Design**: Designing and implementing an end-to-end data pipeline from data generation to analysis provides a holistic understanding of data engineering principles and best practices.

