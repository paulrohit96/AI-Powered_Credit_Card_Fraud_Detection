# AI-Powered Credit Card Fraud Detection: Anomaly-Based Alerting & Case Management System

## Project Overview

### Problem Statement
Credit card fraud is on the rise, causing significant financial losses and eroding customer trust. Traditional fraud detection methods struggle to keep up with emerging fraud patterns, leading to undetected fraud and false alerts. 

This project aims to develop an **AI-powered Anomaly Detection System** that:
- Detects suspicious transactions in real-time
- Automates case creation for flagged transactions
- Expedites fraud investigations, improving accuracy, efficiency, and security

### Goal
To design and deploy an AI-enabled fraud detection system within **3 months** that:
- **Reduces fraudulent transactions by at least 30%**
- **Minimizes false positives**
- **Enhances fraud investigation efficiency**

## Objectives & Milestones

### **1. Design and Train the Fraud Detection Model**
- **Output:** AI-based anomaly detection model for credit card transactions
- **Metric:** 90% recall, ≤5% false positive rate
- **Approach:** Use **Isolation Forest, One-Class SVM, and Autoencoders** for anomaly detection

### **2. Automate Case Creation and Investigation Workflow**
- **Output:** Automatic logging of flagged transactions for investigation
- **Measure:** 100% of flagged transactions create investigation cases
- **Approach:** Develop a case management database & fraud analyst dashboard

### **3. Optimize Fraud Detection for Accuracy and Efficiency**
- **Output:** Fine-tuned model optimized for real-world fraud detection
- **Measure:** Reduce fraud losses by 30% compared to historical data
- **Approach:** Perform **pilot testing** and adjust based on real or simulated transaction data

## Success Criteria
- **Accuracy:** 90% fraud detection recall, ≤5% false positive rate
- **Automation:** 100% flagged transactions generate cases
- **Customer Impact:** Fraud losses reduced by 30%, enhancing customer security and trust

## Assumptions, Risks & Mitigation Strategies

### **Assumptions**
- Availability of high-quality **historical transaction data** for training
- Timely **feedback from fraud analysts** for validation and optimization

### **Risks & Mitigation**
| **Risk**                              | **Mitigation Strategy** |
|----------------------------------------|-------------------------|
| **Data Quality Issues** (incomplete, biased data) | Perform **thorough data preprocessing** & validation |
| **Model Accuracy Challenges** (high false positives) | **Rigorous evaluation & tuning** to optimize results |
| **Integration Challenges** with existing pipelines | Allocate time for **testing, documentation & collaboration** |
| **Real-Time Processing Delays** (large transaction volumes) | Optimize architecture with **efficient streaming tech** |
| **Limited Fraud Data for Training** | Use **synthetic data generation** to augment training |
| **Evolving Fraud Patterns** | Regularly **update & retrain** model |

## Tech Stack
- **Machine Learning:** Isolation Forest, One-Class SVM, Autoencoders
- **Data Visualisation:** Tableau


## Contributors
- **Paul Rohit Jangareddi** - [LinkedIn](https://www.linkedin.com/in/paul-rohit-jangareddi)

## License
This project is licensed under the MIT License.

---
*This project is designed to assist financial institutions in improving fraud detection, minimizing losses, and enhancing customer security through AI-driven anomaly detection and automated case management.*
