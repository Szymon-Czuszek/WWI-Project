#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Create scatter plot using sns.relplot
sns.relplot(data = result,
            x = 'PROFITPERMONTH',
            y = 'TAXPERMONTH',
            hue = 'TRANSACTIONYEAR',
            palette = 'viridis',
            aspect = 1.5
           )
plt.title("Scatter Plot of Profit per Month vs. Tax per Month")
plt.xlabel("Profit per Month")
plt.ylabel("Tax per Month")
plt.show()

