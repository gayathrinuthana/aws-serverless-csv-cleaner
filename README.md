# AWS Serverless CSV Cleaner & Visualizer

This project demonstrates a complete serverless data pipeline using AWS services to clean messy CSV data and visualize the output using Amazon QuickSight.

---

## 🚀 Project Overview

- 📥 **Input**: User uploads a CSV file to an S3 bucket
- ⚙️ **Processing**: AWS Lambda cleans the file (removes blanks, formats text)
- 📤 **Output**: Cleaned CSV is saved to another S3 bucket
- 📊 **Visualization**: Amazon QuickSight connects to the cleaned file and generates bar charts

---

## 🧰 Technologies Used

- **AWS Lambda** (Python)
- **Amazon S3**
- **Amazon IAM**
- **Amazon QuickSight**
- **Python csv module**

---

## 📁 File Structure

```bash
├── lambda_function.py          # Main Lambda logic
├── sample_input.csv            # Example raw CSV
├── architecture.png            # Architecture flowchart
├── screenshots/                # Optional visual output
│   └── bar_chart.png
└── README.md
