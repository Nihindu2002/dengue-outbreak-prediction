# Dengue Outbreak Early Warning System — Sri Lanka

## Overview
This project is a machine learning-based Early Warning System designed to predict and visualize the risk of Dengue outbreaks across various districts in Sri Lanka. It utilizes historical case data and features to provide early warnings and help authorities take preemptive measures.

## Features
- **Interactive Dashboard**: A Streamlit web application providing a user-friendly interface.
- **Outbreak Prediction**: Uses a trained machine learning model (Random Forest) to predict the probability of a Dengue outbreak.
- **Risk Assessment Alerts**: Real-time alerts categorizing the risk into LOW, MEDIUM, or HIGH based on model probabilities.
- **Geospatial Visualization**: Interactive Choropleth maps built with Folium to visualize the total number of Dengue cases across different districts.
- **Historical Trends**: Line charts displaying historical Dengue cases over time for a selected district.

## Project Structure
- `app/`: Contains the main Streamlit application code (`app.py`).
- `data/`: Contains the datasets used for training and visualization (e.g., `dengue_features.csv`, `lka_districts.geojson`).
- `models/`: Stores the trained machine learning models (e.g., `rf_model.pkl`).
- `notebooks/`: Jupyter notebooks used for data exploration, model development, and mapping:
  - `01_eda.ipynb`: Exploratory Data Analysis.
  - `02_features.ipynb`: Feature Engineering and preprocessing.
  - `03_models.ipynb`: Model training and evaluation.
  - `04_maps.ipynb`: Geospatial mapping experiments.
- `requirements.txt`: List of Python dependencies required to run the project.

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd dengue-outbreak-prediction
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

To launch the Streamlit application, run the following command from the root directory of the project:

```bash
streamlit run app/app.py
```

## Technologies Used
- **Python**
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Scikit-Learn**: Machine learning (Random Forest model)
- **Folium & Streamlit-Folium**: Interactive geospatial mapping
- **Joblib**: Model serialization