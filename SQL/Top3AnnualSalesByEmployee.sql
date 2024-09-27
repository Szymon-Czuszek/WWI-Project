WITH TotalSalesPerEmployee AS (
   SELECT
       EXTRACT(YEAR FROM o.INVOICEDATE) AS ORDER_YEAR,
       p.FULLNAME,
       SUM(l.UNITPRICE) AS TotalSales
   FROM
       WWI.INVOICELINES l
   JOIN
       WWI.INVOICES o ON l.INVOICEID = o.INVOICEID
   JOIN
       WWI.PEOPLE2 p ON o.SALESPERSONPERSONID = p.PERSONID
   GROUP BY
       EXTRACT(YEAR FROM o.INVOICEDATE),
       p.FULLNAME
),
RankedSales AS (
   SELECT
       ORDER_YEAR,
       FULLNAME,
       TotalSales,
       ROW_NUMBER() OVER (PARTITION BY ORDER_YEAR ORDER BY TotalSales DESC) AS SalesRank
   FROM
       TotalSalesPerEmployee
)
SELECT
   ORDER_YEAR,
   FULLNAME,
   TotalSales
FROM
   RankedSales
WHERE
   SalesRank <= 3
ORDER BY
   ORDER_YEAR,
   SalesRank
;