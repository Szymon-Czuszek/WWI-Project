SELECT
   o.CountryName,
   s.StateProvinceName,
   c.CityName,
   COUNT(*) AS NumberOfCustomers,
   SUM(t.TransactionAmount) AS TotalTransactionAmount
FROM
   WWI.customers u
JOIN
   WWI.cities c ON u.DeliveryCityID = c.CityID
JOIN
   WWI.stateprovinces s ON c.StateProvinceID = s.StateProvinceID
JOIN
   WWI.countries o ON s.CountryID = o.CountryID
JOIN
   WWI.customertransactions t ON u.CustomerID = t.CustomerID
GROUP BY
   GROUPING SETS ((o.CountryName, s.StateProvinceName, c.CityName), (o.CountryName, s.StateProvinceName), (o.CountryName))
ORDER BY
   o.CountryName, s.StateProvinceName, c.CityName;