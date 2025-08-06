\# 📱 Smartphone Market Analytics – Egypt



This project explores smartphone sales data in Egypt, focusing on cleaning, transformation, and preparation for analytics workflows. The goal is to produce a high-quality, reproducible dataset ready for advanced analysis and dashboarding.



---



\##  Tools Used



\- \*\*Python\*\*

\- \*\*pandas\*\* for data cleaning and transformation

\- \*\*CSV\*\* as the final export format



---



\## Dataset Overview



The raw dataset contains product-level information scraped from e-commerce platforms, including:



\- Product identifiers and titles

\- Pricing details (original and discounted)

\- Ratings and review counts

\- Offer counts and seller flags

\- Brand and product type

\- Sales volume (textual)



---



\## 🧹 Data Cleaning Steps



The cleaning pipeline includes:



\### 1. \*\*Column Pruning\*\*

\- Removed irrelevant or redundant columns not useful for analysis.



\### 2. \*\*Duplicate Handling\*\*

\- Dropped exact duplicate rows to ensure uniqueness.



\### 3. \*\*Type Conversion\*\*

\- Converted `product\_price` and other numeric fields to proper `float` types.

\- Ensured all numeric columns are free of non-numeric characters.



\### 4. \*\*Missing Value Imputation\*\*

\- Imputed missing numeric values using \*\*median\*\* strategy for robustness.



\### 5. \*\*Sales Volume Normalization\*\*

\- Created a new column `sales\_volume\_clean` to standardize textual sales volume into a consistent format.



---



Author

Ahmed — Data Analyst

Focused on building reproducible analytics workflows.







