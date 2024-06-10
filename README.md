# Project Overview

## Description

This project aims to create a comprehensive data analysis system based on the Wide World Importers (WWI) database. The system integrates SQL, SAS, and Python to manage, analyze, and visualize customer transaction data. By leveraging the strengths of each technology, the project provides a robust solution for handling large datasets, performing complex statistical analyses, and generating insightful reports.

## Snippet List

### SQL

1. [CustomerTransactionSummaryByGeography.sql](CustomerTransactionSummaryByGeography.sql): The query aims to summarize customer transactions by geographical hierarchy, providing insights into the number of customers and total transaction amounts at the city, state/province, and country levels.
2. [SupplierTransactionSummaryByYear.sql](SupplierTransactionSummaryByYear.sql): The output of this query will be a list of suppliers with their total transaction amounts for each year.
3. [SalespersonMonthlyOrderSummary.sql](SalespersonMonthlyOrderSummary.sql): The output of this query will be a list of sales transactions, aggregated by salesperson, year, and month.
4. [SalespersonAnnualPerformanceWithBonus.sql](SalespersonAnnualPerformanceWithBonus.sql): The output of this query will be a list of sales transactions, aggregated by salesperson and year.
5. [TopMonthlyOrdersByYear.sql](TopMonthlyOrdersByYear.sql): Identifies the top monthly order by amount for each year, including salesperson details and tax amounts.
6. [MonthlyCustomerProfitVouchers.sql](MonthlyCustomerProfitVouchers.sql): Calculates monthly profit and tax per customer, assigning vouchers to the most profitable customers.
7. [MonthlyStockGroupAvgQuantity.sql](MonthlyStockGroupAvgQuantity.sql): Calculates the average monthly stock quantity on hand per customer and stock group, with results grouped by year, month, customer, and stock group.
8. [MonthlyStockGroupRollup.sql](MonthlyStockGroupRollup.sql): Calculates the average monthly stock quantity on hand per customer and stock group, with hierarchical grouping by year, month, customer, and stock group.
9. [MonthlySalespersonCumulativeInvoice.sql](MonthlySalespersonCumulativeInvoice.sql): Calculates monthly and cumulative invoice totals per salesperson, grouped by year and month.
10. [Top3AnnualSalesByEmployee.sql](Top3AnnualSalesByEmployee.sql): Identifies the top three sales employees by total sales for each year.

### SAS

11. [TopSalesByEmployeeSAS.sas](TopSalesByEmployeeSAS.sas): Imports WWI data, calculates monthly total unit price and quantity per salesperson and stock item, and retrieves the top 15 sales records.
12. [AddRecordIDToResultSAS.sas](AddRecordIDToResultSAS.sas): Adds a RecordID to the query results using DS2, increments the ID for each record, and prints the final dataset.
13. [CountRecordsByFullNameSAS.sas](CountRecordsByFullNameSAS.sas): Counts the records for each FullName in the dataset, sorts by descending total count, and prints the results.
14. [CalculatePriceAndTaxSAS.sas](CalculatePriceAndTaxSAS.sas): Calculates the total price and tax for each record by multiplying unit price and quantity, and prints the results with relevant variables.

### Python

15. [LoadSASFilesToSQLite.py](LoadSASFilesToSQLite.py): Reads SAS files from the WWI directory, loads them into DataFrames, and saves them to a SQLite database.
16. [ExecuteSQLQueriesSQLite.py](ExecuteSQLQueriesSQLite.py): Defines a function to execute SQL queries on a SQLite database and return the results as pandas DataFrames, then executes and retrieves data for customer profits, employee order quantities, and invoice totals.
17. [DescribeQueryResults.py](DescribeQueryResults.py): Displays summary statistics for each result set.
18. [MonthlyAnalysisAndMerge.py](MonthlyAnalysisAndMerge.py): Performs monthly profit, quantity, and sales analyses by aggregating and merging data based on the date, fills missing values, and displays the merged DataFrame with the date as the index.
