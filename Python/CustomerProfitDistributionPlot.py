#!/usr/bin/env python
# coding: utf-8

# In[ ]:


plt.figure(figsize = (12, 6))
# Plot Monthly Profit
sns.lineplot(data = monthly_profit, x = 'DATE', y = 'PROFITPERMONTH', label = 'Profit')
# Plot Monthly Total Quantity
sns.lineplot(data = monthly_quantity, x = 'DATE', y = 'Total_Quantity', label = 'Total Quantity')
# Plot Monthly Sales
sns.lineplot(data = monthly_sales, x = 'DATE', y = 'InvoiceTotal', label = 'Sales')
plt.title('Trend Analysis Over Time')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

