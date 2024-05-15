# Change-Data-Capture-CDC-Sales-Data-Processing

## Overview
This project aims to capture data changes in sales transactions, process and prepare it for ad-hoc analysis. The workflow involves generating mock sales data, storing it in DynamoDB, capturing data changes using DynamoDB Streams, transferring data to Kinesis Streams via EventBridge, transforming data with Lambda, storing it in an S3 bucket, cataloging metadata with Glue Crawler, and analyzing data with Athena.

## Architecture

![Alt Text](https://github.com/MrSachinGoyal/Change-Data-Capture-CDC-Sales-Data-Processing/blob/master/architecture.png)

## Prerequisites
- **Programming Language**: Python 3.1 or higher
- **Amazon Web Services (AWS) Account**:An active AWS account with the necessary permissions to create and manage services.
- **AWS Services**:
  - DynamoDB
  - EventBridge
  - Kinesis Streams
  - Lambda
  - Kinesis Firehose
  - S3
  - Glue
  - Athena
- **Note**: Ensure that appropriate IAM roles and permissions are assigned to access and manage the AWS services mentioned above.

## Workflow of the Project
**1. Mock Data Generation:**
  - Develop a Python script to generate real-time sales data. This script will simulate sales transactions and continuously feed data into the system.

**2. DynamoDB Table Setup:**
  - Create a DynamoDB table with a partition key to organize the data.
  - Enable DynamoDB Streams on this table to capture item-level modifications (inserts, updates, deletes) in a time-ordered sequence.

**3. Kinesis Stream Integration:**
  - Create an Amazon Kinesis Stream to handle real-time data changes from the DynamoDB Stream.
  - Use EventBridge Pipes to connect the DynamoDB Stream to the Kinesis Stream.
  - Configure the partition key using JSONPath to determine the appropriate shard in the Kinesis Stream for storing the data. Each shard handles a specific range of hash values.

**4. Data Transformation with Kinesis Firehose and Lambda Function:**
  - Set up Kinesis Data Firehose to consume data in batches from the Kinesis Stream.
  - Configure the Kinesis Firehose to send the batched data to an AWS Lambda function for transformation. Key configurations for the Lambda function include:
    - 1. Buffer Size: The amount of data Kinesis Firehose gathers before sending it to the Lambda function.
    - 2. Buffer Interval: The time Kinesis Firehose waits before sending the collected data to the Lambda function.
  - Transform the data in the Lambda function as required.
  - Send the transformed data back to Kinesis Firehose for final processing.

**5. Persistent Storage:**
  - Kinesis Firehose writes the transformed data to persistent storage, such as Amazon S3.

**6. Metadata and Schema Management with AWS Glue:**
  - Create an AWS Glue Crawler to scan the data stored in S3.
  - Use the crawler to generate a schema and metadata, which are stored in the AWS Glue Catalog, a centralized metadata repository.

**7. Data Analysis with AWS Athena:**
  - Leverage the metadata in the AWS Glue Catalog to perform ad-hoc analysis using AWS Athena.
  - Execute SQL queries directly on the data stored in S3, utilizing the schema and metadata information for efficient querying.

## Key Learnings
- **Change Data Capture (CDC) Implementation**: Understanding the process of capturing and processing change data in real-time from sales transactions.
- **AWS Service Integration**: Integrating various AWS services such as DynamoDB, Kinesis, Lambda, Glue, and Athena showcases the versatility and power of cloud-based data processing solutions.
- **End-to-End Data Pipeline Design**: Designing and implementing an end-to-end data pipeline from data generation to analysis provides a holistic understanding of data engineering principles and best practices.

