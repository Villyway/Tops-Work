/* ============================================================
   Title: Retail Profitability & Market Segment Analysis
   Problem Statement: Identify underperforming product categories 
   and regions by analyzing the relationship between discount 
   rates and net profit margins.
   Dataset: Sample Superstore Dataset (SampleSuperstore.csv)
   Source: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final
   ============================================================ */


/* ------------------------------------------------------------
   1. DATABASE & SCHEMA CREATION
   ------------------------------------------------------------ */

CREATE DATABASE RetailAnalysis;
USE RetailAnalysis;

CREATE TABLE Orders (
    RowID           INT PRIMARY KEY,
    OrderID         VARCHAR(20)     NOT NULL,
    OrderDate       DATE            NOT NULL,
    ShipDate        DATE,
    ShipMode        VARCHAR(50),
    CustomerID      VARCHAR(20),
    CustomerName    VARCHAR(100),
    Segment         VARCHAR(50),
    Country         VARCHAR(50),
    City            VARCHAR(50),
    State           VARCHAR(50),
    PostalCode      VARCHAR(10),
    Region          VARCHAR(20),
    ProductID       VARCHAR(20),
    Category        VARCHAR(50),
    SubCategory     VARCHAR(50),
    ProductName     VARCHAR(200),
    Sales           DECIMAL(10,2),
    Quantity        INT,
    Discount        DECIMAL(4,2),
    Profit          DECIMAL(10,2)
);

-- Load data (bulk import method depends on the SQL engine used)
-- Example (MySQL):
-- LOAD DATA INFILE 'SampleSuperstore.csv'
-- INTO TABLE Orders
-- FIELDS TERMINATED BY ','
-- ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
-- IGNORE 1 ROWS;


/* ------------------------------------------------------------
   2. MULTI-CONDITION FILTERING QUERIES
   ------------------------------------------------------------ */

-- 2.1 Orders with high discount but negative profit (loss-making due to discounting)
SELECT OrderID, Category, SubCategory, Region, Discount, Profit
FROM Orders
WHERE Discount > 0.3
  AND Profit < 0;

-- 2.2 High sales but low/negative profit margin transactions
SELECT OrderID, Category, Region, Sales, Profit
FROM Orders
WHERE Sales > 1000
  AND Profit < 50;

-- 2.3 Orders from a specific region with above-average discount
SELECT OrderID, Region, Category, Discount, Profit
FROM Orders
WHERE Region = 'West'
  AND Discount > 0.2
  AND Profit < 0;


/* ------------------------------------------------------------
   3. AGGREGATED PERFORMANCE REPORT BY REGION
   ------------------------------------------------------------ */

SELECT 
    Region,
    Category,
    ROUND(SUM(Sales), 2)           AS Total_Sales,
    ROUND(SUM(Profit), 2)          AS Total_Profit,
    ROUND(AVG(Discount), 2)        AS Avg_Discount,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin_Percent
FROM Orders
GROUP BY Region, Category
ORDER BY Region, Profit_Margin_Percent ASC;


/* ------------------------------------------------------------
   4. SUMMARY OF LOSS-MAKING TRANSACTIONS
   ------------------------------------------------------------ */

-- 4.1 Overall count and total loss amount by Region and Category
SELECT 
    Region,
    Category,
    COUNT(*)                    AS Loss_Making_Orders,
    ROUND(SUM(Profit), 2)       AS Total_Loss,
    ROUND(AVG(Discount), 2)     AS Avg_Discount_On_Loss_Orders
FROM Orders
WHERE Profit < 0
GROUP BY Region, Category
ORDER BY Total_Loss ASC;

-- 4.2 Top 10 biggest loss-making individual orders
SELECT TOP 10 
    OrderID, Region, Category, SubCategory, Discount, Sales, Profit
FROM Orders
WHERE Profit < 0
ORDER BY Profit ASC;
-- (For MySQL/PostgreSQL, replace "TOP 10" with "LIMIT 10" at the end instead)


/* ------------------------------------------------------------
   OBSERVATIONS (to be included in report/summary write-up)
   ------------------------------------------------------------
   - Categories/Regions with high average discounts but negative 
     total profit indicate over-discounting is eroding margins.
   - Sub-categories like Tables/Bookcases (commonly seen in this 
     dataset) tend to show high losses despite decent sales volume.
   - Comparing Profit_Margin_Percent across regions highlights 
     which regions are underperforming relative to sales generated.
   ------------------------------------------------------------ */
