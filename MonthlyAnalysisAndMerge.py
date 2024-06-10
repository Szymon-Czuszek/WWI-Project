#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Monthly Profit Analysis
monthly_profit = result.groupby(['TRANSACTIONYEAR', 'TRANSACTIONMONTH'])['PROFITPERMONTH'].sum().reset_index()
monthly_profit['DATE'] = pd.to_datetime(monthly_profit['TRANSACTIONYEAR'].astype(str) + '-'
                                        + monthly_profit['TRANSACTIONMONTH'].astype(str))
# Monthly Total Quantity Analysis
monthly_quantity = employees.groupby(['ORDER_YEAR', 'ORDER_MONTH'])['Total_Quantity'].sum().reset_index()
monthly_quantity['DATE'] = pd.to_datetime(monthly_quantity['ORDER_YEAR'].astype(str) + '-'
                                          + monthly_quantity['ORDER_MONTH'].astype(str))
# Convert ORDER_YEAR and ORDER_MONTH to string and create a date column
invoices['DATE'] = pd.to_datetime(invoices['ORDER_YEAR'].astype(str) + '-'
                                  + invoices['ORDER_MONTH'].astype(str))
# Monthly Sales Analysis
monthly_sales = invoices.groupby(['ORDER_YEAR', 'ORDER_MONTH'])['InvoiceTotal'].sum().reset_index()
monthly_sales['DATE'] = pd.to_datetime(monthly_sales['ORDER_YEAR'].astype(str) + '-'
                                       + monthly_sales['ORDER_MONTH'].astype(str))
# Merge the three DataFrames based on the DATE column
merged_data = pd.merge(monthly_profit, monthly_quantity, on = 'DATE', how = 'outer')
merged_data = pd.merge(merged_data, monthly_sales, on = 'DATE', how = 'outer')

# Fill missing values with 0
merged_data.fillna(0, inplace = True)
# Drop not needed columns
merged_data.drop(['TRANSACTIONYEAR',
                  'TRANSACTIONMONTH',
                  'ORDER_YEAR_x',
                  'ORDER_MONTH_x',
                  'ORDER_YEAR_y',
                  'ORDER_MONTH_y'
                 ],
                 axis = 1,
                 inplace = True
                )
# Set the 'DATE' column as the index
merged_data.set_index('DATE', inplace = True)
# Display the updated DataFrame with 'DATE' as the index
display(merged_data)

