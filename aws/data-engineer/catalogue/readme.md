# AWS Certified Data Engineer Associate - Complete Service List

## **Core Data Engineering Services (Must Know)**

### **1. Storage Services**
```bash
🔥 Amazon S3 (Simple Storage Service)
   - Data lake foundation
   - Storage classes and lifecycle policies
   - Event notifications
   - Cross-region replication
   - S3 Transfer Acceleration

🔥 Amazon EFS (Elastic File System)
   - Shared file storage for EMR clusters
   - NFS protocol support

🔥 Amazon FSx
   - High-performance file systems
   - Lustre for HPC workloads
```

### **2. Databases & Data Stores**
```bash
🔥 Amazon RDS (Relational Database Service)
   - Source systems for ETL
   - Read replicas for analytics
   - Cross-region automated backups

🔥 Amazon Redshift
   - Data warehouse service
   - Redshift Spectrum (query S3 directly)
   - Concurrency scaling
   - Workload management

🔥 Amazon DynamoDB
   - NoSQL database
   - DynamoDB Streams
   - Global tables

🔥 Amazon DocumentDB
   - MongoDB-compatible document database

🔥 Amazon Neptune
   - Graph database service

🔥 Amazon Keyspaces (Apache Cassandra)
   - Managed Cassandra service
   - CQL compatibility

🔥 Amazon MemoryDB for Redis
   - In-memory database
   - Redis-compatible

🔥 Amazon ElastiCache
   - Managed caching service
   - Redis and Memcached
```

## **ETL & Data Processing (Critical)**

### **3. AWS Glue Ecosystem**
```bash
🔥🔥 AWS Glue
   - ETL jobs (Python/Scala)
   - Visual ETL (Glue Studio)
   - Job bookmarks
   - Development endpoints

🔥🔥 AWS Glue Data Catalog
   - Metadata repository
   - Schema registry
   - Table definitions

🔥🔥 AWS Glue Crawlers
   - Automatic schema discovery
   - Incremental crawls
   - Custom classifiers

🔥🔥 AWS Glue DataBrew
   - Visual data preparation
   - 300+ built-in transformations
   - Recipe-based workflows

🔥🔥 AWS Glue Data Quality
   - Data validation rules
   - Quality scoring
   - Anomaly detection
```

### **4. Big Data Processing**
```bash
🔥🔥 Amazon EMR (Elastic MapReduce)
   - EMR on EC2
   - EMR Serverless
   - EMR on EKS
   - EMR Studio
   - Supported frameworks: Spark, Hadoop, Hive, Presto, Flink

🔥 AWS Batch
   - Managed batch computing
   - Job queues and definitions
   - Container-based processing
```

### **5. Streaming Data**
```bash
🔥🔥 Amazon Kinesis Data Streams
   - Real-time data streaming
   - Shards and scaling
   - Producer/consumer libraries

🔥🔥 Amazon Kinesis Data Firehose
   - Data delivery service
   - Built-in transformations
   - Direct integration with analytics services

🔥🔥 Amazon Kinesis Data Analytics
   - Stream processing with SQL
   - Apache Flink support
   - Real-time analytics

🔥 Amazon MSK (Managed Streaming for Apache Kafka)
   - Managed Apache Kafka
   - Kafka Connect
   - Schema Registry
```

## **Analytics & Querying (Important)**

### **6. Query Services**
```bash
🔥🔥 Amazon Athena
   - Serverless SQL queries on S3
   - Federated queries
   - Workgroups and cost controls
   - ACID transactions

🔥 Amazon OpenSearch Service
   - Search and analytics engine
   - Log analytics and monitoring
   - Kibana dashboards

🔥 Amazon QuickSight
   - Business intelligence service
   - SPICE in-memory engine
   - Dashboards and visualizations
```

### **7. Data Lake & Analytics**
```bash
🔥 AWS Lake Formation
   - Data lake setup and security
   - Fine-grained access control
   - Data discovery and cataloging

🔥 Amazon DataZone
   - Data governance and collaboration
   - Data marketplace
   - Business glossary
```

## **Data Migration & Integration**

### **8. Migration Services**
```bash
🔥🔥 AWS Database Migration Service (DMS)
   - Database migration and replication
   - Continuous data replication
   - Change data capture (CDC)

🔥 AWS Schema Conversion Tool (SCT)
   - Database schema conversion
   - Assessment reports

🔥 AWS DataSync
   - Data transfer between on-premises and AWS
   - One-time or recurring transfers

🔥 AWS Snow Family
   - AWS Snowball Edge
   - AWS Snowmobile
   - Offline data transfer

🔥 AWS Transfer Family
   - SFTP/FTPS/FTP endpoints
   - Direct S3 integration

🔥 AWS AppFlow
   - SaaS application integration
   - No-code data flows
```

## **Workflow & Orchestration**

### **9. Orchestration Services**
```bash
🔥🔥 AWS Step Functions
   - Serverless workflow orchestration
   - State machines
   - Error handling and retries

🔥 Amazon Managed Workflows for Apache Airflow (MWAA)
   - Managed Apache Airflow
   - Python-based DAGs
   - Workflow scheduling

🔥 AWS Data Pipeline
   - Data workflow service
   - Preconfigured pipeline templates
   - On-premises integration

🔥 Amazon EventBridge
   - Event-driven architecture
   - Event routing and filtering
   - Custom event buses
```

## **Compute Services**

### **10. Serverless Compute**
```bash
🔥🔥 AWS Lambda
   - Serverless functions
   - Event-driven processing
   - Integration with data services

🔥 AWS Fargate
   - Serverless containers
   - ECS and EKS support
```

### **11. Container Services**
```bash
🔥 Amazon ECS (Elastic Container Service)
   - Container orchestration
   - Batch processing jobs

🔥 Amazon EKS (Elastic Kubernetes Service)
   - Managed Kubernetes
   - EMR on EKS support
```

## **Security & Governance**

### **12. Identity & Access Management**
```bash
🔥🔥 AWS IAM (Identity and Access Management)
   - Roles and policies
   - Cross-account access
   - Service-linked roles

🔥 AWS IAM Identity Center (SSO)
   - Single sign-on
   - Multi-account access

🔥🔥 AWS KMS (Key Management Service)
   - Encryption key management
   - Data encryption at rest/transit
```

### **13. Security Services**
```bash
🔥 Amazon VPC (Virtual Private Cloud)
   - Network isolation
   - VPC endpoints for S3/DynamoDB
   - Security groups and NACLs

🔥 AWS Secrets Manager
   - Database credentials management
   - Automatic rotation

🔥 AWS CloudTrail
   - API logging and auditing
   - Data governance compliance

🔥 AWS Config
   - Resource configuration tracking
   - Compliance monitoring
```

## **Monitoring & Operations**

### **14. Monitoring Services**
```bash
🔥🔥 Amazon CloudWatch
   - Metrics and alarms
   - Log aggregation
   - Custom metrics
   - CloudWatch Insights

🔥 AWS X-Ray
   - Distributed tracing
   - Application performance monitoring

🔥 AWS CloudFormation
   - Infrastructure as Code
   - Stack management
   - Drift detection

🔥 AWS CDK (Cloud Development Kit)
   - Programmatic infrastructure definition
   - Multiple language support
```

## **Machine Learning Integration**

### **15. ML Services (Basic Knowledge)**
```bash
🔥 Amazon SageMaker
   - ML model training and deployment
   - SageMaker Data Wrangler
   - Feature Store

🔥 Amazon Comprehend
   - Natural language processing
   - Text analytics

🔥 Amazon Textract
   - Document text extraction
   - Form and table extraction
```

## **Messaging & Notifications**

### **16. Messaging Services**
```bash
🔥 Amazon SQS (Simple Queue Service)
   - Message queuing
   - Dead letter queues
   - FIFO queues

🔥 Amazon SNS (Simple Notification Service)
   - Pub/sub messaging
   - Multi-protocol delivery
   - Fan-out patterns
```

## **Service Priority Levels**

### **🔥🔥 CRITICAL (Deep Knowledge Required):**
- AWS Glue (all components)
- Amazon EMR
- Amazon Kinesis (all services)
- Amazon Athena
- Amazon S3
- Amazon Redshift
- AWS Lambda
- Step Functions
- DMS
- IAM & KMS
- CloudWatch

### **🔥 IMPORTANT (Good Understanding):**
- All databases (RDS, DynamoDB, etc.)
- Lake Formation
- DataSync, Snow Family
- VPC, Security services
- CloudFormation
- MWAA
- QuickSight

### **📚 FOUNDATIONAL (Basic Knowledge):**
- ML services
- Container services
- Messaging services
- Monitoring tools

## **Exam Focus Areas**

### **1. Data Ingestion (25%)**
```bash
- Kinesis family services
- DMS and CDC
- Snow family for bulk transfer
- Real-time vs batch ingestion
- Data format considerations
```

### **2. Data Transformation (25%)**
```bash
- Glue ETL jobs and DataBrew
- EMR for complex processing
- Lambda for lightweight transforms
- Data quality and validation
- Performance optimization
```

### **3. Data Storage (20%)**
```bash
- S3 storage classes and lifecycle
- Data lake architectures
- Redshift design and optimization
- Database selection criteria
- Partitioning strategies
```

### **4. Data Orchestration (15%)**
```bash
- Step Functions workflows
- MWAA/Airflow DAGs
- Event-driven architectures
- Error handling and retries
- Workflow optimization
```

### **5. Data Security & Governance (15%)**
```bash
- IAM policies and roles
- Data encryption (KMS)
- VPC and networking
- Lake Formation permissions
- Compliance and auditing
```

## **Study Strategy**

### **Week 1-2: Core Services**
- S3, Glue, EMR, Kinesis, Athena

### **Week 3-4: Integration & Migration**
- DMS, DataSync, Lambda, Step Functions

### **Week 5-6: Security & Governance**
- IAM, KMS, VPC, Lake Formation, CloudTrail

### **Week 7-8: Practice & Scenarios**
- Hands-on labs
- Practice exams
- Architecture scenarios

## **Hands-on Labs to Practice**

```bash
1. Build a complete data pipeline: S3 → Glue → Redshift
2. Set up real-time streaming: Kinesis → Lambda → S3
3. Create a data lake with Lake Formation
4. Migrate database with DMS
5. Orchestrate workflows with Step Functions
6. Implement data quality checks with Glue Data Quality
7. Set up monitoring and alerting with CloudWatch
8. Configure security with IAM and KMS
```

Focus your study time on the 🔥🔥 CRITICAL services, as they form the core of most data engineering scenarios in the exam.
