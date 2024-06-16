#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Create subplots
fig, axes = plt.subplots(1, 3, figsize = (12, 6))
# Monthly Profit Boxplot
sns.boxplot(ax = axes[0], x = 'TRANSACTIONMONTH', y = 'PROFITPERMONTH', data = result)
axes[0].set_title('Monthly Profit Distribution')
axes[0].set_xlabel('Month')
axes[0].set_ylabel('Profit per Month')
# Monthly Quantity Boxplot
sns.boxplot(ax = axes[1], x = 'ORDER_MONTH', y = 'Total_Quantity', data = employees)
axes[1].set_title('Monthly Quantity Distribution')
axes[1].set_xlabel('Month')
axes[1].set_ylabel('Total Quantity')
# Monthly Sales Boxplot
sns.boxplot(ax = axes[2], x = 'ORDER_MONTH', y = 'InvoiceTotal', data = invoices)
axes[2].set_title('Monthly Sales Distribution')
axes[2].set_xlabel('Month')
axes[2].set_ylabel('Invoice Total')
plt.tight_layout()  # Adjust layout
plt.show()

