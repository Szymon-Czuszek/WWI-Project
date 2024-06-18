#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Create hexbin plot
hb = result.plot(kind='hexbin', x='PROFITPERMONTH', y='TAXPERMONTH', gridsize=25, cmap='Blues', mincnt=1)
hb.set_title("Hexbin Plot of Profit per Month vs. Tax per Month")
hb.set_xlabel("Profit per Month")
hb.set_ylabel("Tax per Month")
cb = hb.collections[0].colorbar
cb.set_label('Count')
plt.show()

