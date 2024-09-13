

# 🚀 AI-Powered Text Summarizer with Google Pegasus 📝

## Overview

This project provides an end-to-end pipeline for text summarization using the `google/pegasus` model, implemented with modular components like data ingestion, transformation, validation, model training, and evaluation.

## Project Structure

```
├── config/config.yaml   
├── src/
│   ├── textSummarizer/
│   │   ├── components/
│   │   │   ├── data_ingestion.py
│   │   │   ├── data_transformation.py
│   │   │   ├── data_validation.py
│   │   │   ├── model_evaluation.py
│   │   │   ├── model_trainer.py
│   │   ├── config/
│   │   │   ├── configuration.py
│   │   ├── constants/
│   │   ├── entity/
│   │   ├── logging/
│   │   ├── pipeline/
│   │   │   ├── prediction.py
│   │   │   ├── stage_01_data_ingestion.py
│   │   │   ├── stage_02_data_validation.py
│   │   │   ├── stage_03_data_transformation.py
│   │   │   ├── stage_04_model_training.py
│   │   │   ├── stage_05_model_evaluation.py
│   │   ├── utils/
            ├── common.py
│   ├── .gitignore
│   ├── app.py
│   ├── Dockerfile
│   ├── main.py
│   ├── params.yaml
│   ├── README.md
│   ├── requirements.txt
│   ├── setup.py
│   ├── template.py
│   ├── test.py
```

## Pipeline Stages

1. **Data Ingestion**
2. **Data Validation**
3. **Data Transformation**
4. **Model Training**
5. **Model Evaluation**
6. **Prediction**

## Setup Instructions

### Prerequisites

- Python 3.12+
- Pip
- GPU (optional)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Puzan789/Text_summarizer/tree/master/Text-summarizer
   cd textSummarizer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```



### Running the Pipeline

```
python main.py
```

### Serving the Model

To serve the model, use:

```bash
fastapi dev app.py
```

## Configuration

All configuration parameters are stored in `params.yaml`.

## Logging and Monitoring

Logs are available in the `logs/` directory.


