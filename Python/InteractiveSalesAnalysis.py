#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Convert ORDER_YEAR and ORDER_MONTH to datetime for easier plotting
invoices['ORDER_DATE'] = pd.to_datetime(invoices['ORDER_YEAR'].astype(str)
                                        + '-' + invoices['ORDER_MONTH'].astype(str) + '-01')
# Plot 1: Interactive Line Plot using Plotly
fig1 = px.line(
    invoices,
    x = 'ORDER_DATE',
    y = 'InvoiceTotal',
    color = 'FullName',
    labels = {'ORDER_DATE': 'Date', 'InvoiceTotal': 'Invoice Total', 'FullName': 'Employee'},
    title = 'Comparison of Monthly Sales Across Employees'
)
# Update layout to move the legend outside the plot
fig1.update_layout(
    legend = dict(
        title = 'Employee',
        x = 1.05,
        y = 1,
        traceorder = 'normal'
    ),
    margin = dict(l = 0, r = 150, t = 50, b = 50)
)
# Show plot
fig1.show()
# Aggregate data to yearly totals
yearly_totals = invoices.groupby(['FullName', 'ORDER_YEAR'])['InvoiceTotal'].sum().reset_index()
# Plot 2: Interactive Bar Plot using Plotly
fig2 = px.bar(
    yearly_totals,
    x = 'ORDER_YEAR',
    y = 'InvoiceTotal',
    color = 'FullName',
    labels = {'ORDER_YEAR': 'Year', 'InvoiceTotal': 'Invoice Total', 'FullName': 'Employee'},
    title = 'Total Sales Per Year for Each Employee'
)
# Update layout to move the legend outside the plot
fig2.update_layout(
    legend = dict(
        title = 'Employee',
        x = 1.05,
        y = 1,
        traceorder = 'normal'
    ),
    margin = dict(l = 0, r = 150, t = 50, b = 50)
)

# Show plot
fig2.show()
# Calculate the rankings for each year
yearly_totals['Rank'] = yearly_totals.groupby('ORDER_YEAR')['InvoiceTotal'].rank(method = 'first',
                                                                                 ascending = False
                                                                                )
# Pivot the data to get the rankings in the correct format for a bump chart
pivot = yearly_totals.pivot(index = 'FullName', columns = 'ORDER_YEAR', values = 'Rank')
# Plot 3: Interactive Bump Chart using Plotly
fig3 = go.Figure()
for name in pivot.index:
    fig3.add_trace(go.Scatter(
        x = pivot.columns,
        y = pivot.loc[name],
        mode = 'lines+markers',
        name = name,
        hoverinfo = 'text',
        text = [f'{name}<br>Year: {year}<br>Rank: {rank}' for year, rank in zip(pivot.columns, pivot.loc[name])]
    ))
# Update the layout
fig3.update_layout(
    title = 'Rankings of Total Sales Per Year for Each Employee',
    xaxis_title = 'Year',
    yaxis_title = 'Rank',
    yaxis = dict(autorange='reversed'),  # Invert the y-axis to have rank 1 at the top
    legend = dict(
        title = 'Employee',
        x = 1.05,
        y = 1,
        traceorder = 'normal'
    ),
    margin = dict(l = 0, r = 150, t = 50, b = 50)
)
# Show plot
fig3.show()

