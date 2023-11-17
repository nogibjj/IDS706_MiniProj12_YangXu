# IDS706_MiniProj12_YangXu: MLflow Project Management

[![Python CI](https://github.com/nogibjj/IDS706_MiniProj12_YangXu/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS706_MiniProj12_YangXu/actions/workflows/cicd.yml)

## Project Overview
This project showcases the creation of a simple machine learning model and the utilization of MLflow to manage the project, including tracking metrics.

## Getting Started

### Prerequisites
- Python 3.7 or later
- Pip package manager

### Installation
Follow these steps to install the required packages and run the MLflow tracking server:
```shell
pip install mlflow
mlflow server --host 127.0.0.1 --port 8080
```

### Model Functionality
A Logistic Regression model has been trained on the Iris dataset with evaluation metrics like accuracy, precision, recall, and F1-score calculated to assess performance.

### MLflow Tracking
MLflow is used to track experiments, log parameters, and register the model. To view metrics and model details, navigate to the MLflow UI at http://127.0.0.1:8080.

#### Main MLflow Tracking Page
Here's the MLflow Tracking main page showing the list of experiments:
![Main MLflow Tracking Page](Main_MLflow_Tracking_Page.png)

#### Detailed Run View Page
Clicking on a specific run provides detailed metrics, parameters, and model artifacts:
![Detailed Run View Page](Run_View_Page.png)

## Deliverables
### MLflow Project Directory
The project directory structure is as follows:
```bash
IDS706_MiniProj12_YangXu (Root Directory)
│
├── .devcontainer
│   ├── Dockerfile
│   └── devcontainer.json
│
├── .github
│   └── workflows
│       └── cicd.yml
│
├── main.py
│
├── test_main.py
│
├── requirements.txt
│
├── Makefile
│
├── README.md
│
└── .gitignore
```

Testing
To run tests, execute the test_main.py script using the following command:
```shell
python test_main.py
```
