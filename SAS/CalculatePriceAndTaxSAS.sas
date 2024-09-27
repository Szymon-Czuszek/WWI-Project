/* Using DS2 to declare variables and multiply columns */
PROC DS2;
    DATA result_data / overwrite = yes;
        dcl double PRICE_TOTAL;
        dcl double TAX_TOTAL;
                method run();
            SET result;
            PRICE_TOTAL = UNITPRICE_TOTAL * QUANTITY_TOTAL;
            TAX_TOTAL = (PRICE_TOTAL * TAXRATE) / 100;
            output;
        end;
    enddata;
RUN;
QUIT;
/* Print the results */
PROC PRINT
    DATA = result_data;
    VAR RecordID FullName EmailAddress YEAR MONTH StockItemID PRICE_TOTAL TAX_TOTAL;
RUN;