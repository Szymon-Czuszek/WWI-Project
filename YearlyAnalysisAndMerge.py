#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Yearly Profit Analysis
yearly_profit = result.groupby('TRANSACTIONYEAR')['PROFITPERMONTH'].sum().reset_index()
# Yearly Total Quantity Analysis
yearly_quantity = employees.groupby('ORDER_YEAR')['Total_Quantity'].sum().reset_index()
# Yearly Sales Analysis
yearly_sales = invoices.groupby('ORDER_YEAR')['InvoiceTotal'].sum().reset_index()
# Rename columns to have a common name
yearly_profit.rename(columns = {'TRANSACTIONYEAR': 'Year'}, inplace = True)
yearly_quantity.rename(columns = {'ORDER_YEAR': 'Year'}, inplace = True)
yearly_sales.rename(columns = {'ORDER_YEAR': 'Year'}, inplace = True)
# Merge the dataframes
merged_df = yearly_profit.merge(yearly_quantity, on = 'Year', how = 'outer')
merged_df = merged_df.merge(yearly_sales, on = 'Year', how = 'outer')
# Display the merged dataframe
display(merged_df)

