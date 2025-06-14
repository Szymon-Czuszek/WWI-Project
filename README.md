# 📊 Project Overview

## 📝 Description

This project aims to create a comprehensive data analysis system based on the Wide World Importers (WWI) database. The system integrates SQL, SAS, and Python to manage, analyze, and visualize customer transaction data. By leveraging the strengths of each technology, the project provides a robust solution for handling large datasets, performing complex statistical analyses, and generating insightful reports.

## 📂 Snippet List

### 💾 SQL

1. 📌 [CustomerTransactionSummaryByGeography.sql](SQL/CustomerTransactionSummaryByGeography.sql): The query aims to summarize customer transactions by geographical hierarchy, providing insights into the number of customers and total transaction amounts at the city, state/province, and country levels.
2. 📌 [SupplierTransactionSummaryByYear.sql](SQL/SupplierTransactionSummaryByYear.sql): The output of this query will be a list of suppliers with their total transaction amounts for each year.
3. 📌 [SalespersonMonthlyOrderSummary.sql](SQL/SalespersonMonthlyOrderSummary.sql): The output of this query will be a list of sales transactions, aggregated by salesperson, year, and month.
4. 📌 [SalespersonAnnualPerformanceWithBonus.sql](SQL/SalespersonAnnualPerformanceWithBonus.sql): The output of this query will be a list of sales transactions, aggregated by salesperson and year.
5. 📌 [TopMonthlyOrdersByYear.sql](SQL/TopMonthlyOrdersByYear.sql): Identifies the top monthly order by amount for each year, including salesperson details and tax amounts.
6. 📌 [MonthlyCustomerProfitVouchers.sql](SQL/MonthlyCustomerProfitVouchers.sql): Calculates monthly profit and tax per customer, assigning vouchers to the most profitable customers.
7. 📌 [MonthlyStockGroupAvgQuantity.sql](SQL/MonthlyStockGroupAvgQuantity.sql): Calculates the average monthly stock quantity on hand per customer and stock group, with results grouped by year, month, customer, and stock group.
8. 📌 [MonthlyStockGroupRollup.sql](SQL/MonthlyStockGroupRollup.sql): Calculates the average monthly stock quantity on hand per customer and stock group, with hierarchical grouping by year, month, customer, and stock group.
9. 📌 [MonthlySalespersonCumulativeInvoice.sql](SQL/MonthlySalespersonCumulativeInvoice.sql): Calculates monthly and cumulative invoice totals per salesperson, grouped by year and month.
10. 📌 [Top3AnnualSalesByEmployee.sql](SQL/Top3AnnualSalesByEmployee.sql): Identifies the top three sales employees by total sales for each year.

### SAS

11. 📌 [TopSalesByEmployeeSAS.sas](SAS/TopSalesByEmployeeSAS.sas): Imports WWI data, calculates monthly total unit price and quantity per salesperson and stock item, and retrieves the top 15 sales records.
12. 📌 [AddRecordIDToResultSAS.sas](SAS/AddRecordIDToResultSAS.sas): Adds a RecordID to the query results using DS2, increments the ID for each record, and prints the final dataset.
13. 📌 [CountRecordsByFullNameSAS.sas](SAS/CountRecordsByFullNameSAS.sas): Counts the records for each FullName in the dataset, sorts by descending total count, and prints the results.
14. 📌 [CalculatePriceAndTaxSAS.sas](SAS/CalculatePriceAndTaxSAS.sas): Calculates the total price and tax for each record by multiplying unit price and quantity, and prints the results with relevant variables.

### Python

15. 📌 [LoadSASFilesToSQLite.py](Python/LoadSASFilesToSQLite.py): Reads SAS files from the WWI directory, loads them into DataFrames, and saves them to a SQLite database.
16. 📌 [ExecuteSQLQueriesSQLite.py](Python/ExecuteSQLQueriesSQLite.py): Defines a function to execute SQL queries on a SQLite database and return the results as pandas DataFrames, then executes and retrieves data for customer profits, employee order quantities, and invoice totals.
17. 📌 [DescribeQueryResults.py](Python/DescribeQueryResults.py): Displays summary statistics for each result set.
18. 📌 [MonthlyAnalysisAndMerge.py](Python/MonthlyAnalysisAndMerge.py): Performs monthly profit, quantity, and sales analyses by aggregating and merging data based on the date, fills missing values, and displays the merged DataFrame with the date as the index.
19. [CustomerAndEmployeeAnalysis.py](Python/CustomerAndEmployeeAnalysis.py): Performs profit analysis per customer and aggregates sales and order quantities per employee, then merges and displays the results.
20. [YearlyAnalysisAndMerge.py](Python/YearlyAnalysisAndMerge.py): Aggregates yearly profit, total quantity, and sales, merges the results based on the year, and displays the merged DataFrame.
21. [MonthlyTrendAnalysisPlot.py](Python/MonthlyTrendAnalysisPlot.py): Generates and displays a line plot showing monthly profit, total quantity, and sales trends over time.
22. [CustomerProfitDistributionPlot.py](Python/CustomerProfitDistributionPlot.py): Generates and displays a histogram showing the distribution of total profit per customer, including a kernel density estimate (KDE).
23. [MonthlyDistributionBoxplots.py](Python/MonthlyDistributionBoxplots.py): Creates subplots with boxplots to visualize the distribution of monthly profit, total quantity, and invoice total. Each subplot represents a different aspect of the data, showing how these metrics vary month by month.
24. [MonthlySalesComparison.py](Python/MonthlySalesComparison.py): This script converts the ORDER_YEAR and ORDER_MONTH columns in the employees DataFrame to a datetime format for easier plotting. It then creates a line plot comparing the total quantity of sales per month across different employees.
25. [YearlySalesPerEmployee.py](Python/YearlySalesPerEmployee.py): This script aggregates the employees DataFrame to yearly totals of sales quantities for each employee. It then creates a bar plot to visualise the total sales per year for each employee.
26. [EmployeeYearlySalesRankings.py](Python/EmployeeYearlySalesRankings.py): This script calculates the yearly rankings of total sales quantities for each employee and creates a bump chart to visualize the changes in rankings over the years.
27. [HexbinPlotProfitVsTax.py](Python/HexbinPlotProfitVsTax.py): This script generates a hexbin plot to visualize the relationship between monthly profit and monthly tax amounts.
28. [RainCloudPlotProfitPerMonth.py](Python/RainCloudPlotProfitPerMonth.py): This script generates a RainCloud plot to visualize the distribution of profit per month by transaction year. The RainCloud plot combines elements of boxplots, violin plots, and jittered scatter plots to provide a detailed view of the data distribution.
29. [ScatterPlotProfitVsTax.py](Python/ScatterPlotProfitVsTax.py): This script generates a scatter plot to visualize the relationship between profit per month and tax per month, with the data points colored by the transaction year. The plot provides a clear view of how profits and taxes are distributed across different years.
30. [InteractiveSalesAnalysis.py](Python/InteractiveSalesAnalysis.py): This script uses the plotly library to create interactive visualizations for analyzing sales data across different employees. It includes a line plot to compare monthly sales, a bar plot to compare yearly sales, and a bump chart to visualize the rankings of total sales per year for each employee.
