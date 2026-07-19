# SQL for Data Analytics — Retail Sales Exploration

## 📌 Overview
This project is a SQL assessment based on the **Superstore Sales Dataset**, focused on retail sales exploration, profitability analysis, and identifying underperforming product categories/regions.

**Dataset Source:** [Superstore Dataset (Kaggle)](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)

---

## 📂 Files in this Project

| File | Description |
|---|---|
| `SQL_Assessment_Section A and B.pdf` | Section A (concept questions) & Section B (practical queries) — formatted report |

| `retail_profitability_analysis.sql` | Section C mini-project SQL script (schema, filters, aggregation, loss report) |

---

## 📝 Assessment Structure

### Section A: Concept Application
Covers core SQL concepts including:
- `SELECT *` vs specific column selection
- Column aliasing with `AS`
- Data type conflicts in `WHERE` clauses
- Sorting with `ORDER BY` (ASC vs DESC)
- `LIMIT` vs `TOP` across SQL engines
- Logical query execution order

### Section B: Practical Task
Hands-on queries on the `orders` table:
1. Retrieve first 20 records
2. Select specific columns with an alias (`Sales AS Total_Sales`)
3. Filter high-value transactions (`Sales > 5000`)
4. Top 10 most profitable orders (`ORDER BY Profit DESC`)

### Section C: Mini Project — Retail Profitability & Market Segment Analysis
**Problem Statement:** Identify underperforming product categories and regions by analyzing the relationship between discount rates and net profit margins.

**Deliverables (in `retail_profitability_analysis.sql`):**
- Database & table schema creation
- Multi-condition filtering queries (discount vs profit, sales vs margin, region-specific)
- Aggregated performance report by Region & Category (total sales, profit, avg discount, profit margin %)
- Summary of loss-making transactions (grouped + top 10 biggest losses)

---

## 🛠️ How to Use
1. Import the `SampleSuperstore.csv` dataset into your SQL environment.
2. Run `retail_profitability_analysis.sql` to create the schema and execute the analysis queries.
3. Refer to `SQL_Assessment_Section A and B.pdf` for Section A & B answers.

> **Note:** Queries use SQL Server (`TOP`) syntax by default. MySQL/PostgreSQL equivalents (`LIMIT`) are included as comments where applicable.

---

## 🧰 Tools & Skills Used
- SQL
- Concepts: Filtering, Aggregation, Sorting, Aliasing, GROUP BY, Schema Design

---

## ✍️ Author
Prepared as part of a SQL for Data Analytics assessment — Retail Sales Exploration theme.
