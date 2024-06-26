SELECT
   p.FULLNAME,
   EXTRACT(YEAR FROM o.INVOICEDATE) AS ORDER_YEAR,
   EXTRACT(MONTH FROM o.INVOICEDATE) AS ORDER_MONTH,
   SUM(l.UNITPRICE) AS InvoiceTotal,
   SUM(SUM(l.UNITPRICE)) OVER (PARTITION BY p.FULLNAME ORDER BY EXTRACT(YEAR FROM o.INVOICEDATE), EXTRACT(MONTH FROM o.INVOICEDATE)) AS CumulativeInvoiceTotal
FROM
   WWI.INVOICELINES l
JOIN
   WWI.INVOICES o
ON
   l.INVOICEID = o.INVOICEID
JOIN
   WWI.PEOPLE2 p
ON
   o.SALESPERSONPERSONID = p.PERSONID
GROUP BY
   EXTRACT(YEAR FROM o.INVOICEDATE),
   EXTRACT(MONTH FROM o.INVOICEDATE),
   p.FULLNAME
;