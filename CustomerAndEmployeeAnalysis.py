#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Customer Profit Analysis
customer_profit = result.groupby('CustomerName')['PROFITPERMONTH'].sum().reset_index()
# Employee Sales & Order Quantity Analysis
employee_quantity = employees.groupby('FullName')['Total_Quantity'].sum().reset_index()
employee_sales = invoices.groupby('FullName')['InvoiceTotal'].sum().reset_index()
merged_employees = pd.merge(employee_quantity, employee_sales, on = 'FullName', how = 'outer')
display(customer_profit, merged_employees)

