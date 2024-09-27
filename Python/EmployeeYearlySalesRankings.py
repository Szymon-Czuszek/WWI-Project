#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Calculate the rankings for each year
yearly_totals['Rank'] = yearly_totals.groupby('ORDER_YEAR')['Total_Quantity'].rank(method = 'first', ascending = False)
# Pivot the data to get the rankings in the correct format for a bump chart
pivot = yearly_totals.pivot(index = 'FullName', columns = 'ORDER_YEAR', values = 'Rank')
# Bump Chart of Rankings of Total Sales Per Year for Each Employee
plt.figure(figsize = (14, 7))
for name in pivot.index:
    plt.plot(pivot.columns, pivot.loc[name], marker = 'o', label = name)
plt.gca().invert_yaxis()  # Invert the y-axis to have rank 1 at the top
plt.title('Rankings of Total Sales Per Year for Each Employee')
plt.xlabel('Year')
plt.ylabel('Rank')
# Position the legend outside the plot
plt.legend(bbox_to_anchor = (1.05, 1), loc = 'upper left')
plt.tight_layout(rect = [0, 0, 0.85, 1])  # Adjust the layout to make room for the legend
plt.show()

