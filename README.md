# 🧹 Task 1 – Data Cleaning & Preprocessing  
### *Elevate Data Analyst Internship Program*

<p align="center">
  <img src="https://img.shields.io/badge/Internship-Elevate%20Data%20Analyst-blueviolet?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Task-01%20Data%20Cleaning-success?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Language-Python%203.13-yellow?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Library-Pandas-orange?style=for-the-badge&logo=pandas"/>
</p>

---

## 🎯 Objective
This repository contains **Task 1** of the **Elevate Data Analyst Internship Program**, focused on **data cleaning and preprocessing** using Python and Pandas.

The goal is to clean and prepare a real-world dataset by handling missing values, removing duplicates, standardizing categorical data, fixing date formats, and ensuring consistent data types.

---

## 📊 Dataset
**Dataset:** [Customer Personality Analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)  
**Source:** Kaggle  
**Rows:** 2240  **Columns:** 29  

This dataset contains customer demographics, purchasing behavior, and campaign response information, used to understand marketing segmentation.

---

## 🧰 Tools & Libraries Used
- **Python 3.13**
- **Pandas**
- **NumPy**
- **VS Code / Jupyter Notebook**

---

## ⚙️ Steps Performed

| Step | Task | Description |
|------|------|--------------|
| 1 | Identify Missing Values | Used `.isnull()` and `.fillna()` to detect and handle missing data |
| 2 | Remove Duplicates | Used `.drop_duplicates()` to eliminate duplicate rows |
| 3 | Standardize Text | Cleaned and formatted categorical values (Gender, Education, Marital Status) |
| 4 | Convert Date Format | Transformed date columns to uniform `dd-mm-yyyy` format |
| 5 | Rename Columns | Renamed headers to lowercase with underscores (`snake_case`) |
| 6 | Fix Data Types | Ensured numeric columns are int/float and dates are datetime |
| 7 | Derive New Columns | Calculated `Age` from `Year_Birth` |
| 8 | Export | Saved cleaned dataset as `marketing_campaign_cleaned.csv` |

---

## 🧾 Deliverables
- ✅ Cleaned dataset → `marketing_campaign_cleaned.csv`  
- ✅ Final validated dataset → `marketing_campaign_cleaned_final.csv`  
- ✅ Python cleaning script → `quick_clean_customer_personality.py`  
- ✅ Task 1 report (summary of changes)

---

## 📂 Project Structure
| File / Folder                            | Description                                                    |
| ---------------------------------------- | -------------------------------------------------------------- |
| **marketing_campaign.csv**               | Original Kaggle dataset (raw data)                             |
| **quick_clean_customer_personality.py**  | Python script used for data cleaning and preprocessing         |
| **marketing_campaign_cleaned.csv**       | Intermediate cleaned dataset (after removing nulls/duplicates) |
| **marketing_campaign_cleaned_final.csv** | Final dataset after full cleaning and validation               |
| **README.md**                            | Documentation describing objectives, steps, and results        |
| **Before_Data_Preprocessing.png**        | Screenshot showing data before preprocessing                   |
| **After_Data_Preprocessing.png**         | Screenshot showing data after preprocessing                    |


---

## 📈 Results Summary
| Metric | Before | After |
|--------|---------|--------|
| Rows | 2240 | 2240 |
| Columns | 29 | 30 |
| Missing Income | 24 | 0 (filled with median 51,381.5) |
| Duplicate Rows | 0 | 0 |
| Invalid Dates | 2 | 0 |
| Invalid Ages | 3 | 0 (optional median fill) |

---

## 🧠 Key Learnings
- Practical experience in **data cleaning & wrangling** using Pandas  
- Understanding of **data type conversions, imputation, and standardization**  
- Use of **.isnull(), .drop_duplicates(), .fillna(), .to_datetime()** methods effectively  
- Preparation of datasets for **EDA & modeling**  

---

## 🚀 About the Internship
**Program:** Elevate Data Analyst Intern  
**Task:** 1 – Data Cleaning and Preprocessing  
**Domain:** Data Analytics / Data Wrangling  
**Language:** Python  
**Tools:** Pandas, VS Code  

---

## 👩‍💻 Author
**Haripriya SK**  
📧 haripriyask964@example.com  
💼 *Elevate Data Analyst Intern (Task 1)*  

---

<p align="center">
  <b>✨ Part of the Elevate Internship Journey ✨</b><br>
  Transforming raw data into insights — one dataset at a time.
</p>

