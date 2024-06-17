#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Aggregate data to yearly totals
yearly_totals = employees.groupby(['FullName', 'ORDER_YEAR'])['Total_Quantity'].sum().reset_index()
# : Total Sales Per Year for Each Employee
plt.figure(figsize = (14, 7))
sns.barplot(data=yearly_totals, x = 'ORDER_YEAR', y = 'Total_Quantity', hue = 'FullName')
plt.title('Total Sales Per Year for Each Employee')
plt.xlabel('Year')
plt.ylabel('Total Quantity')
# Position the legend outside the plot
plt.legend(bbox_to_anchor = (1.05, 1), loc = 'upper left')
plt.tight_layout(rect = [0, 0, 0.85, 1])  # Adjust the layout to make room for the legend
plt.show()

