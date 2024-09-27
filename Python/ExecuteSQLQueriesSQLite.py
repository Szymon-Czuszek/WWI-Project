#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Define a function to execute SQL queries and return results as pandas DataFrame
def query_data(query, connection = sqlite3.connect('wwi.db')):
        return pd.read_sql_query(query, connection)
    
wwi = sqlite3.connect('wwi.db')

# Create SQL queries for all the data used in the project
result = query_data("""
SELECT
    c.CUSTOMERNAME,
    strftime('%Y', i.INVOICEDATE) AS TRANSACTIONYEAR,
    strftime('%m', i.INVOICEDATE) AS TRANSACTIONMONTH,
    SUM(l.LINEPROFIT) AS PROFITPERMONTH,
    SUM(l.TAXAMOUNT) AS TAXPERMONTH
FROM
    INVOICELINES l
JOIN
    INVOICES i
ON
    l.INVOICEID = i.INVOICEID
JOIN
    CUSTOMERS c
ON
    i.CUSTOMERID = c.CUSTOMERID
GROUP BY
    strftime('%Y', i.INVOICEDATE),
    strftime('%m', i.INVOICEDATE),
    c.CUSTOMERNAME
ORDER BY
    strftime('%Y', i.INVOICEDATE),
    strftime('%m', i.INVOICEDATE),
    c.CUSTOMERNAME
;
""", wwi)

employees = query_data("""
SELECT
    p.FULLNAME,
    strftime('%Y', o.ORDERDATE) AS ORDER_YEAR,
    strftime('%m', o.ORDERDATE) AS ORDER_MONTH,
    SUM(l.QUANTITY) AS Total_Quantity
FROM
    ORDERLINES l
JOIN
    ORDERS o
ON
    l.ORDERID = o.ORDERID
JOIN
    PEOPLE p
ON
    o.SALESPERSONPERSONID = p.PERSONID
GROUP BY
    p.FULLNAME,
    strftime('%Y', o.ORDERDATE),
    strftime('%m', o.ORDERDATE)
;
""", wwi)

invoices = query_data("""
SELECT
    p.FULLNAME,
    strftime('%Y', o.INVOICEDATE) AS ORDER_YEAR,
    strftime('%m', o.INVOICEDATE) AS ORDER_MONTH,
    SUM(l.UNITPRICE) AS InvoiceTotal
FROM
    INVOICELINES l
JOIN
    INVOICES o
ON
    l.INVOICEID = o.INVOICEID
JOIN
    PEOPLE p
ON
    o.SALESPERSONPERSONID = p.PERSONID
GROUP BY
    p.FULLNAME,
    strftime('%Y', o.INVOICEDATE),
    strftime('%m', o.INVOICEDATE)
;
""", wwi)

