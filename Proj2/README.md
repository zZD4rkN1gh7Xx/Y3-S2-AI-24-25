# Predicting Students' Dropout / Academic Success

Supervised Learning -- Artificial Intelligence FEUP2025

## Overview

This project applies **supervised machine learning** techniques to
predict the **academic status** of university students.\
The target variable includes **three possible outcomes**:

-   **Dropout**\
-   **Enrolled**\
-   **Graduate**

The goal is to build accurate models capable of identifying students at
risk of dropping out and supporting academic decision-making.

------------------------------------------------------------------------

## Objectives

-   Preprocess and prepare an educational dataset with numerical and
    categorical variables\
-   Train and evaluate multiple classification algorithms\
-   Compare models using standard ML metrics\
-   Identify key factors influencing academic success\
-   Provide interpretability and relevant visualisations

------------------------------------------------------------------------

## Machine Learning Methods

The following supervised learning models were implemented:

### **Algorithms**

-    **Decision Tree**
-    **Random Forest** *(best performance \~75.7% accuracy)*
-    **k-Nearest Neighbors (k-NN)**

### **Additional Techniques**

-   **GridSearchCV** --- Hyperparameter optimization\
-   **MinMaxScaler** --- Feature normalization\
-   **PCA** --- Dimensionality reduction and exploratory analysis

------------------------------------------------------------------------

## Dataset & Problem Definition

-   **Problem Type:** Multiclass classification\
-   **Target Variable:** *Encoded as*
    -   Dropout → `0`\
    -   Enrolled → `1`\
    -   Graduate → `2`\
-   Includes diverse categorical and numerical features\
-   Missing data handled; categorical data encoded appropriately

------------------------------------------------------------------------

## Methodology

### **1. Preprocessing**

-   Handling missing values\
-   Encoding categorical variables\
-   Normalizing numerical attributes\
-   Feature--target separation

### **2. Train/Test Split**

-   `train_test_split` with **20%** for testing

### **3. Training & Evaluation**

Metrics used: - **Accuracy** - **Precision** - **Recall** -
**F1-Score** - **Classification Report** - **Confusion Matrix** -
**Learning curve analysis** (for overfitting evaluation)

### **4. PCA Analysis**

-   Used to simplify correlated features\
-   Helped visualize variance retention

------------------------------------------------------------------------

## Results Summary

-   **Random Forest achieved the best performance (\~75.7%)**
-   Decision Tree and KNN showed lower accuracy\
-   PCA effectively compressed feature space\
-   Feature importance analysis highlighted the most influential
    predictors

------------------------------------------------------------------------

## Related Work (Brief Summary)

-   Machine learning widely used to predict dropout and academic
    performance\
-   Models like Random Forest, SVM, and CatBoost frequently show strong
    results\
-   Incorporating learning management system logs improves prediction
    quality\
-   Model explainability is crucial for real-world adoption by
    universities

------------------------------------------------------------------------

## Technologies Used

### **Languages & Tools**

-   Python\
-   Jupyter Notebook

### **Libraries**

    pandas
    numpy
    scikit-learn
    matplotlib
    seaborn

------------------------------------------------------------------------

## Project Structure (Suggested)

    ├── data/
    │   └── students.csv
    ├── notebooks/
    │   └── SupervisedLearning.ipynb
    ├── reports/
    │   └── Artificial Intelligence-SupervisedLearningCP1-final.pdf
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## How to Run

### 1. Install dependencies

``` bash
pip install -r requirements.txt
```

### 2. Open the Jupyter Notebook

``` bash
jupyter notebook SupervisedLearning.ipynb
```

### 3. Execute the notebook cells to:

-   preprocess data\
-   train models\
-   evaluate performance\
-   generate plots

------------------------------------------------------------------------

## Future Improvements

-   Test more models (SVM, CatBoost, XGBoost)\
-   Address dataset imbalance\
-   Add cross-validation\
-   Deploy the model as a web service or dashboard\
-   Improve explainability (SHAP, LIME)

------------------------------------------------------------------------

## Authors

**Grupo A1_111**\
- João Cordeiro (202205682)\
- Luciano Ferreira (202208158)\
- Tomás Telmo (202206091)
