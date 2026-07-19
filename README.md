<div align="center">

# Customer Segmentation using Machine Learning

### RFM Analysis + K-Means Clustering for Retail Customer Insights

</div>

---

## Project Overview

This project segments retail customers into meaningful groups based on purchasing behavior using **Machine Learning**.  
The workflow uses **RFM (Recency, Frequency, Monetary)** analysis, outlier handling, logarithmic transformation, feature scaling, and **K-Means clustering** to identify customer groups that can be targeted with different marketing strategies.

The final output includes:
- clean transactional data
- customer-level RFM dataset
- clustering results
- cluster interpretation
- business recommendations
- evaluation metrics
- visualizations and report-ready outputs

---

## Problem Statement

Retail businesses often collect large volumes of transaction data but struggle to turn it into actionable customer insights.  
Without segmentation, marketing campaigns become broad, inefficient, and less effective.

The goal of this project is to automatically group customers with similar buying patterns so that the business can:
- identify high-value customers
- find loyal customers
- detect inactive or lost customers
- improve retention and marketing performance

---

## Objectives

- Collect and clean retail transaction data
- Perform exploratory data analysis
- Engineer customer-level RFM features
- Detect and analyze outliers
- Apply logarithmic transformation to reduce skewness
- Standardize features for clustering
- Use K-Means to segment customers
- Evaluate the clustering quality
- Interpret each customer segment in business terms
- Provide marketing recommendations for each cluster

---

## Dataset

### Dataset Used
**Online Retail Dataset**

### Source
UCI Machine Learning Repository

### Dataset Size
- **541,909** transaction records
- **8** original columns

### Key Columns
- `InvoiceNo`
- `StockCode`
- `Description`
- `Quantity`
- `InvoiceDate`
- `UnitPrice`
- `CustomerID`
- `Country`

### Why this dataset?
This dataset is ideal for customer segmentation because it contains real transaction history, customer IDs, purchase values, and time-based behavior.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Joblib

---

## Skills Required

This project uses the following skills:

- Data cleaning
- Exploratory Data Analysis
- Feature engineering
- Outlier detection
- Log transformation
- Feature scaling
- Unsupervised learning
- K-Means clustering
- Cluster evaluation
- Business interpretation
- Data visualization
- Report writing
- Git and GitHub

---

## Project Workflow

1. Load raw retail data
2. Clean missing, duplicate, and invalid records
3. Perform EDA to understand customer behavior
4. Create RFM features:
   - Recency
   - Frequency
   - Monetary
5. Detect outliers using the IQR method
6. Apply `log1p` transformation to reduce skewness
7. Scale the features using `StandardScaler`
8. Use Elbow Method and Silhouette Score to choose K
9. Train K-Means clustering model
10. Analyze and name each customer segment
11. Generate business insights and recommendations
12. Save outputs, plots, and final reports

---

## Final Customer Segments

The final clustering produced four meaningful groups:

- **Champions / VIP Customers**
- **Loyal Regular Customers**
- **New / Promising Customers**
- **Lost Customers**

These segments help the business understand which customers should be retained, nurtured, reactivated, or rewarded.

---

## Model Evaluation

The final clustering model was evaluated using standard clustering metrics:

- **Silhouette Score:** `0.3375`
- **Calinski-Harabasz Index:** `3328.34`
- **Davies-Bouldin Index:** `1.0086`

These results indicate that the clustering produced meaningful and usable customer groups for business analysis.

---

## Key Business Insights

- A small group of customers contributes a large share of total revenue
- Many customers are inactive and can be targeted with reactivation campaigns
- Loyal customers can be upgraded into VIP segments
- New customers can be converted into repeat buyers with onboarding offers
- The business can improve revenue using segment-specific strategies

---

## Marketing Recommendations

### Champions / VIP Customers
- Exclusive offers
- Loyalty rewards
- Premium support
- Early access to products

### Loyal Regular Customers
- Membership benefits
- Upselling
- Bundle offers
- Personalized recommendations

### New / Promising Customers
- Welcome offers
- Follow-up emails
- Product suggestions
- Repeat-purchase incentives

### Lost Customers
- Win-back campaigns
- Discount coupons
- Re-engagement emails
- Reminder-based promotions

---

## Repository Structure

```text
customer-segmentation-ml/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│
├── reports/
│   └── figures/
│
├── models/
│
├── outputs/
│
├── README.md
├── requirements.txt
├── .gitignore
└── main.py

<div align="center">

# Customer Segmentation using Machine Learning

### RFM Analysis + K-Means Clustering for Retail Customer Insights

</div>

---

## Project Overview

This project segments retail customers into meaningful groups based on purchasing behavior using **Machine Learning**.  
The workflow uses **RFM (Recency, Frequency, Monetary)** analysis, outlier handling, logarithmic transformation, feature scaling, and **K-Means clustering** to identify customer groups that can be targeted with different marketing strategies.

The final output includes:
- clean transactional data
- customer-level RFM dataset
- clustering results
- cluster interpretation
- business recommendations
- evaluation metrics
- visualizations and report-ready outputs

---

## Problem Statement

Retail businesses often collect large volumes of transaction data but struggle to turn it into actionable customer insights.  
Without segmentation, marketing campaigns become broad, inefficient, and less effective.

The goal of this project is to automatically group customers with similar buying patterns so that the business can:
- identify high-value customers
- find loyal customers
- detect inactive or lost customers
- improve retention and marketing performance

---

## Objectives

- Collect and clean retail transaction data
- Perform exploratory data analysis
- Engineer customer-level RFM features
- Detect and analyze outliers
- Apply logarithmic transformation to reduce skewness
- Standardize features for clustering
- Use K-Means to segment customers
- Evaluate the clustering quality
- Interpret each customer segment in business terms
- Provide marketing recommendations for each cluster

---

## Dataset

### Dataset Used
**Online Retail Dataset**

### Source
UCI Machine Learning Repository

### Dataset Size
- **541,909** transaction records
- **8** original columns

### Key Columns
- `InvoiceNo`
- `StockCode`
- `Description`
- `Quantity`
- `InvoiceDate`
- `UnitPrice`
- `CustomerID`
- `Country`

### Why this dataset?
This dataset is ideal for customer segmentation because it contains real transaction history, customer IDs, purchase values, and time-based behavior.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Joblib

---

## Skills Required

This project uses the following skills:

- Data cleaning
- Exploratory Data Analysis
- Feature engineering
- Outlier detection
- Log transformation
- Feature scaling
- Unsupervised learning
- K-Means clustering
- Cluster evaluation
- Business interpretation
- Data visualization
- Report writing
- Git and GitHub

---

## Project Workflow

1. Load raw retail data
2. Clean missing, duplicate, and invalid records
3. Perform EDA to understand customer behavior
4. Create RFM features:
   - Recency
   - Frequency
   - Monetary
5. Detect outliers using the IQR method
6. Apply `log1p` transformation to reduce skewness
7. Scale the features using `StandardScaler`
8. Use Elbow Method and Silhouette Score to choose K
9. Train K-Means clustering model
10. Analyze and name each customer segment
11. Generate business insights and recommendations
12. Save outputs, plots, and final reports

---

## Final Customer Segments

The final clustering produced four meaningful groups:

- **Champions / VIP Customers**
- **Loyal Regular Customers**
- **New / Promising Customers**
- **Lost Customers**

These segments help the business understand which customers should be retained, nurtured, reactivated, or rewarded.

---

## Model Evaluation

The final clustering model was evaluated using standard clustering metrics:

- **Silhouette Score:** `0.3375`
- **Calinski-Harabasz Index:** `3328.34`
- **Davies-Bouldin Index:** `1.0086`

These results indicate that the clustering produced meaningful and usable customer groups for business analysis.

---

## Key Business Insights

- A small group of customers contributes a large share of total revenue
- Many customers are inactive and can be targeted with reactivation campaigns
- Loyal customers can be upgraded into VIP segments
- New customers can be converted into repeat buyers with onboarding offers
- The business can improve revenue using segment-specific strategies

---

## Marketing Recommendations

### Champions / VIP Customers
- Exclusive offers
- Loyalty rewards
- Premium support
- Early access to products

### Loyal Regular Customers
- Membership benefits
- Upselling
- Bundle offers
- Personalized recommendations

### New / Promising Customers
- Welcome offers
- Follow-up emails
- Product suggestions
- Repeat-purchase incentives

### Lost Customers
- Win-back campaigns
- Discount coupons
- Re-engagement emails
- Reminder-based promotions

---

## Repository Structure

```text
customer-segmentation-ml/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│
├── reports/
│   └── figures/
│
├── models/
│
├── outputs/
│
├── README.md
├── requirements.txt
├── .gitignore
└── main.py
