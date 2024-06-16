#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Convert ORDER_YEAR and ORDER_MONTH to datetime for easier plotting
employees['ORDER_DATE'] = pd.to_datetime(employees['ORDER_YEAR'].astype(str) + '-' + employees['ORDER_MONTH'].astype(str) + '-01')
# Comparison of Monthly Sales Across Employees
plt.figure(figsize = (14, 7))
sns.lineplot(data = employees, x = 'ORDER_DATE', y = 'Total_Quantity', hue = 'FullName')
plt.title('Comparison of Monthly Sales Across Employees')
plt.xlabel('Date')
plt.ylabel('Total Quantity')
# Position the legend outside the plot
plt.legend(bbox_to_anchor = (1.05, 1), loc = 'upper left')
plt.tight_layout(rect=[0, 0, 0.85, 1])  # Adjust the layout to make room for the legend
plt.show()

