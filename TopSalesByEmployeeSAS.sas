%MACRO ImportWWI(subfolder);
    %LET name = WWI_%SUBSTR(&subfolder, 1, 3);
    LIBNAME &name BASE "/shared/home/name.surname@edu.uekat.pl/WWI/&subfolder";
    PROC CONTENTS DATA = &name.._ALL_ NODS;
    RUN;
%MEND;
%ImportWWI(Application);
%ImportWWI(Purchasing);
%ImportWWI(Sales);
%ImportWWI(Warehouse);
PROC DS2;
DATA query_result/ overwrite = yes;
method run();
SET {
SELECT
    p.FULLNAME,
    p.EMAILADDRESS,
    l.STOCKITEMID,
    SUM(l.UNITPRICE) AS UNITPRICE_TOTAL,
    SUM(l.QUANTITY) AS QUANTITY_TOTAL,
    l.TAXRATE,
    YEAR(o.ORDERDATE),
    MONTH(o.ORDERDATE)
FROM
    WWI_SAL.ORDERLINES l
JOIN
    WWI_SAL.ORDERS o
ON
    l.ORDERID = o.ORDERID
JOIN
    WWI_APP.PEOPLE p
ON
    o.SALESPERSONPERSONID = p.PERSONID
GROUP BY
    p.FULLNAME,
    p.EMAILADDRESS,
    YEAR(o.ORDERDATE),
    MONTH(o.ORDERDATE),
    l.STOCKITEMID,
    l.TAXRATE
ORDER BY
    SUM(l.UNITPRICE * l.QUANTITY) DESC
LIMIT 15
} ;
end;
enddata;
RUN;
QUIT;
PROC PRINT
    DATA = work.query_result;
RUN;