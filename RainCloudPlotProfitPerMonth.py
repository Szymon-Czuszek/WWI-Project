#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Plot RainCloud for PROFITPERMONTH
plt.figure(figsize = (12, 8))
pt.RainCloud(x = 'TRANSACTIONYEAR',
             y = 'PROFITPERMONTH',
             data = result,
             palette = "Set2",
             bw = .2,
             width_viol = 1,
             ax = None,
             orient = 'h'
            )
plt.title("RainCloud Plot for PROFIT PER MONTH by TRANSACTION YEAR")
plt.show()

