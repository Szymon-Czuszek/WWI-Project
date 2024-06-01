SELECT
   EXTRACT(YEAR FROM t.TransactionDate) AS TransactionYear,
   s.SupplierName,
   TO_CHAR(SUM(t.TransactionAmount), '$999,999,999.99') AS TotalTransactionAmount
FROM
   WWI.suppliers s
JOIN
   WWI.suppliertransactions t ON s.SupplierID = t.SupplierID
GROUP BY
   EXTRACT(YEAR FROM t.TransactionDate), s.SupplierName
ORDER BY
   TransactionYear ASC, TotalTransactionAmount DESC;