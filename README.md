# Data Mining Assignment: Data Preprocessing and Regression Analysis

This project demonstrates comprehensive data preprocessing techniques and regression analysis on a healthcare dataset using Python and Jupyter Notebooks.

## 📋 Overview

This notebook covers the complete data science pipeline from data loading to model evaluation, including:

1. **Data Loading and Exploration** - Loading CSV dataset and initial data inspection
2. **Missing Value Handling** - Mean and median imputation techniques
3. **Data Normalization** - Min-Max normalization and Z-score standardization
4. **Outlier Detection** - IQR (Interquartile Range) method for outlier identification and removal
5. **Regression Models** - Implementation of Linear, Multi-linear, and Logistic Regression

## 🗂️ Project Structure

```
dataminingassignment/
├── data_preprocessing_regression.ipynb  # Main Jupyter notebook
├── healthcare_dataset.csv               # Dataset file
├── .gitignore                           # Git ignore file
├── LICENSE                              # License file
└── README.md                            # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Jupyter Notebook or JupyterLab
- Required Python packages (see below)

### Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/Virgile1k/dataminingassignment.git
   cd dataminingassignment
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn jupyter
   ```

   Or install all at once:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn jupyter
   ```

4. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```
   
   Or use JupyterLab:
   ```bash
   jupyter lab
   ```

5. **Open the notebook**:
   - Navigate to `data_preprocessing_regression.ipynb`
   - Make sure `healthcare_dataset.csv` is in the same directory

## 📦 Required Libraries

- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **matplotlib** - Data visualization
- **seaborn** - Statistical data visualization
- **scikit-learn** - Machine learning algorithms and preprocessing tools
- **jupyter** - Interactive notebook environment

## 📊 Dataset

The project uses a healthcare dataset (`healthcare_dataset.csv`) containing:
- **55,500 rows** and **15 columns**
- Patient information including age, gender, blood type, medical conditions
- Billing information and room numbers
- Various other healthcare-related features

## 🔍 Notebook Contents

### 1. Data Loading and Exploration
- Load CSV dataset
- Display dataset shape and basic information
- Check for missing values
- Display data types
- Generate basic statistics

### 2. Missing Value Handling
- **Mean Imputation**: Replace missing values with column mean
- **Median Imputation**: Replace missing values with column median (more robust to outliers)
- Comparison of both methods

### 3. Data Normalization and Standardization
- **Min-Max Normalization**: Scale data to range [0, 1]
- **Z-score Standardization**: Transform data to have mean=0 and std=1
- Visualization of normalized vs standardized data

### 4. Outlier Detection and Removal
- **IQR Method**: Identify outliers using Interquartile Range
- Calculate lower and upper bounds (Q1 - 1.5×IQR, Q3 + 1.5×IQR)
- Remove outliers from dataset
- Visualize data before and after outlier removal

### 5. Regression Models

#### 5.1 Simple Linear Regression
- Predict `Billing Amount` based on `Age`
- Model evaluation using MSE and R² score
- Visualization of regression line

#### 5.2 Multi-linear Regression
- Predict `Billing Amount` using multiple features (`Age`, `Room Number`)
- Model evaluation metrics
- Residual analysis

#### 5.3 Logistic Regression
- Binary classification task
- Predict high/low billing amounts
- Confusion matrix and classification report
- Accuracy evaluation

## 📈 Key Features

- **Comprehensive Data Preprocessing**: Multiple techniques for handling missing data and outliers
- **Multiple Scaling Methods**: Both normalization and standardization approaches
- **Three Regression Models**: Linear, Multi-linear, and Logistic regression
- **Visualizations**: Box plots, scatter plots, and regression visualizations
- **Model Evaluation**: MSE, R² score, accuracy, confusion matrix, and classification reports

## 🛠️ Usage

1. Ensure `healthcare_dataset.csv` is in the project directory
2. Open `data_preprocessing_regression.ipynb` in Jupyter
3. Run all cells sequentially or execute cells individually
4. Review the outputs, visualizations, and model results

## 📝 Notes

- The notebook uses median imputation for further processing (more robust to outliers)
- Outlier removal is performed using the IQR method
- All models are evaluated on a test set (80/20 train-test split)
- Random state is set to 42 for reproducibility

## 🤝 Contributing

This is an assignment project. For questions or suggestions, please open an issue.

## 👤 Authors

Data Mining Assignment GROUP ONE


-   NDAYAMBAJE Virgile 25011041
- Innocent Fiston Kabalisa  W/BCS/21/09/15534
- Name 3

---

**Note**: Make sure to have the `healthcare_dataset.csv` file in the same directory as the notebook before running the code.

